# Biochemistry and Clinical Biology MCQ Review

An offline multiple choice review site with three separate subject sections: 160 Metabolic Biochemistry questions from pages 1–18 of `MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf`, 40 Clinical Biochemistry questions, and 50 Clinical Biology questions. `Clinical Bio+chem final.pdf` supplies 40 Clinical Biochemistry and 10 Clinical Biology questions using highlighted answer choices. `MCQ kru Mona.pdf` supplies another 40 Clinical Biology questions on Disorder of Hemostasis and Coagulation Disorders using its explicit “Correct answer:” lines; each answer letter is checked against its written answer text. The metabolic case questions beginning after question 160 and matching exercises are excluded. Use the subject buttons above the questions to switch sections. Each section has its own saved session, answers, question order, and settings; switching subjects preserves progress. Question sets always contain one subject.

The clinical answer key follows the highlights exactly, including Clinical Biochemistry question 5, where the PDF highlights B despite the question asking about metabolic alkalosis.

## Use the website

Open `index.html` in a browser. The page contains its question data and works offline. You can shuffle questions and choices, practice a smaller set, bookmark questions, and review your score as you answer. After selecting a choice, “Correct answer:” displays the PDF's keyed choice with its current letter, accounting for shuffled choices.

On phones, use the fixed bottom bar or swipe across the question card to move between questions. The Navigator sheet filters questions by answer status or bookmarks; tablets with enough width show a persistent navigator. Study settings are available from the header.

The site saves answers, question and choice order, position, and settings for each subject in this browser after each change. Refreshing or reopening the page restores the last selected subject and its session until you reset progress or confirm a new session. Bookmarks and theme are saved separately. This storage is local to the current browser and device, so it does not sync across devices or private browsing sessions. If storage is blocked, the page warns that progress cannot be recovered. A second tab that changes the same subject's session prompts the older tab to reload the latest saved progress.

The site is also a static page that can be hosted with the included `vercel.json` configuration.

## Export to Google Forms

`google_forms_mcq.gs` contains all 250 questions and creates three separate, automatically graded draft quizzes. Paste it into a new Google Apps Script project and run `createMcqForms`. See [GOOGLE_FORMS_SETUP.md](GOOGLE_FORMS_SETUP.md) for setup, batch progress, quiz feedback, and publishing instructions. Regenerate the export with `python build_google_forms.py`; verify it with `node test_google_forms.cjs`.

## Rebuild from the PDF

Rebuilding requires Python 3, the `pypdf` and `pymupdf` packages, and Poppler's `pdftotext` utility on your PATH. Install the Python packages with `python -m pip install pypdf pymupdf`; install Poppler using your operating system's package manager.

From this directory, run:

```bash
python3 build_review_data.py
python3 build_clinical_data.py
python3 build_standalone_app.py
```

The first command validates and writes the metabolic questions to `questions_db.json`. The second adds both clinical subjects from both clinical PDFs, verifying four choices and one answer per question. It matches the yellow fills in `Clinical Bio+chem final.pdf` and the written answer keys in `MCQ kru Mona.pdf`, including questions split across pages and choices sharing a line. It can also run on the existing database without Poppler and safely replaces previously imported clinical questions. The final command embeds the database plus `standalone_app.js` and `standalone_mobile.css` in `index.html`. Source PDFs are kept in this project so the generated data can be rebuilt.

To run the PDF extraction checks, run `python -m unittest test_mona_data.py`. To run the subject interaction checks, install the test dependency with `npm install --prefix .qa_tools jsdom --no-audit --no-fund`, then run `node test_subject_sections.cjs`.
