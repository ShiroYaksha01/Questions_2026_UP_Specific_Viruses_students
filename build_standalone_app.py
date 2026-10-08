#!/usr/bin/env python3
"""
build_standalone_app.py
Builds a completely self-contained, standalone, mobile-first index.html file containing:
- Mobile-optimized responsive UI (iPhone, Android, tablet, desktop)
- Fixed mobile thumb-zone navigation and tablet sidebar
- Smart in-place scrolling (keeps question in view without jumping to top)
- Filterable Question Navigator bottom sheet
- Local autosave and restore of study progress
- Full dual randomization (Questions + Options)
- Embedded metabolic biochemistry MCQs with PDF-highlighted answers
- Windows double-click ready (runs natively in Edge, Chrome, Firefox with zero tools)
- Vercel ready (static site deployment out-of-the-box)
"""

import hashlib
import json
from pathlib import Path

def main():
    with open("questions_db.json", encoding="utf-8") as f:
        questions_data = json.load(f)

    json_str = json.dumps(questions_data, ensure_ascii=False)
    dataset_hash = hashlib.sha256(json_str.encode("utf-8")).hexdigest()
    source_dir = Path(__file__).resolve().parent
    app_css = (source_dir / "standalone_mobile.css").read_text(encoding="utf-8")
    app_js = (source_dir / "standalone_app.js").read_text(encoding="utf-8")
    total_questions = len(questions_data)

    html_template = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
  <meta name="theme-color" content="#2563eb">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="description" content="Metabolic Biochemistry Year 2 MCQ review. Practice {total_questions} PDF questions with randomized choices and highlighted answers.">
  <title>Metabolic Biochemistry QCM Review 2026 — University of Puthisastra</title>
  
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

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
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

      --bg-body: #090d16;
      --bg-card: #131b2a;
      --bg-subtle: #1c2638;
      --border: #2c384d;

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
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      padding-bottom: env(safe-area-inset-bottom);
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    /* Top Sticky Header */
    header {{
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
      padding-top: env(safe-area-inset-top);
    }}

    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.65rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
      text-decoration: none;
      color: inherit;
      min-width: 0;
    }}

    .brand-icon {{
      width: 38px;
      height: 38px;
      min-width: 38px;
      background: linear-gradient(135deg, var(--primary), #8b5cf6);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 1.25rem;
      font-weight: bold;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
    }}

    .brand-title {{
      min-width: 0;
    }}

    .brand-title h1 {{
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .brand-title p {{
      font-size: 0.7rem;
      color: var(--text-muted);
      font-weight: 500;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-shrink: 0;
    }}

    .btn-shuffle-top {{
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      color: white;
      border: none;
      padding: 0.5rem 0.85rem;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
      touch-action: manipulation;
      min-height: 38px;
    }}

    @media (max-width: 480px) {{
      .btn-shuffle-top span.btn-lbl {{
        display: none;
      }}
      .btn-shuffle-top {{
        padding: 0.5rem 0.65rem;
      }}
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
      touch-action: manipulation;
    }}

    /* Main Container */
    main {{
      flex: 1;
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
      padding: 1rem;
    }}

    @media (min-width: 768px) {{
      main {{
        padding: 1.5rem 1.25rem 3rem 1.25rem;
      }}
    }}

    /* Controls Panel */
    .controls-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
    }}

    .controls-toggle-btn {{
      display: none;
      width: 100%;
      background: none;
      border: none;
      color: var(--text-main);
      padding: 0;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      align-items: center;
      justify-content: space-between;
      min-height: 38px;
      touch-action: manipulation;
    }}

    .controls-toggle-left {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      font-size: 0.88rem;
    }}

    .controls-toggle-right {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .controls-body {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }}

    @media (max-width: 640px) {{
      .controls-panel {{
        padding: 0.65rem 0.85rem;
        margin-bottom: 0.85rem;
      }}
      .controls-toggle-btn {{
        display: flex;
      }}
      .controls-body {{
        display: none;
        padding-top: 0.75rem;
        border-top: 1px solid var(--border);
        margin-top: 0.45rem;
      }}
      .controls-body.is-open {{
        display: flex;
      }}
      .filter-item {{
        width: 100%;
        flex: 1 1 100%;
      }}
      .select-box {{
        width: 100%;
        font-size: 16px; /* Prevents iOS Safari auto-zoom */
      }}
    }}

    .controls-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }}

    .filter-item {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex: 1 1 240px;
    }}

    .filter-label {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
      white-space: nowrap;
    }}

    .select-box {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border: 1px solid var(--border);
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.88rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
      min-height: 44px;
      touch-action: manipulation;
    }}

    .stats-pills {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.8rem;
      flex-wrap: wrap;
    }}

    .pill {{
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-full);
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
    }}

    .pill-blue {{ background: var(--primary-light); color: var(--primary-text); }}
    .pill-green {{ background: var(--success-light); color: var(--success-text); }}

    .randomize-toggles {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.65rem 1rem;
      font-size: 0.85rem;
      font-weight: 600;
    }}

    .toggle-chip {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-full);
      cursor: pointer;
      user-select: none;
      touch-action: manipulation;
    }}

    .toggle-chip input {{
      width: 16px;
      height: 16px;
      accent-color: var(--primary);
      cursor: pointer;
    }}

    /* Main Grid Layout */
    .content-grid {{
      display: grid;
      grid-template-columns: 1fr 310px;
      gap: 1.25rem;
      align-items: start;
    }}

    @media (max-width: 880px) {{
      .content-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Question Card */
    .q-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
    }}

    @media (min-width: 640px) {{
      .q-card {{
        padding: 2rem;
      }}
    }}

    .q-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }}

    .q-meta-badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      align-items: center;
    }}

    .badge-lec {{
      background: var(--primary-light);
      color: var(--primary-text);
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .badge-orig {{
      background: var(--bg-subtle);
      color: var(--text-muted);
      font-size: 0.72rem;
      font-weight: 600;
      padding: 0.2rem 0.5rem;
      border-radius: var(--radius-full);
    }}

    .btn-star {{
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      color: var(--text-muted);
      width: 40px;
      height: 40px;
      min-width: 40px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.25rem;
      touch-action: manipulation;
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
      font-size: clamp(1.05rem, 3.8vw, 1.25rem);
      font-weight: 700;
      line-height: 1.45;
      color: var(--text-main);
      margin-bottom: 1.25rem;
    }}

    /* Options List */
    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-bottom: 1.25rem;
    }}

    .opt-btn {{
      background: var(--bg-subtle);
      border: 2px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.85rem 1rem;
      text-align: left;
      font-size: 0.92rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      min-height: 52px;
      touch-action: manipulation;
      transition: background 0.15s, border-color 0.15s;
    }}

    .opt-btn:active:not(.locked) {{
      transform: scale(0.99);
      background: var(--bg-card);
    }}

    @media (hover: hover) {{
      .opt-btn:hover:not(.locked) {{
        border-color: var(--primary);
        background: var(--bg-card);
      }}
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
      font-weight: 800;
      font-size: 0.82rem;
      color: var(--text-muted);
      flex-shrink: 0;
    }}

    .opt-text {{
      flex: 1;
      line-height: 1.4;
      word-break: break-word;
    }}

    /* Correct / Wrong States */
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

    /* Highlighted Answer Box */
    .expl-box {{
      background: var(--bg-subtle);
      border-left: 4px solid var(--success);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 1rem;
      margin-bottom: 1.25rem;
      animation: slideDown 0.25s ease-out;
    }}

    .expl-header {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 800;
      font-size: 0.9rem;
      color: var(--success-text);
      flex-wrap: wrap;
    }}

    /* Navigation Bar (Single in-card button set, thumb-friendly on mobile) */
    .q-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      padding-top: 1.25rem;
      margin-top: 0.5rem;
      border-top: 1px solid var(--border);
    }}

    .btn-nav {{
      background: var(--primary);
      color: white;
      border: 1px solid transparent;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-md);
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      min-height: 50px;
      touch-action: manipulation;
      user-select: none;
      transition: background-color 0.15s ease, transform 0.1s ease, box-shadow 0.15s ease;
    }}

    .btn-nav:active:not(:disabled) {{
      transform: scale(0.98);
    }}

    .btn-nav#btnNext {{
      flex: 1.35;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.25);
    }}

    .btn-nav#btnNext:hover:not(:disabled) {{
      background: var(--primary-hover);
    }}

    .btn-nav-outline {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border: 1px solid var(--border);
      flex: 1;
    }}

    .btn-nav-outline:hover:not(:disabled) {{
      background: var(--border);
    }}

    .btn-nav:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
      pointer-events: none;
      box-shadow: none;
    }}

    /* Palette Sidebar / Mobile Drawer */
    .palette-sidebar {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1rem;
      box-shadow: var(--shadow-sm);
    }}

    @media (min-width: 881px) {{
      .palette-sidebar {{
        position: sticky;
        top: 80px;
        max-height: calc(100vh - 120px);
        display: flex;
        flex-direction: column;
      }}
      .palette-grid {{
        flex: 1;
        overflow-y: auto;
      }}
    }}

    .palette-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.75rem;
      font-size: 0.9rem;
      font-weight: 700;
    }}

    .palette-toggle-btn {{
      display: none;
      width: 100%;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 0.65rem 1rem;
      border-radius: var(--radius-md);
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      text-align: left;
      align-items: center;
      justify-content: space-between;
      min-height: 44px;
      touch-action: manipulation;
    }}

    @media (max-width: 880px) {{
      .palette-toggle-btn {{
        display: flex;
      }}
      .palette-body {{
        display: none;
        margin-top: 0.75rem;
      }}
      .palette-body.is-open {{
        display: block;
      }}
    }}

    .palette-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 0.35rem;
      max-height: 320px;
      overflow-y: auto;
      padding-right: 0.2rem;
    }}

    @media (min-width: 480px) and (max-width: 880px) {{
      .palette-grid {{
        grid-template-columns: repeat(8, 1fr);
      }}
    }}

    .pal-btn {{
      height: 38px;
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
      touch-action: manipulation;
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


    @keyframes slideDown {{
      from {{ opacity: 0; transform: translateY(-6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Modal Dialog */
    .modal-dialog {{
      border: none;
      border-radius: var(--radius-lg);
      padding: 0;
      background: transparent;
      max-width: 380px;
      width: calc(100% - 2rem);
      margin: auto;
      box-shadow: var(--shadow-lg);
    }}

    .modal-dialog::backdrop {{
      background: rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      animation: fadeIn 0.2s ease-out;
    }}

    .modal-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem 1.25rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.75rem;
      animation: scaleUp 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .modal-icon-badge {{
      width: 54px;
      height: 54px;
      border-radius: var(--radius-full);
      background: var(--primary-light);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.75rem;
      margin-bottom: 0.2rem;
    }}

    .modal-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.3;
    }}

    .modal-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .modal-desc strong {{
      color: var(--text-main);
    }}

    .modal-actions {{
      display: flex;
      gap: 0.65rem;
      width: 100%;
      margin-top: 0.65rem;
    }}

    .btn-modal {{
      flex: 1;
      padding: 0.75rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      min-height: 48px;
      touch-action: manipulation;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}

    .btn-modal:active {{
      transform: scale(0.98);
    }}

    .btn-modal-cancel {{
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      color: var(--text-main);
    }}

    .btn-modal-confirm {{
      background: var(--primary);
      border: 1px solid transparent;
      color: white;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.25);
    }}

    .btn-modal-confirm.danger {{
      background: var(--danger);
      box-shadow: 0 2px 6px rgba(239, 68, 68, 0.25);
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    @keyframes scaleUp {{
      from {{ opacity: 0; transform: scale(0.92); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .hidden {{ display: none !important; }}
  </style>
  <style>{app_css}</style>
</head>
<body>

  <!-- Top Sticky Header -->
  <header>
    <div class="header-inner">
      <a href="#" class="brand">
        <div class="brand-icon">🔬</div>
        <div class="brand-title">
          <h1>Metabolic Biochemistry QCM</h1>
          <p>Year 2 Assessment &bull; {total_questions} Questions</p>
        </div>
      </a>

      <div class="header-actions">
        <button type="button" class="btn-icon header-star" id="btnStarOnly" aria-label="Show starred questions" aria-pressed="false" title="Show starred questions">☆</button>
        <button type="button" class="btn-icon header-navigator" id="btnOpenNavigator" aria-label="Open question navigator" title="Question navigator">▦</button>
        <button type="button" class="btn-icon" id="btnOpenSettings" aria-label="Open study settings" title="Study settings">⚙</button>
        <button type="button" class="btn-icon" id="btnThemeToggle" aria-label="Toggle dark mode" title="Toggle Dark/Light Mode">🌙</button>
      </div>
    </div>
    <div class="header-progress" role="progressbar" aria-label="Questions answered" aria-valuemin="0" aria-valuemax="{total_questions}" aria-valuenow="0" id="headerProgress"><div id="progressFill"></div></div>
  </header>

  <!-- Main Content Container -->
  <main>
    <div class="study-notice hidden" id="studyNotice" role="status"></div>

    <!-- Study settings -->
    <dialog class="study-sheet settings-dialog" id="settingsDialog" aria-labelledby="settingsTitle" closedby="any">
      <div class="sheet-card">
      <div class="sheet-heading"><h2 id="settingsTitle">Study settings</h2><button type="button" class="sheet-close" data-close-sheet aria-label="Close settings">×</button></div>
    <div class="controls-panel">
      <!-- Mobile Bar Toggle -->
      <button type="button" class="controls-toggle-btn hidden" id="btnToggleControls">
        <span class="controls-toggle-left">
          <span>⚙️</span>
          <span id="controlsSummaryText">Metabolic Biochemistry • {total_questions} Qs</span>
        </span>
        <span class="controls-toggle-right">
          <span class="pill pill-blue" id="progressPillMobile" style="font-size:0.75rem; padding:0.2rem 0.55rem;">0/{total_questions}</span>
          <span id="controlsArrow">▼</span>
        </span>
      </button>

      <div class="controls-body" id="controlsBody">
        <div class="controls-row">
          
          <!-- Filter Topic -->
          <div class="filter-item">
            <span class="filter-label">Topic:</span>
            <select id="lectureFilter" class="select-box">
              <!-- Populated via JS -->
            </select>
          </div>

          <!-- Filter Question Count -->
          <div class="filter-item">
            <span class="filter-label">Count:</span>
            <select id="countFilter" class="select-box">
              <option value="all" selected>All {total_questions} Questions</option>
              <option value="10">10 Questions (Quick Test)</option>
              <option value="20">20 Questions</option>
              <option value="50">50 Questions</option>
              <option value="100">100 Questions</option>
            </select>
          </div>

          <!-- Stats Counter -->
          <div class="stats-pills">
            <span class="pill pill-blue" id="progressPill">0 / {total_questions} Answered</span>
            <span class="pill pill-green" id="accuracyPill">0% Accuracy</span>
          </div>

        </div>

        <div class="controls-row" style="padding-top:0.6rem; border-top:1px solid var(--border);">
          
          <!-- Randomize Toggles -->
          <div class="randomize-toggles">
            <label class="toggle-chip">
              <input type="checkbox" id="checkShuffleQuestions" checked>
              <span>🔀 Questions</span>
            </label>
            <label class="toggle-chip">
              <input type="checkbox" id="checkShuffleAnswers" checked>
              <span>🔀 Choices (A–D)</span>
            </label>
            <label class="toggle-chip">
              <input type="checkbox" id="checkStarOnly">
              <span>⭐ Starred</span>
            </label>
          </div>

          <button type="button" class="btn-nav btn-nav-outline" id="btnResetProgress" style="padding:0.35rem 0.75rem; font-size:0.78rem; min-height:36px; flex:none;">
            🔄 Reset
          </button>
          <button type="button" class="btn-nav btn-nav-outline" id="btnShuffleAll">🎲 Shuffle &amp; restart</button>

        </div>
      </div>
    </div>
      </div>
    </dialog>

    <!-- Question + Palette Grid -->
    <div class="content-grid">
      
      <!-- Question Card -->
      <section class="q-card" id="touchArea">
        
        <div class="q-card-header">
          <div class="q-meta-badges">
            <span class="badge-lec" id="badgeLecture">Metabolic Biochemistry</span>
            <span class="badge-orig" id="badgeOrigQ">Original Q1</span>
            <span class="badge-orig" id="badgePosition">Question 1 of {total_questions}</span>
          </div>
          <button type="button" class="btn-star" id="btnStarQ" title="Star / Bookmark for review">☆</button>
        </div>

        <h2 class="q-title" id="qTitle">Question text loading...</h2>

        <!-- Shuffled Options -->
        <div class="options-grid" id="optionsContainer">
          <!-- Dynamic options buttons -->
        </div>

        <!-- Highlighted answer box -->
        <div class="expl-box hidden" id="explBox">
          <div class="expl-header">
            <span>✓ Highlighted Correct Answer:</span>
            <span id="explAnswerLabel" style="color:var(--text-main);"></span>
          </div>
        </div>

        <!-- In-Card Navigation Bar (Single set for mobile & desktop) -->
        <div class="q-nav-bar">
          <button type="button" class="btn-nav btn-nav-outline" id="btnPrev">← Previous</button>
          <button type="button" class="btn-nav" id="btnNext">Next Question →</button>
        </div>

      </section>

      <!-- Palette Sidebar / Collapsible Mobile Drawer -->
      <aside class="palette-sidebar">
        <button type="button" class="palette-toggle-btn" id="btnTogglePalette">
          <span>📑 Question Navigator (<span id="palDrawerCounter">0/{total_questions}</span>)</span>
          <span id="palArrow">▼</span>
        </button>

        <div class="palette-body" id="paletteBody">
          <div class="palette-header">
            <span>Question Navigator</span>
            <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;" id="palAnsweredCounter">0 / {total_questions}</span>
          </div>
          <div class="palette-grid" id="paletteGrid">
            <!-- Grid items -->
          </div>
        </div>
      </aside>

    </div>

  </main>

  <nav class="mobile-nav" aria-label="Question navigation">
    <button type="button" id="btnPrevMobile" class="mobile-nav-prev">← Prev</button>
    <button type="button" id="btnNavigatorMobile" class="mobile-nav-center" aria-label="Open question navigator">Q <span id="mobilePosition">1/160</span> ▦</button>
    <button type="button" id="btnNextMobile" class="mobile-nav-next">Next →</button>
  </nav>

  <dialog class="study-sheet navigator-dialog" id="navigatorDialog" aria-labelledby="navigatorTitle" closedby="any">
    <div class="sheet-card">
      <div class="sheet-handle" aria-hidden="true"></div>
      <div class="sheet-heading"><h2 id="navigatorTitle">Question navigator</h2><button type="button" class="sheet-close" data-close-sheet aria-label="Close navigator">×</button></div>
      <p class="sheet-subtitle" id="navigatorCount">0 / 160 answered</p>
      <div class="navigator-filters" id="navigatorFilters" role="group" aria-label="Filter questions">
        <button type="button" data-filter="all" aria-pressed="true">All</button>
        <button type="button" data-filter="correct" aria-pressed="false">Correct</button>
        <button type="button" data-filter="wrong" aria-pressed="false">Wrong</button>
        <button type="button" data-filter="unanswered" aria-pressed="false">Unanswered</button>
        <button type="button" data-filter="starred" aria-pressed="false">Starred</button>
      </div>
      <div class="palette-grid sheet-palette" id="sheetPaletteGrid"></div>
      <p class="navigator-empty hidden" id="navigatorEmpty">No questions match this filter.</p>
    </div>
  </dialog>

  <dialog class="modal-dialog" id="staleDialog" aria-labelledby="staleTitle" closedby="none">
    <div class="modal-card"><div class="modal-icon-badge">↻</div><h3 class="modal-title" id="staleTitle">Progress changed in another tab</h3><p class="modal-desc">Reload to continue with the latest saved session.</p><button type="button" class="btn-modal btn-modal-confirm" id="btnReloadSession">Reload saved session</button></div>
  </dialog>

  <!-- Confirmation Modal Dialog -->
  <dialog class="modal-dialog" id="confirmModal" closedby="any">
    <div class="modal-card">
      <div class="modal-icon-badge" id="modalIcon">🎲</div>
      <h3 class="modal-title" id="modalTitle">Shuffle All Questions?</h3>
      <p class="modal-desc" id="modalDesc">
        This will re-randomize question order and answer choices, and reset your current progress.
      </p>
      <div class="modal-actions">
        <button type="button" class="btn-modal btn-modal-cancel" id="btnModalCancel">Cancel</button>
        <button type="button" class="btn-modal btn-modal-confirm" id="btnModalConfirm">Shuffle &amp; Restart</button>
      </div>
    </div>
  </dialog>

  <!-- Embedded Raw Database -->
  <script>
    window.RAW_QUESTIONS = {json_str};
  </script>

  <!-- Application Logic -->
  <script>window.DATASET_HASH = "{dataset_hash}";</script>
  <script>
{app_js}
  </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Generated mobile-optimized standalone index.html successfully!")

if __name__ == "__main__":
    main()
