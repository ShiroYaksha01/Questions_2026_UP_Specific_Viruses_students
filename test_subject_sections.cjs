const assert = require('node:assert/strict');
const fs = require('node:fs');
const { JSDOM } = require('./.qa_tools/node_modules/jsdom');

const html = fs.readFileSync('index.html', 'utf8');
const db = JSON.parse(fs.readFileSync('questions_db.json', 'utf8'));
const dom = new JSDOM(html, {
  runScripts: 'dangerously', url: 'https://study.example/',
  beforeParse(w) { w.scrollTo = () => {}; }
});
const { window } = dom;
const doc = window.document;
const get = id => doc.getElementById(id);
const click = node => node.click();
const buttons = () => [...get('subjectSections').querySelectorAll('button')];
const snapshot = () => JSON.parse(window.localStorage.getItem(
  `metabolic_biochem_session_v1_subject_${get('lectureFilter').value}`));

assert.ok(get('subjectSections'), 'Subject sections must be visible');
assert.equal(buttons().length, 3);
assert.deepEqual([...get('lectureFilter').options].map(o => o.value), ['1', '2', '3']);
assert.equal(get('paletteGrid').children.length, 160);
click(get('optionsContainer').children[0]);
const metabolic = snapshot();
assert.equal(Object.keys(metabolic.answers).length, 1);

for (const [id, count, name] of [[2, 40, 'Clinical Biochemistry'], [3, 50, 'Clinical Biology']]) {
  click(buttons().find(b => b.dataset.subject === String(id)));
  assert.equal(get('lectureFilter').value, String(id));
  assert.equal(get('paletteGrid').children.length, count);
  assert.equal(get('badgeLecture').textContent, name);
  const initial = snapshot();
  const question1 = db.find(q => q.lecture_id === id && q.question_id === 1);
  click(get('paletteGrid').children[initial.questionIds.indexOf(question1.global_id)]);
  const saved = snapshot();
  assert.ok(saved.questionIds.every(qid => db.find(q => q.global_id === qid).lecture_id === id));
  const q = db.find(q => q.global_id === saved.currentId);
  const correctIndex = saved.optionOrder[q.global_id].indexOf(q.correct_answer);
  click(get('optionsContainer').children[correctIndex]);
  assert.equal(get('accuracyPill').textContent, '1 Correct (100%)');
  assert.ok(get('explAnswerLabel').textContent.endsWith(q.correct_text));
}
// Check the explicit answer key after choice shuffling, within Clinical Biology.
const biology = snapshot();
const mona1 = db.find(q => q.source === 'MCQ kru Mona.pdf' && q.question_id === 1);
assert.equal(mona1.correct_answer, 'B');
click(get('paletteGrid').children[biology.questionIds.indexOf(mona1.global_id)]);
const monaIndex = snapshot().optionOrder[mona1.global_id].indexOf('B');
click(get('optionsContainer').children[monaIndex]);
assert.ok(get('optionsContainer').children[monaIndex].classList.contains('is-correct'));
assert.ok(get('explAnswerLabel').textContent.endsWith('Stop blood loss after blood vessel injury'));
assert.equal(get('paletteGrid').children.length, 50);
click(buttons().find(b => b.dataset.subject === '1'));
assert.deepEqual(snapshot().answers, metabolic.answers);
assert.deepEqual(snapshot().questionIds, metabolic.questionIds);
click(buttons().find(b => b.dataset.subject === '2'));
assert.equal(Object.keys(snapshot().answers).length, 1);
assert.equal(buttons().find(b => b.dataset.subject === '2').getAttribute('aria-pressed'), 'true');

// The source deliberately highlights B for clinical Q5; preserve that key.
const clinical = snapshot();
const question5 = db.find(q => q.lecture_id === 2 && q.question_id === 5);
assert.equal(question5.correct_answer, 'B');
click(get('paletteGrid').children[clinical.questionIds.indexOf(question5.global_id)]);
const index5 = snapshot().optionOrder[question5.global_id].indexOf('B');
click(get('optionsContainer').children[index5]);
assert.ok(get('optionsContainer').children[index5].classList.contains('is-correct'));
assert.ok(get('explAnswerLabel').textContent.endsWith(question5.correct_text));

const stored = Object.fromEntries(Object.keys(window.localStorage).map(key => [key, window.localStorage.getItem(key)]));
const reopened = new JSDOM(html, {
  runScripts: 'dangerously', url: 'https://study.example/',
  beforeParse(w) { for (const [key, value] of Object.entries(stored)) w.localStorage.setItem(key, value); }
});
assert.equal(reopened.window.document.getElementById('lectureFilter').value, '2');
assert.equal(reopened.window.document.getElementById('paletteGrid').children.length, 40);
assert.equal(reopened.window.document.getElementById('accuracyPill').textContent, '2 Correct (100%)');
console.log('Passed: separate subjects, counts, PDF answers, independent progress, reload restoration.');
dom.window.close();
reopened.window.close();
