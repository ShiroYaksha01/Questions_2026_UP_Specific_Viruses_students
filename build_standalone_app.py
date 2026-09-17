#!/usr/bin/env python3
"""
build_standalone_app.py
Builds a completely self-contained, standalone index.html file containing:
- Modern, responsive, aesthetic UI with Dark/Light modes
- Real-time randomization of both Questions and Answers/Options
- Embedded questions database (all 241 questions with 100% verified highlighted answers)
- Zero external build tools, zero node/python dependencies needed by the student
- Windows double-click ready (runs natively in Edge, Chrome, Firefox)
- Vercel ready (static site deployment out-of-the-box)
"""

import json

def main():
    with open("questions_db.json", encoding="utf-8") as f:
        questions_data = json.load(f)

    json_str = json.dumps(questions_data, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Virology QCM Review 2026 — University of Puthisastra (UP)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-light: #eff6ff;
      --primary-border: #bfdbfe;
      --primary-text: #1d4ed8;

      --success: #10b981;
      --success-light: #ecfdf5;
      --success-border: #6ee7b7;
      --success-text: #047857;

      --danger: #ef4444;
      --danger-light: #fef2f2;
      --danger-border: #fca5a5;
      --danger-text: #b91c1c;

      --warning: #f59e0b;
      --warning-light: #fffbeb;
      --warning-border: #fcd34d;
      --warning-text: #b45309;

      --bg-body: #f8fafc;
      --bg-card: #ffffff;
      --bg-subtle: #f1f5f9;
      --border: #e2e8f0;

      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-dim: #94a3b8;

      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);

      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
    }}

    [data-theme="dark"] {{
      --primary: #3b82f6;
      --primary-hover: #60a5fa;
      --primary-light: #1e293b;
      --primary-border: #3b82f6;
      --primary-text: #93c5fd;

      --success: #10b981;
      --success-light: #064e3b;
      --success-border: #059669;
      --success-text: #a7f3d0;

      --danger: #ef4444;
      --danger-light: #7f1d1d;
      --danger-border: #dc2626;
      --danger-text: #fecaca;

      --warning: #f59e0b;
      --warning-light: #78350f;
      --warning-border: #d97706;
      --warning-text: #fde68a;

      --bg-body: #0b0f19;
      --bg-card: #151e2e;
      --bg-subtle: #1e293b;
      --border: #334155;

      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;

      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    /* Navbar Header */
    header {{
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }}

    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: inherit;
    }}

    .brand-icon {{
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, var(--primary), #8b5cf6);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 1.35rem;
      font-weight: bold;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
    }}

    .brand-title h1 {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}

    .brand-title p {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .btn-shuffle-top {{
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
    }}

    .btn-shuffle-top:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }}

    .btn-icon {{
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      color: var(--text-main);
      width: 38px;
      height: 38px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.1rem;
      transition: all 0.15s ease;
    }}

    .btn-icon:hover {{
      background: var(--border);
    }}

    /* Main Container */
    main {{
      flex: 1;
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
      padding: 1.5rem 1.25rem 3rem 1.25rem;
    }}

    /* Settings & Controls Bar */
    .controls-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .controls-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .filter-item {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .filter-label {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}

    .select-box {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border: 1px solid var(--border);
      padding: 0.5rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
      transition: border-color 0.15s ease;
    }}

    .select-box:focus {{
      border-color: var(--primary);
    }}

    .randomize-toggles {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 1.25rem;
      font-size: 0.9rem;
      font-weight: 600;
    }}

    .toggle-check {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      cursor: pointer;
      user-select: none;
    }}

    .toggle-check input {{
      width: 17px;
      height: 17px;
      accent-color: var(--primary);
      cursor: pointer;
    }}

    .stats-pills {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
    }}

    .pill {{
      padding: 0.35rem 0.75rem;
      border-radius: var(--radius-full);
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }}

    .pill-blue {{ background: var(--primary-light); color: var(--primary-text); }}
    .pill-green {{ background: var(--success-light); color: var(--success-text); }}

    /* Layout: Question & Sidebar */
    .content-grid {{
      display: grid;
      grid-template-columns: 1fr 310px;
      gap: 1.5rem;
      align-items: start;
    }}

    @media (max-width: 900px) {{
      .content-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Question Card */
    .q-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-sm);
    }}

    .q-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }}

    .q-meta-badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      align-items: center;
    }}

    .badge-lec {{
      background: var(--primary-light);
      color: var(--primary-text);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .badge-orig {{
      background: var(--bg-subtle);
      color: var(--text-muted);
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-full);
    }}

    .btn-star {{
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.15rem;
      transition: all 0.15s ease;
    }}

    .btn-star.starred {{
      background: #fef9c3;
      color: #ca8a04;
      border-color: #fde047;
    }}

    [data-theme="dark"] .btn-star.starred {{
      background: #713f12;
      color: #fde047;
      border-color: #a16207;
    }}

    .q-title {{
      font-size: 1.2rem;
      font-weight: 700;
      line-height: 1.5;
      color: var(--text-main);
      margin-bottom: 1.5rem;
    }}

    /* Options List */
    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.75rem;
    }}

    .opt-btn {{
      background: var(--bg-subtle);
      border: 2px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.95rem 1.25rem;
      text-align: left;
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 1rem;
      transition: all 0.15s ease;
      position: relative;
    }}

    .opt-btn:hover:not(.locked) {{
      border-color: var(--primary);
      background: var(--bg-card);
      transform: translateY(-1px);
    }}

    .opt-tag {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: var(--bg-card);
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--text-muted);
      flex-shrink: 0;
      transition: all 0.15s ease;
    }}

    .opt-text {{
      flex: 1;
      line-height: 1.4;
    }}

    /* Correct / Incorrect Feedback Styles */
    .opt-btn.is-correct {{
      background: var(--success-light) !important;
      border-color: var(--success-border) !important;
      color: var(--success-text) !important;
      font-weight: 600;
    }}

    .opt-btn.is-correct .opt-tag {{
      background: var(--success) !important;
      color: white !important;
      border-color: var(--success) !important;
    }}

    .opt-btn.is-wrong {{
      background: var(--danger-light) !important;
      border-color: var(--danger-border) !important;
      color: var(--danger-text) !important;
    }}

    .opt-btn.is-wrong .opt-tag {{
      background: var(--danger) !important;
      color: white !important;
      border-color: var(--danger) !important;
    }}

    /* Explanation Box */
    .expl-box {{
      background: var(--bg-subtle);
      border-left: 4px solid var(--success);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
      animation: slideDown 0.25s ease-out;
    }}

    .expl-header {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--success-text);
      margin-bottom: 0.5rem;
    }}

    .expl-content {{
      font-size: 0.9rem;
      line-height: 1.55;
      color: var(--text-main);
    }}

    .expl-takeaway {{
      margin-top: 0.75rem;
      padding: 0.6rem 0.85rem;
      background: var(--bg-card);
      border: 1px dashed var(--border);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .takeaway-lbl {{
      background: var(--warning-light);
      color: var(--warning-text);
      font-weight: 800;
      font-size: 0.7rem;
      padding: 0.2rem 0.45rem;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }}

    /* Card Bottom Navigation */
    .q-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border);
    }}

    .btn-nav {{
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.65rem 1.4rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.15s ease;
    }}

    .btn-nav:hover:not(:disabled) {{
      background: var(--primary-hover);
      transform: translateY(-1px);
    }}

    .btn-nav:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }}

    .btn-nav-outline {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border: 1px solid var(--border);
    }}

    .btn-nav-outline:hover:not(:disabled) {{
      background: var(--border);
    }}

    /* Right Sidebar Palette */
    .palette-sidebar {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 80px;
      max-height: calc(100vh - 120px);
      display: flex;
      flex-direction: column;
    }}

    .palette-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
      font-size: 0.95rem;
      font-weight: 700;
    }}

    .palette-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 0.4rem;
      overflow-y: auto;
      padding-right: 0.25rem;
      flex: 1;
    }}

    .pal-btn {{
      aspect-ratio: 1;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
    }}

    .pal-btn:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}

    .pal-btn.current {{
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary-text);
      font-weight: 800;
    }}

    .pal-btn.correct {{
      background: var(--success-light);
      color: var(--success-text);
      border-color: var(--success);
    }}

    .pal-btn.wrong {{
      background: var(--danger-light);
      color: var(--danger-text);
      border-color: var(--danger);
    }}

    .kbd-tip {{
      font-size: 0.75rem;
      color: var(--text-dim);
      text-align: center;
      margin-top: 1rem;
      line-height: 1.4;
    }}

    kbd {{
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 1px 5px;
      font-family: monospace;
      font-size: 0.75rem;
    }}

    @keyframes slideDown {{
      from {{ opacity: 0; transform: translateY(-6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .hidden {{ display: none !important; }}
  </style>
</head>
<body>

  <!-- Top Navbar -->
  <header>
    <div class="header-inner">
      <a href="#" class="brand">
        <div class="brand-icon">🔬</div>
        <div class="brand-title">
          <h1>Virology QCM Review</h1>
          <p>UP Specific Viruses Exam 2026 — 241 Official Questions</p>
        </div>
      </a>

      <div class="header-actions">
        <button type="button" class="btn-shuffle-top" id="btnShuffleAll" title="Reshuffle both questions and answer choices">
          <span>🎲</span> Shuffle All
        </button>
        <button type="button" class="btn-icon" id="btnThemeToggle" title="Toggle Dark/Light Mode">🌙</button>
      </div>
    </div>
  </header>

  <!-- Main Content Area -->
  <main>

    <!-- Top Settings & Controls -->
    <div class="controls-panel">
      <div class="controls-row">
        
        <!-- Filter Lecture -->
        <div class="filter-item">
          <span class="filter-label">Lecture:</span>
          <select id="lectureFilter" class="select-box">
            <!-- Populated via JS -->
          </select>
        </div>

        <!-- Filter Count -->
        <div class="filter-item">
          <span class="filter-label">Count:</span>
          <select id="countFilter" class="select-box">
            <option value="all" selected>All Questions</option>
            <option value="10">10 Questions (Quick Test)</option>
            <option value="25">25 Questions</option>
            <option value="50">50 Questions</option>
            <option value="100">100 Questions</option>
          </select>
        </div>

        <!-- Stats Counter -->
        <div class="stats-pills">
          <span class="pill pill-blue" id="progressPill">0 / 241 Answered</span>
          <span class="pill pill-green" id="accuracyPill">0% Accuracy</span>
        </div>

      </div>

      <div class="controls-row" style="padding-top:0.75rem; border-top:1px solid var(--border);">
        
        <!-- Randomization Toggles -->
        <div class="randomize-toggles">
          <label class="toggle-check">
            <input type="checkbox" id="checkShuffleQuestions" checked>
            <span>🔀 Randomize Questions</span>
          </label>
          <label class="toggle-check">
            <input type="checkbox" id="checkShuffleAnswers" checked>
            <span>🔀 Randomize Answers (A, B, C, D)</span>
          </label>
          <label class="toggle-check">
            <input type="checkbox" id="checkStarOnly">
            <span>⭐ Starred Only</span>
          </label>
        </div>

        <button type="button" class="btn-nav btn-nav-outline" id="btnResetProgress" style="padding:0.4rem 0.85rem; font-size:0.8rem;">
          🔄 Reset Session
        </button>

      </div>
    </div>

    <!-- Question + Palette Grid -->
    <div class="content-grid">
      
      <!-- Question Card -->
      <section class="q-card">
        
        <div class="q-card-header">
          <div class="q-meta-badges">
            <span class="badge-lec" id="badgeLecture">Lecture 1: HIV</span>
            <span class="badge-orig" id="badgeOrigQ">Original Q1</span>
            <span class="badge-orig" id="badgePosition">Question 1 of 241</span>
          </div>
          <button type="button" class="btn-star" id="btnStarQ" title="Star / Bookmark for review">☆</button>
        </div>

        <h2 class="q-title" id="qTitle">Question text loading...</h2>

        <!-- Shuffled Options -->
        <div class="options-grid" id="optionsContainer">
          <!-- Dynamic options buttons -->
        </div>

        <!-- Explanation & Takeaway Box -->
        <div class="expl-box hidden" id="explBox">
          <div class="expl-header">
            <span>✓ Verified Answer:</span>
            <span id="explAnswerLabel" style="color:var(--text-main);"></span>
          </div>
          <p class="expl-content" id="explText"></p>
          <div class="expl-takeaway">
            <span class="takeaway-lbl">Exam Takeaway</span>
            <span id="explTakeaway" style="font-weight:600;"></span>
          </div>
        </div>

        <!-- Navigation Bar -->
        <div class="q-nav-bar">
          <button type="button" class="btn-nav btn-nav-outline" id="btnPrev">← Previous</button>
          <button type="button" class="btn-nav" id="btnNext">Next Question →</button>
        </div>

      </section>

      <!-- Palette Sidebar -->
      <aside class="palette-sidebar">
        <div class="palette-header">
          <span>Question Palette</span>
          <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;" id="palAnsweredCounter">0 / 241</span>
        </div>
        <div class="palette-grid" id="paletteGrid">
          <!-- Grid items -->
        </div>
        <p class="kbd-tip">
          Shortcuts: <kbd>1</kbd>-<kbd>4</kbd> or <kbd>A</kbd>-<kbd>D</kbd> select &bull; <kbd>←</kbd> <kbd>→</kbd> navigate &bull; <kbd>S</kbd> star
        </p>
      </aside>

    </div>

  </main>

  <!-- Embedded Raw Database -->
  <script>
    window.RAW_QUESTIONS = {json_str};
  </script>

  <!-- Application Logic -->
  <script>
    (function () {{
      "use strict";

      const rawDB = window.RAW_QUESTIONS || [];
      if (!rawDB.length) {{
        alert("Questions database is empty or failed to load.");
        return;
      }}

      // Application State
      const state = {{
        activeQuestions: [], // Shuffled questions currently in session
        currentIndex: 0,
        userAnswers: {{}}, // {{ [question_unique_id]: selected_option_index }}
        starredSet: new Set(JSON.parse(localStorage.getItem("virology_stars_up") || "[]")),
        
        // Settings
        filterLecture: "all",
        filterCount: "all",
        shuffleQuestions: true,
        shuffleAnswers: true,
        starOnly: false
      }};

      // DOM Elements
      const el = {{
        themeBtn: document.getElementById("btnThemeToggle"),
        btnShuffleAll: document.getElementById("btnShuffleAll"),
        lectureFilter: document.getElementById("lectureFilter"),
        countFilter: document.getElementById("countFilter"),
        checkShuffleQ: document.getElementById("checkShuffleQuestions"),
        checkShuffleA: document.getElementById("checkShuffleAnswers"),
        checkStarOnly: document.getElementById("checkStarOnly"),
        btnResetProgress: document.getElementById("btnResetProgress"),

        progressPill: document.getElementById("progressPill"),
        accuracyPill: document.getElementById("accuracyPill"),

        badgeLecture: document.getElementById("badgeLecture"),
        badgeOrigQ: document.getElementById("badgeOrigQ"),
        badgePosition: document.getElementById("badgePosition"),
        btnStarQ: document.getElementById("btnStarQ"),
        qTitle: document.getElementById("qTitle"),
        optionsContainer: document.getElementById("optionsContainer"),

        explBox: document.getElementById("explBox"),
        explAnswerLabel: document.getElementById("explAnswerLabel"),
        explText: document.getElementById("explText"),
        explTakeaway: document.getElementById("explTakeaway"),

        btnPrev: document.getElementById("btnPrev"),
        btnNext: document.getElementById("btnNext"),
        paletteGrid: document.getElementById("paletteGrid"),
        palAnsweredCounter: document.getElementById("palAnsweredCounter")
      }};

      // Fisher-Yates Shuffle
      function shuffle(array) {{
        const arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
        }}
        return arr;
      }}

      // Theme Init
      function initTheme() {{
        const saved = localStorage.getItem("virology_theme_mode") || "light";
        document.documentElement.setAttribute("data-theme", saved);
        el.themeBtn.textContent = saved === "dark" ? "☀️" : "🌙";
      }}

      function toggleTheme() {{
        const cur = document.documentElement.getAttribute("data-theme") || "light";
        const next = cur === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem("virology_theme_mode", next);
        el.themeBtn.textContent = next === "dark" ? "☀️" : "🌙";
      }}

      // Populate Lecture Dropdown
      function populateLectureFilter() {{
        const map = new Map();
        rawDB.forEach(q => {{
          if (!map.has(q.lecture_id)) {{
            map.set(q.lecture_id, {{ name: q.lecture_name, count: 0 }});
          }}
          map.get(q.lecture_id).count++;
        }});

        let html = '<option value="all">All 11 Lectures (241 Questions)</option>';
        map.forEach((val, id) => {{
          html += `<option value="${{id}}">L${{id}}: ${{val.name}} (${{val.count}} Qs)</option>`;
        }});
        el.lectureFilter.innerHTML = html;
      }}

      // Build & Randomize Session Questions
      function buildSession(resetAnswers = false) {{
        if (resetAnswers) {{
          state.userAnswers = {{}};
        }}

        // Filter by lecture
        let list = [...rawDB];
        if (state.filterLecture !== "all") {{
          const lid = parseInt(state.filterLecture, 10);
          list = list.filter(q => q.lecture_id === lid);
        }}

        // Filter starred
        if (state.starOnly) {{
          list = list.filter(q => state.starredSet.has(q.global_id));
        }}

        if (list.length === 0) {{
          alert("No questions match your current filter criteria.");
          if (state.starOnly) {{
            state.starOnly = false;
            el.checkStarOnly.checked = false;
            buildSession(false);
            return;
          }}
        }}

        // Randomize questions order if enabled
        if (state.shuffleQuestions) {{
          list = shuffle(list);
        }}

        // Filter count
        if (state.filterCount !== "all") {{
          const maxCount = parseInt(state.filterCount, 10);
          list = list.slice(0, maxCount);
        }}

        // Prepare questions with options
        state.activeQuestions = list.map((q, idx) => {{
          // Convert options dict to array
          const rawOpts = [];
          ["A", "B", "C", "D", "E"].forEach(letter => {{
            if (q.options[letter]) {{
              rawOpts.push({{
                origLetter: letter,
                text: q.options[letter],
                isCorrect: (letter === q.correct_answer)
              }});
            }}
          }});

          // Shuffle options if enabled
          const finalOpts = state.shuffleAnswers ? shuffle(rawOpts) : rawOpts;

          // Assign letters A, B, C, D to options
          const alphabet = ["A", "B", "C", "D", "E"];
          const formattedOpts = finalOpts.map((opt, oIdx) => ({{
            displayLetter: alphabet[oIdx],
            text: opt.text,
            isCorrect: opt.isCorrect,
            origLetter: opt.origLetter
          }}));

          return {{
            uniqueId: q.global_id + "_" + idx,
            globalId: q.global_id,
            lectureId: q.lecture_id,
            lectureName: q.lecture_name,
            origQId: q.question_id,
            questionText: q.question,
            options: formattedOpts,
            explanation: q.explanation,
            takeaway: q.takeaway,
            correctText: q.correct_text
          }};
        }});

        state.currentIndex = 0;
        renderQuestion();
        renderPalette();
        updateStats();
      }}

      // Render Current Question
      function renderQuestion() {{
        if (!state.activeQuestions.length) return;
        const q = state.activeQuestions[state.currentIndex];
        if (!q) return;

        // Meta badges
        el.badgeLecture.textContent = `L${{q.lectureId}}: ${{q.lectureName}}`;
        el.badgeOrigQ.textContent = `Original Q${{q.origQId}}`;
        el.badgePosition.textContent = `Question ${{state.currentIndex + 1}} of ${{state.activeQuestions.length}}`;
        el.qTitle.textContent = q.questionText;

        // Star button
        const isStarred = state.starredSet.has(q.globalId);
        el.btnStarQ.classList.toggle("starred", isStarred);
        el.btnStarQ.textContent = isStarred ? "★" : "☆";

        // Navigation buttons
        el.btnPrev.disabled = state.currentIndex === 0;
        el.btnNext.disabled = state.currentIndex === state.activeQuestions.length - 1;

        // User answer state
        const selectedOptIdx = state.userAnswers[q.uniqueId];
        const isAnswered = (selectedOptIdx !== undefined);

        // Options
        let html = "";
        q.options.forEach((opt, optIdx) => {{
          let btnClass = "opt-btn";
          if (isAnswered) {{
            btnClass += " locked";
            if (opt.isCorrect) {{
              btnClass += " is-correct";
            }} else if (optIdx === selectedOptIdx) {{
              btnClass += " is-wrong";
            }}
          }}

          html += `
            <button type="button" class="${{btnClass}}" data-opt-index="${{optIdx}}">
              <span class="opt-tag">${{opt.displayLetter}}</span>
              <span class="opt-text">${{opt.text}}</span>
            </button>
          `;
        }});

        el.optionsContainer.innerHTML = html;

        // Option click listener
        el.optionsContainer.querySelectorAll(".opt-btn").forEach(btn => {{
          btn.addEventListener("click", () => {{
            const optIdx = parseInt(btn.getAttribute("data-opt-index"), 10);
            handleOptionSelect(optIdx);
          }});
        }});

        // Explanation Box
        if (isAnswered) {{
          el.explBox.classList.remove("hidden");
          const correctOpt = q.options.find(o => o.isCorrect);
          el.explAnswerLabel.textContent = `${{correctOpt ? correctOpt.displayLetter : ""}}) ${{q.correctText}}`;
          el.explText.textContent = q.explanation;
          el.explTakeaway.textContent = q.takeaway;
        }} else {{
          el.explBox.classList.add("hidden");
        }}

        renderPalette();
      }}

      // Handle Option Selection
      function handleOptionSelect(optIndex) {{
        const q = state.activeQuestions[state.currentIndex];
        if (!q) return;

        state.userAnswers[q.uniqueId] = optIndex;
        renderQuestion();
        updateStats();
      }}

      // Palette Rendering
      function renderPalette() {{
        let html = "";
        state.activeQuestions.forEach((q, idx) => {{
          let btnClass = "pal-btn";
          if (idx === state.currentIndex) btnClass += " current";

          const chosenIdx = state.userAnswers[q.uniqueId];
          if (chosenIdx !== undefined) {{
            const chosenOpt = q.options[chosenIdx];
            btnClass += (chosenOpt && chosenOpt.isCorrect) ? " correct" : " wrong";
          }}

          html += `<button type="button" class="${{btnClass}}" data-nav-index="${{idx}}">${{idx + 1}}</button>`;
        }});

        el.paletteGrid.innerHTML = html;
        el.paletteGrid.querySelectorAll(".pal-btn").forEach(btn => {{
          btn.addEventListener("click", () => {{
            state.currentIndex = parseInt(btn.getAttribute("data-nav-index"), 10);
            renderQuestion();
          }});
        }});

        const answeredCount = Object.keys(state.userAnswers).length;
        el.palAnsweredCounter.textContent = `${{answeredCount}} / ${{state.activeQuestions.length}}`;
      }}

      // Update Statistics
      function updateStats() {{
        const answeredCount = Object.keys(state.userAnswers).length;
        let correctCount = 0;

        state.activeQuestions.forEach(q => {{
          const chosenIdx = state.userAnswers[q.uniqueId];
          if (chosenIdx !== undefined && q.options[chosenIdx] && q.options[chosenIdx].isCorrect) {{
            correctCount++;
          }}
        }});

        const total = state.activeQuestions.length;
        el.progressPill.textContent = `${{answeredCount}} / ${{total}} Answered`;

        const accuracy = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
        el.accuracyPill.textContent = `${{correctCount}} Correct (${{accuracy}}%)`;
      }}

      // Star Toggle
      function toggleStar() {{
        const q = state.activeQuestions[state.currentIndex];
        if (!q) return;

        if (state.starredSet.has(q.globalId)) {{
          state.starredSet.delete(q.globalId);
        }} else {{
          state.starredSet.add(q.globalId);
        }}
        localStorage.setItem("virology_stars_up", JSON.stringify(Array.from(state.starredSet)));
        renderQuestion();
      }}

      // Event Listeners Setup
      function setupListeners() {{
        // Theme
        el.themeBtn.addEventListener("click", toggleTheme);

        // Shuffle Top Button
        el.btnShuffleAll.addEventListener("click", () => {{
          state.shuffleQuestions = true;
          state.shuffleAnswers = true;
          el.checkShuffleQ.checked = true;
          el.checkShuffleA.checked = true;
          buildSession(true);
        }});

        // Filters
        el.lectureFilter.addEventListener("change", (e) => {{
          state.filterLecture = e.target.value;
          buildSession(true);
        }});

        el.countFilter.addEventListener("change", (e) => {{
          state.filterCount = e.target.value;
          buildSession(true);
        }});

        el.checkShuffleQ.addEventListener("change", (e) => {{
          state.shuffleQuestions = e.target.checked;
          buildSession(true);
        }});

        el.checkShuffleA.addEventListener("change", (e) => {{
          state.shuffleAnswers = e.target.checked;
          buildSession(true);
        }});

        el.checkStarOnly.addEventListener("change", (e) => {{
          state.starOnly = e.target.checked;
          buildSession(true);
        }});

        el.btnResetProgress.addEventListener("click", () => {{
          if (confirm("Reset current practice progress?")) {{
            state.userAnswers = {{}};
            renderQuestion();
            renderPalette();
            updateStats();
          }}
        }});

        // Navigation
        el.btnPrev.addEventListener("click", () => {{
          if (state.currentIndex > 0) {{
            state.currentIndex--;
            renderQuestion();
          }}
        }});

        el.btnNext.addEventListener("click", () => {{
          if (state.currentIndex < state.activeQuestions.length - 1) {{
            state.currentIndex++;
            renderQuestion();
          }}
        }});

        el.btnStarQ.addEventListener("click", toggleStar);

        // Keyboard Shortcuts
        window.addEventListener("keydown", (e) => {{
          if (["1", "a", "A"].includes(e.key)) handleOptionSelect(0);
          else if (["2", "b", "B"].includes(e.key)) handleOptionSelect(1);
          else if (["3", "c", "C"].includes(e.key)) handleOptionSelect(2);
          else if (["4", "d", "D"].includes(e.key)) handleOptionSelect(3);
          else if (e.key === "ArrowLeft" && state.currentIndex > 0) {{
            state.currentIndex--;
            renderQuestion();
          }} else if (e.key === "ArrowRight" && state.currentIndex < state.activeQuestions.length - 1) {{
            state.currentIndex++;
            renderQuestion();
          }} else if (e.key.toLowerCase() === "s") {{
            toggleStar();
          }}
        }});
      }}

      // Initialize
      initTheme();
      populateLectureFilter();
      setupListeners();
      buildSession(true);
    }})();
  </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Generated standalone index.html successfully!")

if __name__ == "__main__":
    main()
