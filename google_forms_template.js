/**
 * Paste the GENERATED google_forms_mcq.gs file into a new Google Apps Script
 * project, then run createMcqForms and approve the Google permissions prompt.
 * Creates three unpublished quiz forms. Work continues in timed batches.
 * Run showMcqFormLinks to print edit links and progress at any time.
 * Rerun createMcqForms to resume after an error; it reuses the same forms.
 * Do not edit form questions while the import is still running.
 */
const MCQ_SUBJECTS = __MCQ_SUBJECTS__;
const MCQ_EXPORT_HASH = '__MCQ_EXPORT_HASH__';
const MCQ_STATE_KEY = 'mcq_google_forms_export_v1';
const MCQ_BATCH_SIZE = 40;
const MCQ_RUN_MS = 240000;

function createMcqForms() {
  resumeMcqForms();
}

function resumeMcqForms() {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(1000)) {
    Logger.log('An import is already running. Wait for it to finish.');
    return;
  }
  try {
    clearMcqTriggers_();
    const started = Date.now();
    const properties = PropertiesService.getScriptProperties();
    const saved = properties.getProperty(MCQ_STATE_KEY);
    const state = saved ? JSON.parse(saved) : { hash: MCQ_EXPORT_HASH, forms: {} };
    if (state.hash !== MCQ_EXPORT_HASH) {
      throw new Error('The question data changed. Use a new Apps Script project for a fresh set of forms.');
    }
    const save = () => properties.setProperty(MCQ_STATE_KEY, JSON.stringify(state));
    let added = 0;
    for (const subject of MCQ_SUBJECTS) {
      if (!state.forms[subject.id]) {
        const form = FormApp.create(`${subject.name} — MCQ Quiz 2026`, false);
        state.forms[subject.id] = { id: form.getId(), cursor: 0, pending: false };
        save();
      }
    }
    for (const subject of MCQ_SUBJECTS) {
      const entry = state.forms[subject.id];
      const form = FormApp.openById(entry.id);
      form.setIsQuiz(true);
      form.setShuffleQuestions(false);
      form.setDescription(
        `${subject.name}: ${subject.questions.length} multiple-choice questions. ` +
        'Each question is worth 1 point. Answer keys follow the source PDFs. ' +
        'Correct answers are included in quiz feedback.'
      );
      // Recover an interrupted item before advancing the saved cursor.
      const items = form.getItems();
      if (entry.pending && items.length === entry.cursor + 1) {
        form.deleteItem(items[items.length - 1]);
      } else if (items.length !== entry.cursor) {
        throw new Error(`Question count changed in ${subject.name}. Restore the original questions before resuming.`);
      }
      entry.pending = false;
      save();
      while (entry.cursor < subject.questions.length &&
             added < MCQ_BATCH_SIZE && Date.now() - started < MCQ_RUN_MS) {
        const index = entry.cursor;
        const question = subject.questions[index];
        entry.pending = true;
        save();
        let item;
        try {
          item = form.addMultipleChoiceItem();
          item.setTitle(`${index + 1}. ${question.question}`);
          item.setHelpText(
            `${question.source} · Original question ${question.question_id}` +
            (question.lesson ? ` · ${question.lesson}` : '')
          );
          item.setRequired(true);
          item.setPoints(1);
          item.setChoices(Object.keys(question.options).map(letter =>
            item.createChoice(`${letter}. ${question.options[letter]}`, letter === question.correct_answer)
          ));
          const feedback = FormApp.createFeedback()
            .setText(`Correct answer: ${question.correct_answer}. ${question.correct_text}`)
            .build();
          item.setFeedbackForCorrect(feedback);
          item.setFeedbackForIncorrect(feedback);
          entry.cursor = index + 1;
          entry.pending = false;
          save();
          added++;
        } catch (error) {
          // Remove the incomplete item so retrying cannot duplicate it.
          if (item) form.deleteItem(item);
          entry.cursor = index;
          entry.pending = false;
          save();
          throw error;
        }
      }
    }
    const unfinished = MCQ_SUBJECTS.some(subject =>
      state.forms[subject.id].cursor < subject.questions.length);
    if (unfinished) {
      ScriptApp.newTrigger('resumeMcqForms').timeBased().after(60000).create();
      Logger.log('Next batch scheduled. No need to click Run again.');
    } else {
      Logger.log('Complete. Open each edit link, review quiz/grade-release settings, then publish when ready.');
    }
    showMcqFormLinks();
  } finally {
    lock.releaseLock();
  }
}

function showMcqFormLinks() {
  const saved = PropertiesService.getScriptProperties().getProperty(MCQ_STATE_KEY);
  if (!saved) {
    Logger.log('Run createMcqForms first.');
    return;
  }
  const state = JSON.parse(saved);
  for (const subject of MCQ_SUBJECTS) {
    const entry = state.forms[subject.id];
    if (!entry) continue;
    const form = FormApp.openById(entry.id);
    Logger.log(`${subject.name}: ${entry.cursor}/${subject.questions.length} questions`);
    Logger.log(`Edit: ${form.getEditUrl()}`);
  }
}

function clearMcqTriggers_() {
  ScriptApp.getProjectTriggers().forEach(trigger => {
    if (trigger.getHandlerFunction() === 'resumeMcqForms') ScriptApp.deleteTrigger(trigger);
  });
}

function pauseMcqImport() {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(1000)) {
    throw new Error('A batch is currently running. Run pauseMcqImport again after it finishes.');
  }
  try {
    clearMcqTriggers_();
    Logger.log('Paused. Run createMcqForms to resume.');
  } finally {
    lock.releaseLock();
  }
}
