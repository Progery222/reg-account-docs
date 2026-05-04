# Agent Instructions — Only-chats

## Project Overview

Static knowledge base site generated from Telegram chat exports. Content is manuals/guides for Instagram/TikTok/Facebook account operations. Built as a single-page HTML app with vanilla JS/CSS, deployed to Vercel.

## Architecture

```
/
├── result.json              # Telegram chat export (source of truth)
├── chats/                   # Media files from Telegram export
│   └── chat_562953382643143/topic_1019/
│       ├── photos/
│       ├── video_files/
│       └── stickers/
├── messages.html            # Raw Telegram HTML export (not used for site)
├── css/, js/, images/       # Legacy Telegram export assets
├── site/                    # Build scripts and generated site
│   ├── build.py             # Main generator (v2 — structured guides)
│   ├── build2.py, build3.py # Iterations/experiments
│   ├── generate.py          # Auto-generator from result.json (v1)
│   ├── prepare_deploy.py    # Copies site/ → deploy/, fixes paths
│   ├── fix_paths.py         # Path fixing utility
│   ├── patch.py–patch4.py   # Content patches
│   ├── check.py, check3.py  # Validation scripts
│   ├── final_audit.py       # Final verification
│   ├── scraped_data.json    # Curated text summaries from external guides
│   ├── sizes.py             # Media size checker
│   └── index.html, style.css, script.js  # Generated site output
└── deploy/                  # Vercel deployment directory (git repo)
    ├── index.html           # Copied from site/
    ├── style.css, script.js
    ├── chats/               # Media copied here with fixed paths
    ├── vercel.json          # Static site config
    └── .git/                # Separate git repo for deployment
```

## Build Workflow

1. **Edit content** → Modify `site/build.py` or `site/scraped_data.json`
2. **Generate site** → Run the appropriate build script in `site/`
3. **Prepare deploy** → Run `site/prepare_deploy.py` to copy to `deploy/`
4. **Deploy** → Push `deploy/` to GitHub/Vercel

### Key Scripts

```bash
# Generate the site (from site/ directory)
cd site
python build.py        # v2 structured guides (preferred)
python generate.py     # v1 auto-from-json

# Prepare for deployment (fixes paths, copies media)
python prepare_deploy.py

# The deploy/ directory is a separate git repo — commit and push there
```

## Critical Context

- **`prepare_deploy.py` has hardcoded absolute Windows paths** pointing to `C:\Users\Alex\Downloads\Telegram Desktop\ChatExport_2026-05-01\`. If the project is moved, this script must be updated.
- **No dependency manager** — pure Python stdlib + static HTML/CSS/JS. No `requirements.txt`, `package.json`, or `pyproject.toml`.
- **Two generators exist**: `build.py` (v2, manual structured content) and `generate.py` (v1, auto-parsed from `result.json`). `build.py` is the actively maintained version that produces the current site.
- **Media paths differ between `site/` and `deploy/`**: `site/index.html` uses `../chats/...`, while `deploy/index.html` uses `chats/...` (fixed by `prepare_deploy.py`).
- **Deployment target**: Vercel static hosting. `vercel.json` disables build step and sets cache headers.
- **Source data**: `result.json` is a Telegram Desktop chat export. Do not edit it manually — it is the raw export.

## Code Style

- Python scripts use UTF-8 encoding declarations (`# -*- coding: utf-8 -*-`)
- HTML/CSS/JS are hand-written; no bundler or framework
- Content is in Russian

## Common Gotchas

- `deploy/` is a **separate git repository** from the project root. Do not confuse them.
- If media files are missing after generation, check that `chats/` directory exists and `prepare_deploy.py` ran successfully.
- The `build.py` script writes only the first part of `index.html` (it is incomplete at line 258 — `print("Part 1 written...")`). There may be a `build3.py` or manual step that completes the file.
- `scraped_data.json` contains curated text from external Telegraph/Teletype guides and is imported by `build.py`.
