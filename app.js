// app.js - Master Interactive Virology QCM Exam Engine

(function () {
  "use strict";

  // Data check
  const allQuestions = window.QUESTIONS_DATA || [];
  if (!allQuestions || allQuestions.length === 0) {
    console.error("No questions data found in window.QUESTIONS_DATA.");
    return;
  }

  // State
  const state = {
    mode: "study", // 'study' | 'exam' | 'search'
    selectedLecture: "all",
    studyIndex: 0,
    activeStudyList: [...allQuestions],
    studyAnswers: {}, // { [global_id]: 'A' }
    starredIds: new Set(JSON.parse(localStorage.getItem("virology_starred") || "[]")),

    // Exam state
    examConfig: {
      lecture: "all",
      count: 50,
      timePerQ: 60, // seconds
      timed: true
    },
    examQuestions: [],
    examIndex: 0,
    examAnswers: {}, // { [global_id]: 'A' }
    examMarkedReview: new Set(),
    examTimer: null,
    examSecondsLeft: 0,
    examTotalSeconds: 0,
    examSubmitted: false,

    // Search state
    searchQuery: "",
    searchFilterStarOnly: false,
    searchFilterMissedOnly: false
  };

  // DOM Elements
  const el = {
    themeBtn: document.getElementById("themeBtn"),
    tabStudy: document.getElementById("tabStudy"),
    tabExam: document.getElementById("tabExam"),
    tabSearch: document.getElementById("tabSearch"),

    viewStudy: document.getElementById("viewStudy"),
    viewExam: document.getElementById("viewExam"),
    viewSearch: document.getElementById("viewSearch"),

    // Controls
    lectureSelect: document.getElementById("lectureSelect"),
    searchInput: document.getElementById("searchInput"),
    totalCountBadge: document.getElementById("totalCountBadge"),
    correctCountBadge: document.getElementById("correctCountBadge"),

    // Study UI
    studyCard: document.getElementById("studyCard"),
    qLectureTitle: document.getElementById("qLectureTitle"),
    qNumber: document.getElementById("qNumber"),
    qText: document.getElementById("qText"),
    btnStar: document.getElementById("btnStar"),
    optionsList: document.getElementById("optionsList"),
    explanationBox: document.getElementById("explanationBox"),
    explanationText: document.getElementById("explanationText"),
    takeawayText: document.getElementById("takeawayText"),
    btnPrev: document.getElementById("btnPrev"),
    btnNext: document.getElementById("btnNext"),
    studyGrid: document.getElementById("studyGrid"),

    // Exam UI
    examSetupView: document.getElementById("examSetupView"),
    examActiveView: document.getElementById("examActiveView"),
    examResultView: document.getElementById("examResultView"),

    examLectureSelect: document.getElementById("examLectureSelect"),
    examCountSelect: document.getElementById("examCountSelect"),
    examTimerSelect: document.getElementById("examTimerSelect"),
    btnStartExam: document.getElementById("btnStartExam"),

    examTimerDisplay: document.getElementById("examTimerDisplay"),
    examCurrentMeta: document.getElementById("examCurrentMeta"),
    examQText: document.getElementById("examQText"),
    examOptionsList: document.getElementById("examOptionsList"),
    btnExamMark: document.getElementById("btnExamMark"),
    btnExamPrev: document.getElementById("btnExamPrev"),
    btnExamNext: document.getElementById("btnExamNext"),
    btnExamSubmit: document.getElementById("btnExamSubmit"),
    examGrid: document.getElementById("examGrid"),

    // Exam Results
    resultScorePercent: document.getElementById("resultScorePercent"),
    resultScoreFraction: document.getElementById("resultScoreFraction"),
    resultGradeBadge: document.getElementById("resultGradeBadge"),
    resultBreakdownTbody: document.getElementById("resultBreakdownTbody"),
    btnRetestMissed: document.getElementById("btnRetestMissed"),
    btnNewExam: document.getElementById("btnNewExam"),

    // Search UI
    searchResultsContainer: document.getElementById("searchResultsContainer"),
    starOnlyCheckbox: document.getElementById("starOnlyCheckbox"),
    missedOnlyCheckbox: document.getElementById("missedOnlyCheckbox"),

    // Submit Modal
    confirmModal: document.getElementById("confirmModal"),
    modalUnansweredCount: document.getElementById("modalUnansweredCount"),
    btnModalCancel: document.getElementById("btnModalCancel"),
    btnModalConfirm: document.getElementById("btnModalConfirm")
  };

  // Init
  function init() {
    initTheme();
    populateLectureSelects();
    setupEventListeners();
    updateStudyList();
    renderCurrentStudyQuestion();
    updateGlobalStats();
  }

  // Theme Handling
  function initTheme() {
    const savedTheme = localStorage.getItem("virology_theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);
    updateThemeIcon(savedTheme);
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-theme") || "light";
    const newTheme = currentTheme === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("virology_theme", newTheme);
    updateThemeIcon(newTheme);
  }

  function updateThemeIcon(theme) {
    if (el.themeBtn) {
      el.themeBtn.innerHTML = theme === "dark" ? "☀️" : "🌙";
    }
  }

  // Lecture Selects Population
  function populateLectureSelects() {
    const lectureMap = new Map();
    allQuestions.forEach((q) => {
      if (!lectureMap.has(q.lecture_id)) {
        lectureMap.set(q.lecture_id, { name: q.lecture_name, count: 0 });
      }
      lectureMap.get(q.lecture_id).count++;
    });

    const optionsHtml = ['<option value="all">All 11 Lectures (241 Questions)</option>'];
    lectureMap.forEach((val, id) => {
      optionsHtml.push(`<option value="${id}">L${id}: ${val.name} (${val.count} Qs)</option>`);
    });

    if (el.lectureSelect) el.lectureSelect.innerHTML = optionsHtml.join("");
    if (el.examLectureSelect) el.examLectureSelect.innerHTML = optionsHtml.join("");
  }

  // Switch App Mode
  function setMode(newMode) {
    state.mode = newMode;
    [el.tabStudy, el.tabExam, el.tabSearch].forEach((t) => t && t.classList.remove("active"));
    [el.viewStudy, el.viewExam, el.viewSearch].forEach((v) => v && v.classList.add("hidden"));

    if (newMode === "study") {
      if (el.tabStudy) el.tabStudy.classList.add("active");
      if (el.viewStudy) el.viewStudy.classList.remove("hidden");
      renderCurrentStudyQuestion();
    } else if (newMode === "exam") {
      if (el.tabExam) el.tabExam.classList.add("active");
      if (el.viewExam) el.viewExam.classList.remove("hidden");
    } else if (newMode === "search") {
      if (el.tabSearch) el.tabSearch.classList.add("active");
      if (el.viewSearch) el.viewSearch.classList.remove("hidden");
      renderSearchResults();
    }
  }

  // Study Mode Functions
  function updateStudyList() {
    const selected = el.lectureSelect ? el.lectureSelect.value : "all";
    state.selectedLecture = selected;

    if (selected === "all") {
      state.activeStudyList = [...allQuestions];
    } else {
      const lecId = parseInt(selected, 10);
      state.activeStudyList = allQuestions.filter((q) => q.lecture_id === lecId);
    }

    state.studyIndex = 0;
    renderStudyGrid();
    renderCurrentStudyQuestion();
    updateGlobalStats();
  }

  function renderCurrentStudyQuestion() {
    if (!state.activeStudyList || state.activeStudyList.length === 0) return;
    const q = state.activeStudyList[state.studyIndex];
    if (!q) return;

    // Header metadata
    if (el.qLectureTitle) el.qLectureTitle.textContent = `Lecture ${q.lecture_id}: ${q.lecture_name}`;
    if (el.qNumber) el.qNumber.textContent = `Question ${state.studyIndex + 1} of ${state.activeStudyList.length} (Q${q.question_id})`;
    if (el.qText) el.qText.textContent = q.question;

    // Star icon state
    if (el.btnStar) {
      const isStarred = state.starredIds.has(q.global_id);
      el.btnStar.classList.toggle("starred", isStarred);
      el.btnStar.innerHTML = isStarred ? "★" : "☆";
    }

    // Previous / Next buttons
    if (el.btnPrev) el.btnPrev.disabled = state.studyIndex === 0;
    if (el.btnNext) el.btnNext.disabled = state.studyIndex === state.activeStudyList.length - 1;

    // Render options
    const chosenAnswer = state.studyAnswers[q.global_id];
    const isAnswered = chosenAnswer !== undefined;

    let optionsHtml = "";
    ["A", "B", "C", "D", "E"].forEach((letter) => {
      if (q.options[letter]) {
        let optClass = "option-btn";
        if (isAnswered) {
          if (letter === q.correct_answer) {
            optClass += " correct";
          } else if (letter === chosenAnswer) {
            optClass += " wrong";
          }
        }
        optionsHtml += `
          <button type="button" class="${optClass}" data-letter="${letter}">
            <span class="opt-letter">${letter}</span>
            <span class="opt-text">${q.options[letter]}</span>
          </button>
        `;
      }
    });

    if (el.optionsList) {
      el.optionsList.innerHTML = optionsHtml;
      // Attach click handlers
      el.optionsList.querySelectorAll(".option-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
          const letter = btn.getAttribute("data-letter");
          handleStudyAnswer(q.global_id, letter);
        });
      });
    }

    // Explanation Box
    if (el.explanationBox) {
      if (isAnswered) {
        el.explanationBox.classList.remove("hidden");
        if (el.explanationText) {
          const isCorrect = chosenAnswer === q.correct_answer;
          el.explanationText.innerHTML = `
            <div style="margin-bottom:0.5rem; font-weight:700; color:${isCorrect ? "var(--success)" : "var(--danger)"}">
              ${isCorrect ? "✓ Correct!" : "✗ Incorrect!"} Correct Answer: ${q.correct_answer}) ${q.correct_text}
            </div>
            <div>${q.explanation}</div>
          `;
        }
        if (el.takeawayText) el.takeawayText.textContent = q.takeaway;
      } else {
        el.explanationBox.classList.add("hidden");
      }
    }

    // Update grid active state
    renderStudyGrid();
  }

  function handleStudyAnswer(globalId, letter) {
    state.studyAnswers[globalId] = letter;
    renderCurrentStudyQuestion();
    updateGlobalStats();
  }

  function renderStudyGrid() {
    if (!el.studyGrid) return;
    let html = "";
    state.activeStudyList.forEach((q, idx) => {
      let btnClass = "grid-btn";
      if (idx === state.studyIndex) btnClass += " current";

      const ans = state.studyAnswers[q.global_id];
      if (ans !== undefined) {
        btnClass += ans === q.correct_answer ? " answered-correct" : " answered-wrong";
      }

      html += `<button type="button" class="${btnClass}" data-index="${idx}">${idx + 1}</button>`;
    });

    el.studyGrid.innerHTML = html;
    el.studyGrid.querySelectorAll(".grid-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const targetIdx = parseInt(btn.getAttribute("data-index"), 10);
        state.studyIndex = targetIdx;
        renderCurrentStudyQuestion();
      });
    });
  }

  function toggleStarQuestion(globalId) {
    if (state.starredIds.has(globalId)) {
      state.starredIds.delete(globalId);
    } else {
      state.starredIds.add(globalId);
    }
    localStorage.setItem("virology_starred", JSON.stringify(Array.from(state.starredIds)));
    renderCurrentStudyQuestion();
    if (state.mode === "search") renderSearchResults();
  }

  function updateGlobalStats() {
    const answeredCount = Object.keys(state.studyAnswers).length;
    let correctCount = 0;
    Object.entries(state.studyAnswers).forEach(([gid, ans]) => {
      const qObj = allQuestions.find((item) => item.global_id === parseInt(gid, 10));
      if (qObj && qObj.correct_answer === ans) {
        correctCount++;
      }
    });

    if (el.totalCountBadge) {
      el.totalCountBadge.textContent = `${answeredCount} / ${allQuestions.length} Answered`;
    }
    if (el.correctCountBadge) {
      const pct = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
      el.correctCountBadge.textContent = `${correctCount} Correct (${pct}%)`;
    }
  }

  // Exam Mode Functions
  function startExam() {
    const lecVal = el.examLectureSelect.value;
    let pool = [...allQuestions];
    if (lecVal !== "all") {
      const lid = parseInt(lecVal, 10);
      pool = allQuestions.filter((q) => q.lecture_id === lid);
    }

    // Shuffle pool
    pool.sort(() => Math.random() - 0.5);

    // Question count
    const countVal = el.examCountSelect.value;
    const requestedCount = countVal === "all" ? pool.length : parseInt(countVal, 10);
    const finalCount = Math.min(requestedCount, pool.length);

    state.examQuestions = pool.slice(0, finalCount);
    state.examIndex = 0;
    state.examAnswers = {};
    state.examMarkedReview.clear();
    state.examSubmitted = false;

    // Timer setup
    const timerChoice = el.examTimerSelect.value;
    if (timerChoice === "none") {
      state.examConfig.timed = false;
      state.examSecondsLeft = 0;
    } else {
      state.examConfig.timed = true;
      const totalSec = parseInt(timerChoice, 10) * 60;
      state.examSecondsLeft = totalSec;
      state.examTotalSeconds = totalSec;
      startExamTimer();
    }

    // View switch
    el.examSetupView.classList.add("hidden");
    el.examResultView.classList.add("hidden");
    el.examActiveView.classList.remove("hidden");

    renderExamQuestion();
    renderExamGrid();
  }

  function startExamTimer() {
    clearInterval(state.examTimer);
    updateTimerDisplay();
    state.examTimer = setInterval(() => {
      state.examSecondsLeft--;
      updateTimerDisplay();
      if (state.examSecondsLeft <= 0) {
        clearInterval(state.examTimer);
        submitExam(true); // auto submit
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    if (!el.examTimerDisplay) return;
    if (!state.examConfig.timed) {
      el.examTimerDisplay.textContent = "⏱️ Untimed Mode";
      return;
    }
    const mins = Math.floor(state.examSecondsLeft / 60);
    const secs = state.examSecondsLeft % 60;
    const pad = (n) => String(n).padStart(2, "0");
    el.examTimerDisplay.textContent = `⏱️ ${pad(mins)}:${pad(secs)}`;

    if (state.examSecondsLeft < 300) {
      el.examTimerDisplay.classList.add("warning");
    } else {
      el.examTimerDisplay.classList.remove("warning");
    }
  }

  function renderExamQuestion() {
    const q = state.examQuestions[state.examIndex];
    if (!q) return;

    if (el.examCurrentMeta) {
      el.examCurrentMeta.textContent = `Question ${state.examIndex + 1} of ${state.examQuestions.length} — Lecture ${q.lecture_id}: ${q.lecture_name}`;
    }
    if (el.examQText) el.examQText.textContent = q.question;

    // Mark for review button
    const isMarked = state.examMarkedReview.has(state.examIndex);
    if (el.btnExamMark) {
      el.btnExamMark.classList.toggle("marked", isMarked);
      el.btnExamMark.textContent = isMarked ? "★ Marked for Review" : "☆ Mark for Review";
    }

    // Prev / Next buttons
    if (el.btnExamPrev) el.btnExamPrev.disabled = state.examIndex === 0;
    if (el.btnExamNext) el.btnExamNext.disabled = state.examIndex === state.examQuestions.length - 1;

    // Options
    const chosen = state.examAnswers[state.examIndex];
    let html = "";
    ["A", "B", "C", "D", "E"].forEach((letter) => {
      if (q.options[letter]) {
        const isSelected = chosen === letter;
        html += `
          <button type="button" class="option-btn ${isSelected ? "selected" : ""}" data-letter="${letter}">
            <span class="opt-letter">${letter}</span>
            <span class="opt-text">${q.options[letter]}</span>
          </button>
        `;
      }
    });

    if (el.examOptionsList) {
      el.examOptionsList.innerHTML = html;
      el.examOptionsList.querySelectorAll(".option-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
          const letter = btn.getAttribute("data-letter");
          state.examAnswers[state.examIndex] = letter;
          renderExamQuestion();
          renderExamGrid();
        });
      });
    }

    renderExamGrid();
  }

  function renderExamGrid() {
    if (!el.examGrid) return;
    let html = "";
    state.examQuestions.forEach((_, idx) => {
      let btnClass = "grid-btn";
      if (idx === state.examIndex) btnClass += " current";

      if (state.examMarkedReview.has(idx)) {
        btnClass += " marked-review";
      } else if (state.examAnswers[idx] !== undefined) {
        btnClass += " answered-correct";
      }

      html += `<button type="button" class="${btnClass}" data-index="${idx}">${idx + 1}</button>`;
    });

    el.examGrid.innerHTML = html;
    el.examGrid.querySelectorAll(".grid-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        state.examIndex = parseInt(btn.getAttribute("data-index"), 10);
        renderExamQuestion();
      });
    });
  }

  function promptSubmitExam() {
    const total = state.examQuestions.length;
    const answered = Object.keys(state.examAnswers).length;
    const unanswered = total - answered;

    if (el.modalUnansweredCount) {
      el.modalUnansweredCount.textContent = unanswered;
    }
    if (el.confirmModal) el.confirmModal.classList.remove("hidden");
  }

  function submitExam(forced = false) {
    clearInterval(state.examTimer);
    state.examSubmitted = true;
    if (el.confirmModal) el.confirmModal.classList.add("hidden");
    el.examActiveView.classList.add("hidden");
    el.examResultView.classList.remove("hidden");

    calculateAndRenderResults();
  }

  function calculateAndRenderResults() {
    let correct = 0;
    const total = state.examQuestions.length;
    const lectureStats = {};

    state.examQuestions.forEach((q, idx) => {
      const userAns = state.examAnswers[idx];
      const isCorrect = userAns === q.correct_answer;
      if (isCorrect) correct++;

      const lid = q.lecture_id;
      if (!lectureStats[lid]) {
        lectureStats[lid] = { name: q.lecture_name, total: 0, correct: 0 };
      }
      lectureStats[lid].total++;
      if (isCorrect) lectureStats[lid].correct++;
    });

    const percent = Math.round((correct / total) * 100);
    if (el.resultScorePercent) el.resultScorePercent.textContent = `${percent}%`;
    if (el.resultScoreFraction) el.resultScoreFraction.textContent = `${correct} / ${total} Correct`;

    // Grade badge
    let grade = "A";
    let badgeClass = "badge-success";
    if (percent >= 90) { grade = "Outstanding (A)"; badgeClass = "badge-success"; }
    else if (percent >= 80) { grade = "Very Good (B)"; badgeClass = "badge-success"; }
    else if (percent >= 70) { grade = "Good (C)"; badgeClass = "badge-primary"; }
    else if (percent >= 60) { grade = "Pass (D)"; badgeClass = "badge-warning"; }
    else { grade = "Needs Review (F)"; badgeClass = "badge-danger"; }

    if (el.resultGradeBadge) {
      el.resultGradeBadge.className = `badge ${badgeClass}`;
      el.resultGradeBadge.textContent = grade;
    }

    // Lecture breakdown table
    let tbodyHtml = "";
    Object.keys(lectureStats).sort((a, b) => a - b).forEach((lid) => {
      const stat = lectureStats[lid];
      const lecPct = Math.round((stat.correct / stat.total) * 100);
      tbodyHtml += `
        <tr>
          <td><strong>Lecture ${lid}: ${stat.name}</strong></td>
          <td>${stat.correct} / ${stat.total}</td>
          <td><strong>${lecPct}%</strong></td>
        </tr>
      `;
    });
    if (el.resultBreakdownTbody) el.resultBreakdownTbody.innerHTML = tbodyHtml;
  }

  function retestMissed() {
    const missed = [];
    state.examQuestions.forEach((q, idx) => {
      if (state.examAnswers[idx] !== q.correct_answer) {
        missed.push(q);
      }
    });

    if (missed.length === 0) {
      alert("Congratulations! You scored 100% and have no missed questions to retest.");
      return;
    }

    state.examQuestions = missed;
    state.examIndex = 0;
    state.examAnswers = {};
    state.examMarkedReview.clear();
    state.examSubmitted = false;

    el.examResultView.classList.add("hidden");
    el.examActiveView.classList.remove("hidden");

    if (state.examConfig.timed) {
      state.examSecondsLeft = missed.length * 60;
      startExamTimer();
    }

    renderExamQuestion();
    renderExamGrid();
  }

  // Search & Bank Review
  function renderSearchResults() {
    if (!el.searchResultsContainer) return;
    const query = (el.searchInput ? el.searchInput.value : "").trim().toLowerCase();
    const starOnly = el.starOnlyCheckbox ? el.starOnlyCheckbox.checked : false;
    const missedOnly = el.missedOnlyCheckbox ? el.missedOnlyCheckbox.checked : false;

    let list = allQuestions.filter((q) => {
      if (starOnly && !state.starredIds.has(q.global_id)) return false;
      if (missedOnly) {
        const userAns = state.studyAnswers[q.global_id];
        if (userAns === undefined || userAns === q.correct_answer) return false;
      }
      if (!query) return true;
      const haystack = (
        q.question +
        " " +
        Object.values(q.options).join(" ") +
        " " +
        q.explanation +
        " " +
        q.takeaway +
        " " +
        q.lecture_name
      ).toLowerCase();
      return haystack.includes(query);
    });

    if (list.length === 0) {
      el.searchResultsContainer.innerHTML = `
        <div style="text-align:center; padding:3rem; color:var(--text-muted);">
          <h3>No matching questions found</h3>
          <p>Try searching different keywords or unchecking filters.</p>
        </div>
      `;
      return;
    }

    let html = `
      <div style="margin-bottom:1rem; font-weight:600; color:var(--text-muted);">
        Found ${list.length} Question${list.length > 1 ? "s" : ""}
      </div>
    `;

    list.forEach((q) => {
      const isStarred = state.starredIds.has(q.global_id);
      const chosen = state.studyAnswers[q.global_id];
      html += `
        <div class="question-card" style="margin-bottom:1.5rem;">
          <div class="q-header">
            <div class="q-meta">
              <span class="q-lecture-title">Lecture ${q.lecture_id}: ${q.lecture_name}</span>
              <span class="q-number">Question #${q.global_id} (Q${q.question_id})</span>
            </div>
            <button type="button" class="btn-star ${isStarred ? "starred" : ""}" data-star-id="${q.global_id}">
              ${isStarred ? "★" : "☆"}
            </button>
          </div>
          <div class="q-text">${q.question}</div>
          <div class="options-list">
            ${["A", "B", "C", "D", "E"]
              .map((letter) => {
                if (!q.options[letter]) return "";
                const isCorrect = letter === q.correct_answer;
                const isChosen = chosen === letter;
                let cls = "option-btn";
                if (isCorrect) cls += " correct";
                else if (isChosen) cls += " wrong";
                return `
                <div class="${cls}">
                  <span class="opt-letter">${letter}</span>
                  <span class="opt-text">${q.options[letter]}</span>
                </div>
              `;
              })
              .join("")}
          </div>
          <div class="explanation-box">
            <div class="explanation-title">✓ Verified Answer: ${q.correct_answer}) ${q.correct_text}</div>
            <div style="margin-top:0.4rem;">${q.explanation}</div>
            <div class="takeaway-card">
              <span class="takeaway-badge">Takeaway</span>
              <span>${q.takeaway}</span>
            </div>
          </div>
        </div>
      `;
    });

    el.searchResultsContainer.innerHTML = html;

    // Attach star handlers
    el.searchResultsContainer.querySelectorAll("[data-star-id]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const gid = parseInt(btn.getAttribute("data-star-id"), 10);
        toggleStarQuestion(gid);
      });
    });
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Theme
    if (el.themeBtn) el.themeBtn.addEventListener("click", toggleTheme);

    // Nav Tabs
    if (el.tabStudy) el.tabStudy.addEventListener("click", () => setMode("study"));
    if (el.tabExam) el.tabExam.addEventListener("click", () => setMode("exam"));
    if (el.tabSearch) el.tabSearch.addEventListener("click", () => setMode("search"));

    // Study Controls
    if (el.lectureSelect) el.lectureSelect.addEventListener("change", updateStudyList);
    if (el.btnPrev) {
      el.btnPrev.addEventListener("click", () => {
        if (state.studyIndex > 0) {
          state.studyIndex--;
          renderCurrentStudyQuestion();
        }
      });
    }
    if (el.btnNext) {
      el.btnNext.addEventListener("click", () => {
        if (state.studyIndex < state.activeStudyList.length - 1) {
          state.studyIndex++;
          renderCurrentStudyQuestion();
        }
      });
    }
    if (el.btnStar) {
      el.btnStar.addEventListener("click", () => {
        const q = state.activeStudyList[state.studyIndex];
        if (q) toggleStarQuestion(q.global_id);
      });
    }

    // Exam Controls
    if (el.btnStartExam) el.btnStartExam.addEventListener("click", startExam);
    if (el.btnExamPrev) {
      el.btnExamPrev.addEventListener("click", () => {
        if (state.examIndex > 0) {
          state.examIndex--;
          renderExamQuestion();
        }
      });
    }
    if (el.btnExamNext) {
      el.btnExamNext.addEventListener("click", () => {
        if (state.examIndex < state.examQuestions.length - 1) {
          state.examIndex++;
          renderExamQuestion();
        }
      });
    }
    if (el.btnExamMark) {
      el.btnExamMark.addEventListener("click", () => {
        if (state.examMarkedReview.has(state.examIndex)) {
          state.examMarkedReview.delete(state.examIndex);
        } else {
          state.examMarkedReview.add(state.examIndex);
        }
        renderExamQuestion();
        renderExamGrid();
      });
    }
    if (el.btnExamSubmit) el.btnExamSubmit.addEventListener("click", promptSubmitExam);
    if (el.btnModalCancel) el.btnModalCancel.addEventListener("click", () => el.confirmModal.classList.add("hidden"));
    if (el.btnModalConfirm) el.btnModalConfirm.addEventListener("click", () => submitExam(false));

    if (el.btnRetestMissed) el.btnRetestMissed.addEventListener("click", retestMissed);
    if (el.btnNewExam) {
      el.btnNewExam.addEventListener("click", () => {
        el.examResultView.classList.add("hidden");
        el.examSetupView.classList.remove("hidden");
      });
    }

    // Search Controls
    if (el.searchInput) {
      el.searchInput.addEventListener("input", () => {
        if (state.mode !== "search") setMode("search");
        renderSearchResults();
      });
    }
    if (el.starOnlyCheckbox) el.starOnlyCheckbox.addEventListener("change", renderSearchResults);
    if (el.missedOnlyCheckbox) el.missedOnlyCheckbox.addEventListener("change", renderSearchResults);

    // Global Keyboard Navigation
    window.addEventListener("keydown", (e) => {
      // Ignore if typing in input
      if (document.activeElement && document.activeElement.tagName === "INPUT") return;

      if (state.mode === "study") {
        if (e.key === "ArrowLeft") {
          if (state.studyIndex > 0) {
            state.studyIndex--;
            renderCurrentStudyQuestion();
          }
        } else if (e.key === "ArrowRight") {
          if (state.studyIndex < state.activeStudyList.length - 1) {
            state.studyIndex++;
            renderCurrentStudyQuestion();
          }
        } else if (["a", "b", "c", "d", "A", "B", "C", "D"].includes(e.key)) {
          const letter = e.key.toUpperCase();
          const q = state.activeStudyList[state.studyIndex];
          if (q && q.options[letter]) {
            handleStudyAnswer(q.global_id, letter);
          }
        } else if (e.key.toLowerCase() === "s") {
          const q = state.activeStudyList[state.studyIndex];
          if (q) toggleStarQuestion(q.global_id);
        }
      } else if (state.mode === "exam" && !state.examSubmitted && !el.examActiveView.classList.contains("hidden")) {
        if (e.key === "ArrowLeft") {
          if (state.examIndex > 0) {
            state.examIndex--;
            renderExamQuestion();
          }
        } else if (e.key === "ArrowRight") {
          if (state.examIndex < state.examQuestions.length - 1) {
            state.examIndex++;
            renderExamQuestion();
          }
        } else if (["a", "b", "c", "d", "A", "B", "C", "D"].includes(e.key)) {
          const letter = e.key.toUpperCase();
          const q = state.examQuestions[state.examIndex];
          if (q && q.options[letter]) {
            state.examAnswers[state.examIndex] = letter;
            renderExamQuestion();
          }
        }
      }
    });
  }

  // Start app
  document.addEventListener("DOMContentLoaded", init);
})();
