# Metabolic Biochemistry MCQ Review

An offline multiple choice review site for the 160 numbered questions on pages 1–18 of `MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf`. The correct answers come from the PDF's highlighted options. The case questions beginning after question 160 and the matching exercises on later pages are excluded.

## Use the website

Open `index.html` in a browser. The page contains its question data and works offline. You can shuffle questions and choices, practice a smaller set, bookmark questions, and review your score as you answer. The answer shown after selecting a choice is the highlighted choice from the PDF; the PDF does not provide written explanations.

On phones, use the fixed bottom bar or swipe across the question card to move between questions. The Navigator sheet filters questions by answer status or bookmarks; tablets with enough width show a persistent navigator. Study settings are available from the header.

The site saves answers, question and choice order, position, and settings in this browser after each change. Refreshing or reopening the page restores the same session until you reset progress or confirm a new session. Bookmarks and theme are saved separately. This storage is local to the current browser and device, so it does not sync across devices or private browsing sessions. If storage is blocked, the page warns that progress cannot be recovered. A second tab that changes the session prompts the older tab to reload the latest saved progress.

The site is also a static page that can be hosted with the included `vercel.json` configuration.

## Rebuild from the PDF

Rebuilding requires Python 3, the `pypdf` package, and Poppler's `pdftotext` utility on your PATH. Install `pypdf` with `python3 -m pip install pypdf`; install Poppler using your operating system's package manager.

From this directory, run:

```bash
python3 build_review_data.py
python3 build_standalone_app.py
```

The first command validates and writes `questions_db.json`; the second embeds that database plus `standalone_app.js` and `standalone_mobile.css` in `index.html`. Extraction fails if the 160 questions, four choices per question, or highlighted answers cannot be matched. The source PDF is kept in this project so the generated data can be rebuilt.
