# Create the Google Forms quizzes

1. Open [Google Apps Script](https://script.google.com/) and create a **New project**.
2. Replace the contents of `Code.gs` with the entire contents of `google_forms_mcq.gs` from this folder. The questions are already embedded; no uploads, spreadsheet, GitHub connection, or PDF access is needed.
3. Save, select **createMcqForms** in the function dropdown, and click **Run**. Approve Google's permission request for Forms and the continuation triggers.
4. The execution log prints edit links for three draft quizzes: Metabolic Biochemistry (160 questions), Clinical Biochemistry (40), and Clinical Biology (50).
5. The script adds up to 40 questions per run, then schedules another batch at least one minute later. Check **Executions** for background progress, or run **showMcqFormLinks** to print the latest counts and links.
6. Once counts reach 160/160, 40/40, and 50/50, open the edit links. Check **Settings → Quizzes**, choose when grades are released, and enable correct answers/feedback for respondents as desired. Publish each form and copy its respondent link when ready.

Each item is a required, single-answer MCQ worth one point. Choices retain their A–D labels. Both correct and incorrect responses have feedback in the format `Correct answer: B. Stop blood loss after blood vessel injury`. Feedback is shown through Google Forms' quiz results, not underneath unanswered questions. The source PDF and original question number appear beneath the question title. Clinical Biology keeps all 10 earlier questions plus 40 from `MCQ kru Mona.pdf`.

If an execution fails, rerun **createMcqForms**; it resumes the saved import and reuses the forms. Running it after completion prints the same form links. Do not manually edit questions during the import. **pauseMcqImport** removes scheduled continuation triggers; run it after a current batch finishes. Use a new Apps Script project if you want a fresh set of forms or an updated question database.

Clinical Biochemistry question 5 retains the PDF-highlighted answer B, as requested, even though it conflicts with the question wording. Review that item before sharing the quiz.

The script was checked locally against all 250 answer keys and tested with simulated Google services, including retries and reruns. Creating real forms requires running it in your Google account.

To regenerate the export after updating the website data:

```text
python build_google_forms.py
node test_google_forms.cjs
```

API references: [Google Forms service](https://developers.google.com/apps-script/reference/forms/form-app), [quiz choices and feedback](https://developers.google.com/apps-script/reference/forms/multiple-choice-item), [Apps Script execution limits](https://developers.google.com/apps-script/guides/services/quotas).
