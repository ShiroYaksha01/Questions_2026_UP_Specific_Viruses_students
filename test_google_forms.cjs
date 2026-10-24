const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const questions = JSON.parse(fs.readFileSync('questions_db.json', 'utf8'));
const forms = new Map(), properties = new Map();
let triggers = [], failNext = false;
function item(form) {
  return {
    setTitle(value) { this.title = value; return this; },
    setHelpText(value) { this.help = value; return this; },
    setRequired(value) { this.required = value; return this; },
    setPoints(value) { this.points = value; return this; },
    createChoice(value, correct) { return { value, correct }; },
    setChoices(value) {
      if (failNext) { failNext = false; throw new Error('Temporary service error'); }
      this.choices = value; return this;
    },
    setFeedbackForCorrect(value) { this.correctFeedback = value; return this; },
    setFeedbackForIncorrect(value) { this.incorrectFeedback = value; return this; }
  };
}
const context = vm.createContext({
  Date, console,
  Logger: { log() {} },
  PropertiesService: { getScriptProperties: () => ({
    getProperty: key => properties.get(key) || null,
    setProperty(key, value) { properties.set(key, value); }
  }) },
  LockService: { getScriptLock: () => ({ tryLock: () => true, releaseLock() {} }) },
  ScriptApp: {
    getProjectTriggers: () => triggers.slice(),
    deleteTrigger(trigger) { triggers = triggers.filter(t => t !== trigger); },
    newTrigger(handler) { return {
      timeBased() { return this; }, after() { return this; },
      create() { triggers.push({ getHandlerFunction: () => handler }); }
    }; }
  },
  FormApp: {
    create(title, published) {
      const form = {
        title, published, items: [], id: String(forms.size + 1),
        getId() { return this.id; },
        getEditUrl() { return `https://forms.example/${this.id}/edit`; },
        setIsQuiz(value) { this.quiz = value; return this; },
        setDescription(value) { this.description = value; return this; },
        setShuffleQuestions() { return this; },
        getItems() { return this.items; },
        addMultipleChoiceItem() { const created = item(this); this.items.push(created); return created; },
        deleteItem(value) { this.items = this.items.filter(i => i !== value); }
      };
      forms.set(form.id, form); return form;
    },
    openById: id => forms.get(id),
    createFeedback: () => ({ setText(value) { this.text = value; return this; }, build() { return this.text; } })
  }
});
vm.runInContext(fs.readFileSync('google_forms_mcq.gs', 'utf8'), context);
context.createMcqForms();
assert.equal(forms.size, 3);
assert.equal(triggers.length, 1, 'Incomplete export should schedule one continuation');
// Simulate a timeout after the item was created but before its progress was saved.
const stateKey = 'mcq_google_forms_export_v1';
const interrupted = JSON.parse(properties.get(stateKey));
interrupted.forms['1'].pending = true;
properties.set(stateKey, JSON.stringify(interrupted));
forms.get(interrupted.forms['1'].id).addMultipleChoiceItem();
failNext = true;
assert.throws(() => context.resumeMcqForms(), /Temporary service error/);
context.createMcqForms();
for (let run = 0; triggers.length && run < 20; run++) context.resumeMcqForms();
assert.equal(triggers.length, 0);
assert.deepEqual([...forms.values()].map(f => f.items.length), [160, 40, 50]);
for (const form of forms.values()) {
  assert.equal(form.published, false);
  assert.equal(form.quiz, true);
  const subject = questions.filter(q => form.title.startsWith(q.lecture_name));
  form.items.forEach((created, index) => {
    const q = subject[index];
    assert.equal(created.title, `${index + 1}. ${q.question}`);
    assert.equal(created.points, 1);
    assert.equal(created.required, true);
    assert.equal(created.choices.filter(c => c.correct).length, 1);
    assert.equal(created.choices.find(c => c.correct).value, `${q.correct_answer}. ${q.correct_text}`);
    assert.equal(created.correctFeedback, `Correct answer: ${q.correct_answer}. ${q.correct_text}`);
    assert.equal(created.incorrectFeedback, created.correctFeedback);
  });
}
context.createMcqForms();
assert.equal(forms.size, 3, 'Rerunning must reuse existing forms');
assert.deepEqual([...forms.values()].map(f => f.items.length), [160, 40, 50]);
console.log('Passed: 250 questions, 3 draft quizzes, exact answer keys, batching, retry, no duplicates.');
