#!/usr/bin/env python3
"""
build_standalone_app.py
Builds a completely self-contained, standalone, mobile-first index.html file containing:
- Mobile-optimized responsive UI (iPhone, Android, tablet, desktop)
- Single thumb-friendly navigation button set directly inside the question card
- Smart in-place scrolling (keeps question in view without jumping to top)
- Mobile collapsible Question Navigator drawer
- Full dual randomization (Questions + Options)
- Embedded questions database (all 241 questions with 100% verified highlighted answers)
- Windows double-click ready (runs natively in Edge, Chrome, Firefox with zero tools)
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
  <meta name="theme-color" content="#2563eb">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="description" content="Virology QCM Exam Review 2026 for University of Puthisastra. Practice 241 official questions with randomized choices, answers, and explanations.">
  <title>Virology QCM Review 2026 — University of Puthisastra</title>
  
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
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
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

    /* Explanation Box */
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
      margin-bottom: 0.4rem;
      flex-wrap: wrap;
    }}

    .expl-content {{
      font-size: 0.88rem;
      line-height: 1.5;
      color: var(--text-main);
    }}

    .expl-takeaway {{
      margin-top: 0.65rem;
      padding: 0.5rem 0.75rem;
      background: var(--bg-card);
      border: 1px dashed var(--border);
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      display: flex;
      align-items: flex-start;
      gap: 0.4rem;
      line-height: 1.4;
    }}

    .takeaway-lbl {{
      background: var(--warning-light);
      color: var(--warning-text);
      font-weight: 800;
      font-size: 0.68rem;
      padding: 0.15rem 0.4rem;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      flex-shrink: 0;
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
</head>
<body>

  <!-- Top Sticky Header -->
  <header>
    <div class="header-inner">
      <a href="#" class="brand">
        <div class="brand-icon">🔬</div>
        <div class="brand-title">
          <h1>Virology QCM</h1>
          <p>UP Exam 2026 &bull; 241 Questions</p>
        </div>
      </a>

      <div class="header-actions">
        <button type="button" class="btn-shuffle-top" id="btnShuffleAll" title="Randomize both questions & answer choices">
          <span>🎲</span> <span class="btn-lbl">Shuffle All</span>
        </button>
        <button type="button" class="btn-icon" id="btnThemeToggle" title="Toggle Dark/Light Mode">🌙</button>
      </div>
    </div>
  </header>

  <!-- Main Content Container -->
  <main>

    <!-- Controls Panel -->
    <div class="controls-panel">
      <!-- Mobile Bar Toggle -->
      <button type="button" class="controls-toggle-btn" id="btnToggleControls">
        <span class="controls-toggle-left">
          <span>⚙️</span>
          <span id="controlsSummaryText">All 11 Lectures • 241 Qs</span>
        </span>
        <span class="controls-toggle-right">
          <span class="pill pill-blue" id="progressPillMobile" style="font-size:0.75rem; padding:0.2rem 0.55rem;">0/241</span>
          <span id="controlsArrow">▼</span>
        </span>
      </button>

      <div class="controls-body" id="controlsBody">
        <div class="controls-row">
          
          <!-- Filter Lecture -->
          <div class="filter-item">
            <span class="filter-label">Lecture:</span>
            <select id="lectureFilter" class="select-box">
              <!-- Populated via JS -->
            </select>
          </div>

          <!-- Filter Question Count -->
          <div class="filter-item">
            <span class="filter-label">Count:</span>
            <select id="countFilter" class="select-box">
              <option value="all" selected>All Questions</option>
              <option value="10">10 Questions (Quick Test)</option>
              <option value="20">20 Questions</option>
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

        </div>
      </div>
    </div>

    <!-- Question + Palette Grid -->
    <div class="content-grid">
      
      <!-- Question Card -->
      <section class="q-card" id="touchArea">
        
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
            <span>✓ Highlighted Answer:</span>
            <span id="explAnswerLabel" style="color:var(--text-main);"></span>
          </div>
          <p class="expl-content" id="explText"></p>
          <div class="expl-takeaway">
            <span class="takeaway-lbl">Takeaway</span>
            <span id="explTakeaway" style="font-weight:600;"></span>
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
          <span>📑 Question Navigator (<span id="palDrawerCounter">0/241</span>)</span>
          <span id="palArrow">▼</span>
        </button>

        <div class="palette-body" id="paletteBody">
          <div class="palette-header">
            <span>Question Navigator</span>
            <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;" id="palAnsweredCounter">0 / 241</span>
          </div>
          <div class="palette-grid" id="paletteGrid">
            <!-- Grid items -->
          </div>
        </div>
      </aside>

    </div>

  </main>

  <!-- Confirmation Modal Dialog -->
  <dialog class="modal-dialog" id="confirmModal">
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
        activeQuestions: [],
        currentIndex: 0,
        userAnswers: {{}},
        starredSet: new Set(JSON.parse(localStorage.getItem("virology_stars_up") || "[]")),
        
        // Settings
        filterLecture: "all",
        filterCount: "all",
        shuffleQuestions: true,
        shuffleAnswers: true,
        starOnly: false,
        paletteOpenMobile: false
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

        btnToggleControls: document.getElementById("btnToggleControls"),
        controlsBody: document.getElementById("controlsBody"),
        controlsArrow: document.getElementById("controlsArrow"),
        controlsSummaryText: document.getElementById("controlsSummaryText"),
        progressPillMobile: document.getElementById("progressPillMobile"),

        progressPill: document.getElementById("progressPill"),
        accuracyPill: document.getElementById("accuracyPill"),

        confirmModal: document.getElementById("confirmModal"),
        modalIcon: document.getElementById("modalIcon"),
        modalTitle: document.getElementById("modalTitle"),
        modalDesc: document.getElementById("modalDesc"),
        btnModalCancel: document.getElementById("btnModalCancel"),
        btnModalConfirm: document.getElementById("btnModalConfirm"),

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

        btnTogglePalette: document.getElementById("btnTogglePalette"),
        paletteBody: document.getElementById("paletteBody"),
        palArrow: document.getElementById("palArrow"),
        palDrawerCounter: document.getElementById("palDrawerCounter"),
        paletteGrid: document.getElementById("paletteGrid"),
        palAnsweredCounter: document.getElementById("palAnsweredCounter"),
        touchArea: document.getElementById("touchArea")
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

        let list = [...rawDB];
        if (state.filterLecture !== "all") {{
          const lid = parseInt(state.filterLecture, 10);
          list = list.filter(q => q.lecture_id === lid);
        }}

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

        if (state.shuffleQuestions) {{
          list = shuffle(list);
        }}

        if (state.filterCount !== "all") {{
          const maxCount = parseInt(state.filterCount, 10);
          list = list.slice(0, maxCount);
        }}

        state.activeQuestions = list.map((q, idx) => {{
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

          const finalOpts = state.shuffleAnswers ? shuffle(rawOpts) : rawOpts;
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
        updateControlsSummary();
      }}

      // Render Current Question
      function renderQuestion() {{
        if (!state.activeQuestions.length) return;
        const q = state.activeQuestions[state.currentIndex];
        if (!q) return;

        el.badgeLecture.textContent = `L${{q.lectureId}}: ${{q.lectureName}}`;
        el.badgeOrigQ.textContent = `Original Q${{q.origQId}}`;
        el.badgePosition.textContent = `Question ${{state.currentIndex + 1}} of ${{state.activeQuestions.length}}`;
        el.qTitle.textContent = q.questionText;

        const isStarred = state.starredSet.has(q.globalId);
        el.btnStarQ.classList.toggle("starred", isStarred);
        el.btnStarQ.textContent = isStarred ? "★" : "☆";

        const isFirst = (state.currentIndex === 0);
        const isLast = (state.currentIndex === state.activeQuestions.length - 1);
        el.btnPrev.disabled = isFirst;
        el.btnNext.disabled = isLast;

        const selectedOptIdx = state.userAnswers[q.uniqueId];
        const isAnswered = (selectedOptIdx !== undefined);

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

        el.optionsContainer.querySelectorAll(".opt-btn").forEach(btn => {{
          btn.addEventListener("click", () => {{
            const optIdx = parseInt(btn.getAttribute("data-opt-index"), 10);
            handleOptionSelect(optIdx);
          }});
        }});

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

      // Smart scroll helper: keeps question card comfortably in view without scrolling to top of webpage
      function scrollQuestionIntoView() {{
        const card = el.touchArea || document.getElementById("touchArea");
        if (!card) return;
        const header = document.querySelector("header");
        const headerHeight = header ? header.offsetHeight : 54;
        const rect = card.getBoundingClientRect();
        
        // If top of question card is hidden above header (user scrolled down to read explanations)
        // or pushed down below the fold (> 120px under header):
        if (rect.top < headerHeight || rect.top > headerHeight + 120) {{
          const cardAbsoluteTop = window.scrollY + rect.top;
          const targetY = Math.max(0, cardAbsoluteTop - headerHeight - 12);
          window.scrollTo({{ top: targetY, behavior: "smooth" }});
        }}
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
            scrollQuestionIntoView();
          }});
        }});

        const answeredCount = Object.keys(state.userAnswers).length;
        const total = state.activeQuestions.length;
        el.palAnsweredCounter.textContent = `${{answeredCount}} / ${{total}}`;
        if (el.palDrawerCounter) el.palDrawerCounter.textContent = `${{answeredCount}}/${{total}}`;
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
        if (el.progressPillMobile) el.progressPillMobile.textContent = `${{answeredCount}}/${{total}}`;

        const accuracy = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
        el.accuracyPill.textContent = `${{correctCount}} Correct (${{accuracy}}%)`;
      }}

      // Mobile Controls Summary & Drawer Toggle
      function updateControlsSummary() {{
        if (!el.controlsSummaryText) return;
        const total = state.activeQuestions.length;
        if (state.filterLecture === "all") {{
          el.controlsSummaryText.textContent = `All 11 Lectures • ${{total}} Qs`;
        }} else {{
          const opt = el.lectureFilter.options[el.lectureFilter.selectedIndex];
          const name = opt ? opt.textContent.split(" (")[0] : `Lecture ${{state.filterLecture}}`;
          el.controlsSummaryText.textContent = `${{name}} • ${{total}} Qs`;
        }}
      }}

      let controlsOpenMobile = false;
      function toggleControls() {{
        controlsOpenMobile = !controlsOpenMobile;
        el.controlsBody.classList.toggle("is-open", controlsOpenMobile);
        el.controlsArrow.textContent = controlsOpenMobile ? "▲" : "▼";
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

      // Next / Prev Actions with smart scroll (NO jump to top)
      function goToPrev() {{
        if (state.currentIndex > 0) {{
          state.currentIndex--;
          renderQuestion();
          scrollQuestionIntoView();
        }}
      }}

      function goToNext() {{
        if (state.currentIndex < state.activeQuestions.length - 1) {{
          state.currentIndex++;
          renderQuestion();
          scrollQuestionIntoView();
        }}
      }}

      // Mobile Drawer Toggle
      function togglePaletteDrawer() {{
        state.paletteOpenMobile = !state.paletteOpenMobile;
        el.paletteBody.classList.toggle("is-open", state.paletteOpenMobile);
        el.palArrow.textContent = state.paletteOpenMobile ? "▲" : "▼";
      }}

      // Confirmation Modal Controller
      let onModalConfirmCallback = null;

      function showConfirmModal(opts) {{
        if (!el.confirmModal) return;
        if (el.modalIcon) el.modalIcon.textContent = opts.icon || "⚠️";
        if (el.modalTitle) el.modalTitle.textContent = opts.title || "Are you sure?";
        if (el.modalDesc) el.modalDesc.innerHTML = opts.desc || "";
        if (el.btnModalConfirm) {{
          el.btnModalConfirm.textContent = opts.confirmText || "Confirm";
          el.btnModalConfirm.classList.toggle("danger", !!opts.isDanger);
        }}
        onModalConfirmCallback = opts.onConfirm;

        if (typeof el.confirmModal.showModal === "function") {{
          el.confirmModal.showModal();
        }} else {{
          el.confirmModal.setAttribute("open", "");
        }}
      }}

      function closeModal() {{
        if (!el.confirmModal) return;
        if (typeof el.confirmModal.close === "function") {{
          el.confirmModal.close();
        }} else {{
          el.confirmModal.removeAttribute("open");
        }}
        onModalConfirmCallback = null;
      }}

      // Event Listeners Setup
      function setupListeners() {{
        el.themeBtn.addEventListener("click", toggleTheme);

        el.btnShuffleAll.addEventListener("click", () => {{
          const answeredCount = Object.keys(state.userAnswers).length;

          showConfirmModal({{
            icon: "🎲",
            title: "Shuffle All Questions?",
            desc: answeredCount > 0
              ? `You currently have <strong>${{answeredCount}} answered question${{answeredCount > 1 ? "s" : ""}}</strong>. Shuffling will re-randomize question order & choices, and <strong>reset your progress</strong>.`
              : "This will re-randomize both questions and choices (A–D) for a fresh practice session.",
            confirmText: "Shuffle & Restart",
            isDanger: false,
            onConfirm: () => {{
              state.shuffleQuestions = true;
              state.shuffleAnswers = true;
              el.checkShuffleQ.checked = true;
              el.checkShuffleA.checked = true;
              buildSession(true);
            }}
          }});
        }});

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
          const answeredCount = Object.keys(state.userAnswers).length;
          if (answeredCount === 0) {{
            alert("No progress to reset yet.");
            return;
          }}

          showConfirmModal({{
            icon: "🔄",
            title: "Reset Practice Progress?",
            desc: `This will clear all <strong>${{answeredCount}} answered question${{answeredCount > 1 ? "s" : ""}}</strong> and restart your score from 0.`,
            confirmText: "Reset Progress",
            isDanger: true,
            onConfirm: () => {{
              state.userAnswers = {{}};
              renderQuestion();
              renderPalette();
              updateStats();
            }}
          }});
        }});

        el.btnPrev.addEventListener("click", goToPrev);
        el.btnNext.addEventListener("click", goToNext);

        el.btnStarQ.addEventListener("click", toggleStar);
        if (el.btnTogglePalette) el.btnTogglePalette.addEventListener("click", togglePaletteDrawer);
        if (el.btnToggleControls) el.btnToggleControls.addEventListener("click", toggleControls);

        if (el.btnModalCancel) el.btnModalCancel.addEventListener("click", closeModal);
        if (el.btnModalConfirm) {{
          el.btnModalConfirm.addEventListener("click", () => {{
            const cb = onModalConfirmCallback;
            closeModal();
            if (cb) cb();
          }});
        }}
        if (el.confirmModal) {{
          el.confirmModal.addEventListener("click", (e) => {{
            const rect = el.confirmModal.getBoundingClientRect();
            const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height
              && rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
            if (!isInDialog) closeModal();
          }});
          el.confirmModal.addEventListener("cancel", () => {{
            onModalConfirmCallback = null;
          }});
        }}

        window.addEventListener("keydown", (e) => {{
          if (["1", "a", "A"].includes(e.key)) handleOptionSelect(0);
          else if (["2", "b", "B"].includes(e.key)) handleOptionSelect(1);
          else if (["3", "c", "C"].includes(e.key)) handleOptionSelect(2);
          else if (["4", "d", "D"].includes(e.key)) handleOptionSelect(3);
          else if (e.key === "ArrowLeft") goToPrev();
          else if (e.key === "ArrowRight") goToNext();
          else if (e.key.toLowerCase() === "s") toggleStar();
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
    print("Generated mobile-optimized standalone index.html successfully!")

if __name__ == "__main__":
    main()
