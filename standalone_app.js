(function () {
  "use strict";

  const rawDB = window.RAW_QUESTIONS || [];
  if (!rawDB.length) return;
  const byId = new Map(rawDB.map(q => [q.global_id, q]));
  const SESSION_KEY = "metabolic_biochem_session_v1";
  const STAR_KEY = "metabolic_biochem_stars";
  const THEME_KEY = "metabolic_theme_mode";
  const el = Object.fromEntries([
    "btnThemeToggle", "btnStarOnly", "btnOpenNavigator", "btnOpenSettings",
    "settingsDialog", "navigatorDialog", "staleDialog", "btnReloadSession",
    "studyNotice", "lectureFilter", "countFilter", "checkShuffleQuestions",
    "checkShuffleAnswers", "checkStarOnly", "btnShuffleAll", "btnResetProgress",
    "progressPill", "progressPillMobile", "accuracyPill", "headerProgress",
    "progressFill", "badgeLecture", "badgeOrigQ", "badgePosition", "btnStarQ",
    "qTitle", "optionsContainer", "explBox", "explAnswerLabel", "btnPrev",
    "btnNext", "btnPrevMobile", "btnNextMobile", "btnNavigatorMobile",
    "mobilePosition", "paletteGrid", "sheetPaletteGrid", "navigatorFilters",
    "navigatorCount", "navigatorEmpty", "palAnsweredCounter", "palDrawerCounter",
    "touchArea", "confirmModal", "modalIcon", "modalTitle", "modalDesc",
    "btnModalCancel", "btnModalConfirm", "controlsSummaryText"
  ].map(id => [id, document.getElementById(id)]));

  const state = {
    sessionQuestions: [], viewQuestions: [], currentId: null, answers: {},
    starred: new Set(), lecture: "all", count: "all", shuffleQ: true,
    shuffleA: true, starOnly: false, navFilter: "all", stale: false,
    canSave: true, lastSwipeAt: 0
  };

  function readStorage(key) {
    try { return localStorage.getItem(key); }
    catch (_) { state.canSave = false; return null; }
  }
  function writeStorage(key, value) {
    try { localStorage.setItem(key, value); return true; }
    catch (_) {
      state.canSave = false;
      notice("Progress cannot be saved in this browser. Keep this tab open until you finish.");
      return false;
    }
  }
  function notice(message) {
    el.studyNotice.textContent = message;
    el.studyNotice.classList.remove("hidden");
  }
  function randomize(items) {
    const result = [...items];
    for (let i = result.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }
  function optionLetters(raw) {
    return ["A", "B", "C", "D", "E"].filter(letter =>
      Object.prototype.hasOwnProperty.call(raw.options, letter));
  }
  function makeQuestion(raw, letters) {
    return {
      id: raw.global_id, raw,
      options: letters.map((letter, index) => ({
        origLetter: letter, displayLetter: "ABCDE"[index],
        text: raw.options[letter], isCorrect: letter === raw.correct_answer
      }))
    };
  }
  function snapshot() {
    return {
      version: 1, dataset: window.DATASET_HASH,
      questionIds: state.sessionQuestions.map(q => q.id),
      optionOrder: Object.fromEntries(state.sessionQuestions.map(q =>
        [q.id, q.options.map(option => option.origLetter)])),
      answers: state.answers, currentId: state.currentId,
      lecture: state.lecture, count: state.count,
      shuffleQ: state.shuffleQ, shuffleA: state.shuffleA,
      starOnly: state.starOnly
    };
  }
  function save() {
    if (state.stale || !state.sessionQuestions.length) return;
    writeStorage(SESSION_KEY, JSON.stringify(snapshot()));
  }
  function restore() {
    const text = readStorage(SESSION_KEY);
    if (!text) return false;
    try {
      const saved = JSON.parse(text);
      if (saved.version !== 1 || saved.dataset !== window.DATASET_HASH ||
          !Array.isArray(saved.questionIds) || !saved.questionIds.length ||
          new Set(saved.questionIds).size !== saved.questionIds.length ||
          !saved.optionOrder || !saved.answers ||
          !["all", "10", "20", "50", "100"].includes(saved.count) ||
          !["all", ...new Set(rawDB.map(q => String(q.lecture_id)))].includes(saved.lecture) ||
          typeof saved.shuffleQ !== "boolean" || typeof saved.shuffleA !== "boolean" ||
          typeof saved.starOnly !== "boolean") throw new Error("invalid session");
      const questions = saved.questionIds.map(id => {
        const raw = byId.get(id), letters = saved.optionOrder[id];
        if (!raw || !Array.isArray(letters) ||
            letters.length !== optionLetters(raw).length ||
            new Set(letters).size !== letters.length ||
            letters.some(letter => !optionLetters(raw).includes(letter))) throw new Error("invalid question");
        return makeQuestion(raw, letters);
      });
      const ids = new Set(saved.questionIds.map(String));
      for (const [id, letter] of Object.entries(saved.answers)) {
        if (!ids.has(id) || !saved.optionOrder[id].includes(letter)) throw new Error("invalid answer");
      }
      if (saved.currentId !== null && !ids.has(String(saved.currentId))) throw new Error("invalid position");
      state.sessionQuestions = questions;
      state.answers = saved.answers;
      state.currentId = saved.currentId;
      state.lecture = saved.lecture;
      state.count = saved.count;
      state.shuffleQ = saved.shuffleQ;
      state.shuffleA = saved.shuffleA;
      state.starOnly = saved.starOnly;
      return true;
    } catch (_) {
      try { localStorage.removeItem(SESSION_KEY); } catch (_) { state.canSave = false; }
      notice("Saved progress could not be restored. A new study session has started.");
      return false;
    }
  }
  function newSession() {
    let list = rawDB.filter(q => state.lecture === "all" || String(q.lecture_id) === state.lecture);
    if (state.shuffleQ) list = randomize(list);
    if (state.count !== "all") list = list.slice(0, Number(state.count));
    state.sessionQuestions = list.map(raw => makeQuestion(raw,
      state.shuffleA ? randomize(optionLetters(raw)) : optionLetters(raw)));
    state.answers = {};
    state.starOnly = false;
    state.currentId = state.sessionQuestions[0]?.id ?? null;
    setView();
  }
  function syncSettings() {
    el.lectureFilter.value = state.lecture;
    el.countFilter.value = state.count;
    el.checkShuffleQuestions.checked = state.shuffleQ;
    el.checkShuffleAnswers.checked = state.shuffleA;
    el.checkStarOnly.checked = state.starOnly;
    el.btnStarOnly.setAttribute("aria-pressed", String(state.starOnly));
    el.btnStarOnly.textContent = state.starOnly ? "★" : "☆";
  }
  function setView(persist = true) {
    state.viewQuestions = state.starOnly
      ? state.sessionQuestions.filter(q => state.starred.has(q.id))
      : state.sessionQuestions;
    if (!state.viewQuestions.some(q => q.id === state.currentId))
      state.currentId = state.viewQuestions[0]?.id ?? null;
    syncSettings();
    renderAll();
    if (persist) save();
  }
  function currentQuestion() {
    return state.viewQuestions.find(q => q.id === state.currentId) || null;
  }
  function answeredCount() {
    return state.sessionQuestions.filter(q => state.answers[q.id] !== undefined).length;
  }
  function renderQuestion() {
    const q = currentQuestion();
    const index = state.viewQuestions.findIndex(item => item.id === state.currentId);
    const position = `${index + 1}/${state.viewQuestions.length}`;
    el.mobilePosition.textContent = position;
    el.btnPrev.disabled = el.btnPrevMobile.disabled = index <= 0;
    el.btnNext.disabled = el.btnNextMobile.disabled = index < 0 || index >= state.viewQuestions.length - 1;
    el.btnStarQ.disabled = !q;
    if (!q) {
      el.badgeLecture.textContent = "Starred questions";
      el.badgeOrigQ.textContent = "";
      el.badgePosition.textContent = "0 questions";
      el.qTitle.textContent = "No starred questions in this session. Star a question or turn off Starred mode.";
      el.optionsContainer.replaceChildren();
      el.explBox.classList.add("hidden");
      return;
    }
    el.badgeLecture.textContent = q.raw.lecture_name;
    el.badgeOrigQ.textContent = `Original Q${q.raw.question_id}`;
    el.badgePosition.textContent = `Question ${index + 1} of ${state.viewQuestions.length}`;
    el.qTitle.textContent = q.raw.question;
    el.btnStarQ.classList.toggle("starred", state.starred.has(q.id));
    el.btnStarQ.textContent = state.starred.has(q.id) ? "★" : "☆";
    el.btnStarQ.setAttribute("aria-label", state.starred.has(q.id) ? "Remove bookmark" : "Bookmark question");
    el.optionsContainer.replaceChildren();
    const answer = state.answers[q.id];
    q.options.forEach((option, optionIndex) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "opt-btn";
      if (answer !== undefined) {
        button.classList.add("locked");
        if (option.isCorrect) button.classList.add("is-correct");
        else if (option.origLetter === answer) button.classList.add("is-wrong");
      }
      const tag = document.createElement("span");
      tag.className = "opt-tag";
      tag.textContent = option.displayLetter;
      const label = document.createElement("span");
      label.className = "opt-text";
      label.textContent = option.text;
      button.append(tag, label);
      button.addEventListener("click", () => {
        if (Date.now() - state.lastSwipeAt > 400) selectAnswer(optionIndex);
      });
      el.optionsContainer.append(button);
    });
    el.explBox.classList.toggle("hidden", answer === undefined);
    if (answer !== undefined) {
      const correct = q.options.find(option => option.isCorrect);
      el.explAnswerLabel.textContent = `${correct.displayLetter}) ${q.raw.correct_text}`;
    }
  }
  function selectAnswer(index) {
    if (state.stale) return;
    const q = currentQuestion();
    if (!q || state.answers[q.id] !== undefined || !q.options[index]) return;
    state.answers[q.id] = q.options[index].origLetter;
    renderAll();
    save();
  }
  function paletteStatus(q) {
    const answer = state.answers[q.id];
    if (answer === undefined) return "unanswered";
    return answer === q.raw.correct_answer ? "correct" : "wrong";
  }
  function renderPalette() {
    const count = answeredCount(), total = state.sessionQuestions.length;
    el.palAnsweredCounter.textContent = `${count} / ${total}`;
    el.palDrawerCounter.textContent = `${count}/${total}`;
    el.navigatorCount.textContent = `${count} / ${total} answered`;
    const visible = state.viewQuestions.filter(q =>
      state.navFilter === "all" ||
      (state.navFilter === "starred" ? state.starred.has(q.id) : paletteStatus(q) === state.navFilter));
    el.navigatorEmpty.classList.toggle("hidden", visible.length > 0);
    for (const [grid, questions] of [[el.paletteGrid, state.viewQuestions], [el.sheetPaletteGrid, visible]]) {
      grid.replaceChildren();
      questions.forEach(q => {
        const index = state.viewQuestions.indexOf(q);
        const button = document.createElement("button");
        button.type = "button";
        button.className = `pal-btn ${paletteStatus(q)}`;
        if (q.id === state.currentId) button.classList.add("current");
        if (state.starred.has(q.id)) button.classList.add("starred");
        button.textContent = String(index + 1);
        button.setAttribute("aria-label", `Question ${index + 1}, ${paletteStatus(q)}${state.starred.has(q.id) ? ", starred" : ""}`);
        button.addEventListener("click", () => {
          if (state.stale) return;
          state.currentId = q.id;
          renderAll();
          save();
          if (el.navigatorDialog.open) closeSheet(el.navigatorDialog);
          scrollQuestionIntoView();
        });
        grid.append(button);
      });
    }
    if (el.navigatorDialog.open)
      el.sheetPaletteGrid.querySelector(".current")?.scrollIntoView({block: "nearest"});
  }
  function renderStats() {
    const count = answeredCount(), total = state.sessionQuestions.length;
    const correct = state.sessionQuestions.filter(q => paletteStatus(q) === "correct").length;
    el.progressPill.textContent = `${count} / ${total} Answered`;
    el.progressPillMobile.textContent = `${count}/${total}`;
    el.accuracyPill.textContent = `${correct} Correct (${count ? Math.round(correct / count * 100) : 0}%)`;
    el.headerProgress.setAttribute("aria-valuemax", String(total));
    el.headerProgress.setAttribute("aria-valuenow", String(count));
    el.progressFill.style.width = `${total ? count / total * 100 : 0}%`;
    el.controlsSummaryText.textContent = `Metabolic Biochemistry • ${total} Qs`;
  }
  function renderAll() { renderQuestion(); renderPalette(); renderStats(); }
  function scrollQuestionIntoView() {
    const header = document.querySelector("header");
    const top = el.touchArea.getBoundingClientRect().top;
    const headerHeight = header?.offsetHeight || 54;
    if (top < headerHeight || top > headerHeight + 120)
      window.scrollTo({top: Math.max(0, window.scrollY + top - headerHeight - 12), behavior: "smooth"});
  }
  function move(delta) {
    if (state.stale) return;
    const index = state.viewQuestions.findIndex(q => q.id === state.currentId);
    const next = state.viewQuestions[index + delta];
    if (!next) return;
    state.currentId = next.id;
    renderAll();
    save();
    scrollQuestionIntoView();
  }
  function toggleStar() {
    if (state.stale) return;
    const q = currentQuestion();
    if (!q) return;
    if (state.starred.has(q.id)) state.starred.delete(q.id);
    else state.starred.add(q.id);
    writeStorage(STAR_KEY, JSON.stringify([...state.starred]));
    setView();
  }
  function toggleStarOnly() {
    if (state.stale) return;
    state.starOnly = !state.starOnly;
    setView();
  }
  function openSheet(dialog) {
    if (state.stale || dialog.open) return;
    if (typeof dialog.showModal === "function") dialog.showModal();
    else dialog.setAttribute("open", "");
    if (dialog === el.navigatorDialog) renderPalette();
    dialog.querySelector(".sheet-close")?.focus();
  }
  function closeSheet(dialog) {
    if (typeof dialog.close === "function") dialog.close();
    else dialog.removeAttribute("open");
  }
  let confirmAction = null;
  function showConfirm({title, desc, button, action, danger = false}) {
    el.modalIcon.textContent = danger ? "⚠" : "↻";
    el.modalTitle.textContent = title;
    el.modalDesc.textContent = desc;
    el.btnModalConfirm.textContent = button;
    el.btnModalConfirm.classList.toggle("danger", danger);
    confirmAction = action;
    if (typeof el.confirmModal.showModal === "function") el.confirmModal.showModal();
    else el.confirmModal.setAttribute("open", "");
    el.btnModalCancel.focus();
  }
  function closeConfirm(confirmed) {
    const action = confirmAction;
    confirmAction = null;
    if (typeof el.confirmModal.close === "function") el.confirmModal.close();
    else el.confirmModal.removeAttribute("open");
    if (confirmed && action) action();
  }
  function requestSetting(key, value, control) {
    if (state.stale || value === state[key]) return;
    control.type === "checkbox" ? control.checked = state[key] : control.value = state[key];
    const apply = () => {
      state[key] = value;
      newSession();
      closeSheet(el.settingsDialog);
    };
    if (answeredCount()) showConfirm({
      title: "Start a new study session?",
      desc: "Changing this setting will replace your saved answers and question order.",
      button: "Start new session", action: apply, danger: true
    });
    else apply();
  }
  function populateLectures() {
    const counts = new Map();
    rawDB.forEach(q => counts.set(q.lecture_id, (counts.get(q.lecture_id) || 0) + 1));
    el.lectureFilter.replaceChildren(new Option(`All ${rawDB.length} Questions`, "all"));
    counts.forEach((count, id) => {
      const q = rawDB.find(item => item.lecture_id === id);
      el.lectureFilter.add(new Option(`${q.lecture_name} (${count} Qs)`, String(id)));
    });
  }
  function initTheme() {
    const theme = readStorage(THEME_KEY) === "dark" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", theme);
    el.btnThemeToggle.textContent = theme === "dark" ? "☀️" : "🌙";
  }
  function setupSwipe() {
    let start = null;
    el.touchArea.addEventListener("touchstart", event => {
      if (event.touches.length !== 1 || event.target.closest("a, select, input, textarea, [contenteditable]")) return;
      start = {x: event.touches[0].clientX, y: event.touches[0].clientY};
    }, {passive: true});
    el.touchArea.addEventListener("touchend", event => {
      if (!start || event.changedTouches.length !== 1 || el.navigatorDialog.open || el.settingsDialog.open) return;
      const dx = event.changedTouches[0].clientX - start.x;
      const dy = event.changedTouches[0].clientY - start.y;
      start = null;
      if (Math.abs(dx) > 45 && Math.abs(dy) < 35) {
        state.lastSwipeAt = Date.now();
        move(dx < 0 ? 1 : -1);
      }
    }, {passive: true});
    el.touchArea.addEventListener("touchcancel", () => { start = null; }, {passive: true});
  }
  function setupEvents() {
    el.btnPrev.addEventListener("click", () => move(-1));
    el.btnNext.addEventListener("click", () => move(1));
    el.btnPrevMobile.addEventListener("click", () => move(-1));
    el.btnNextMobile.addEventListener("click", () => move(1));
    el.btnNavigatorMobile.addEventListener("click", () => openSheet(el.navigatorDialog));
    el.btnOpenNavigator.addEventListener("click", () => openSheet(el.navigatorDialog));
    el.btnOpenSettings.addEventListener("click", () => openSheet(el.settingsDialog));
    el.btnStarQ.addEventListener("click", toggleStar);
    el.btnStarOnly.addEventListener("click", toggleStarOnly);
    el.checkStarOnly.addEventListener("change", toggleStarOnly);
    el.btnThemeToggle.addEventListener("click", () => {
      const next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      el.btnThemeToggle.textContent = next === "dark" ? "☀️" : "🌙";
      writeStorage(THEME_KEY, next);
    });
    for (const [id, key, convert] of [
      ["lectureFilter", "lecture", input => input.value],
      ["countFilter", "count", input => input.value],
      ["checkShuffleQuestions", "shuffleQ", input => input.checked],
      ["checkShuffleAnswers", "shuffleA", input => input.checked]
    ]) el[id].addEventListener("change", () => requestSetting(key, convert(el[id]), el[id]));
    el.btnShuffleAll.addEventListener("click", () => showConfirm({
      title: "Shuffle and restart?", desc: "This will replace the saved session and clear its answers.",
      button: "Shuffle and restart", danger: true,
      action: () => { state.shuffleQ = state.shuffleA = true; newSession(); closeSheet(el.settingsDialog); }
    }));
    el.btnResetProgress.addEventListener("click", () => {
      if (!answeredCount()) { notice("No answers to reset yet."); return; }
      showConfirm({title: "Reset progress?", desc: "This will clear the answers in the current session.",
        button: "Reset progress", danger: true, action: () => {
          state.answers = {};
          state.currentId = state.viewQuestions[0]?.id ?? null;
          renderAll(); save(); closeSheet(el.settingsDialog);
        }});
    });
    el.btnModalCancel.addEventListener("click", () => closeConfirm(false));
    el.btnModalConfirm.addEventListener("click", () => closeConfirm(true));
    el.confirmModal.addEventListener("cancel", () => { confirmAction = null; });
    el.confirmModal.addEventListener("close", () => { confirmAction = null; });
    for (const dialog of [el.settingsDialog, el.navigatorDialog]) {
      dialog.querySelector("[data-close-sheet]").addEventListener("click", () => closeSheet(dialog));
      dialog.addEventListener("click", event => { if (event.target === dialog) closeSheet(dialog); });
    }
    el.navigatorFilters.addEventListener("click", event => {
      const button = event.target.closest("button[data-filter]");
      if (!button) return;
      state.navFilter = button.dataset.filter;
      el.navigatorFilters.querySelectorAll("button").forEach(item =>
        item.setAttribute("aria-pressed", String(item === button)));
      renderPalette();
    });
    window.addEventListener("keydown", event => {
      if (state.stale || event.altKey || event.ctrlKey || event.metaKey ||
          document.querySelector("dialog[open]") ||
          event.target.closest?.("input, select, textarea, [contenteditable]")) return;
      const key = event.key.toLowerCase();
      const optionIndex = {"1": 0, a: 0, "2": 1, b: 1, "3": 2, c: 2, "4": 3, d: 3}[key];
      if (optionIndex !== undefined) selectAnswer(optionIndex);
      else if (key === "arrowleft") { event.preventDefault(); move(-1); }
      else if (key === "arrowright") { event.preventDefault(); move(1); }
      else if (key === "s") toggleStar();
    });
    window.addEventListener("storage", event => {
      if (event.key !== SESSION_KEY || state.stale) return;
      state.stale = true;
      if (typeof el.staleDialog.showModal === "function") el.staleDialog.showModal();
      else el.staleDialog.setAttribute("open", "");
    });
    el.staleDialog.addEventListener("cancel", event => event.preventDefault());
    el.btnReloadSession.addEventListener("click", () => location.reload());
    window.addEventListener("beforeunload", event => {
      if (!state.canSave && answeredCount()) { event.preventDefault(); event.returnValue = ""; }
    });
    setupSwipe();
  }

  populateLectures();
  initTheme();
  try {
    const stars = JSON.parse(readStorage(STAR_KEY) || "[]");
    if (Array.isArray(stars)) state.starred = new Set(stars.filter(id => byId.has(id)));
  } catch (_) { state.starred = new Set(); }
  setupEvents();
  if (restore()) { syncSettings(); setView(false); }
  else newSession();
  if (!state.canSave) notice("Progress cannot be saved in this browser. Keep this tab open until you finish.");
})();
