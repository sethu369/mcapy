# MCA Python Lab - MCA 1st Semester, MCA 102 A: Programming in Python

A complete Claymorphism React website with **291 runnable Python programs** across the five syllabus units,
60 practice questions, 26 concept notes, search, ZIP downloads and a full program-management (CRUD) system.

## Just use it
Open `MCA_Python_Lab.html` in Chrome/Edge/Firefox (double-click). No server or internet is needed
(Google Fonts are optional). Your edits, drafts, trash, versions, favorites and progress are saved in the browser.
Downloads (single .py, unit ZIP, all-programs ZIP) work from a normal browser tab.

## Develop
    npm install
    npm run dev          # local dev server
    npm run build        # builds dist/index.html (single self-contained file)

## Program collection
Source of truth: `content/programs/unit1.py … unit5.py` (+ `practice.py`).
    python3 scripts/build_data.py      # parses + RUNS every program, captures real sample output,
                                       # checks every syllabus topic is covered, writes src/data/*.json
Run `pip install -r requirements.txt` first so the numpy/pandas programs can run.

## Stack
React, Tailwind CSS, lucide-react, JSZip, Vite (single-file build). Python programs are plain .py files.

## Notes
* Program management is local to the browser and not protected by an account system.
* The editor stores code as text and never executes it; Python syntax is NOT validated (no backend).
* Programs are for educational purposes.
