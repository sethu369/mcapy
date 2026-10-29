# Content brief (shared by all authors)

We are building "MCA Python Lab" – MCA Sem-1, MCA 102 A: Programming in Python.
You write ONE content file of real, runnable Python programs. Look at `content/schema.py` (helper `P(...)`).
Syllabus topic names live in `content/syllabus_topics.json` – each program's `topics=[...]` MUST use those EXACT strings,
and together the programs of a unit must cover EVERY topic of that unit (checker enforces this).

File layout (example):

    import sys; sys.path.insert(0, __file__.rsplit("/", 2)[0])   # so `schema` imports
    from schema import P
    PROGRAMS = [
      P(title="...", category="...", difficulty="Beginner", description="...",
        concepts=["print()"], filename="hello_world.py",
        code=r'''...python source...''',
        algorithm=["Step 1", "Step 2", "Step 3"],
        explanation="...", sample_input="", tags=["print"], topics=["Introduction to Python"]),
      ...
    ]

RULES
* The ORDER of PROGRAMS = program numbers (1..N). Follow the order of the numbered list in the requirement doc for your unit (one program per numbered item, in order; you may ADD extra programs at the END of the list, or where a topic is otherwise uncovered). Titles should be clear, e.g. "Check Whether a Number Is an Integer".
* Code: wrap with r'''...''' – so NEVER use ''' inside the code (use """ for docstrings). Python 3.13 compatible, beginner-friendly, meaningful names, comments where useful, try/except input validation for interactive programs, `if __name__ == "__main__":` only where natural. Each program is independent and a single file. Pure Python only except where the topic needs pandas/numpy (then list `deps=["pandas"]`/`["numpy"]` and say so in a comment at the top of the code: `# Requires: pip install numpy`).
* Interactive programs use input(): provide `sample_input` (newline-separated, one line per input() call) so the runner can execute them – the runner captures the REAL output as the sample output. Programs using sys.argv: provide `args=[...]`.
* Programs must terminate by themselves within a few seconds, with exit code 0 and WITHOUT needing a network, GUI or files outside the working dir (they run in a throw-away temp dir; SQLite programs may create files there or use ":memory:" – but prefer a file such as "students.db" then delete it at the end / or use :memory: where the lesson is not about files). Avoid output that changes run-to-run where possible (date/time programs are allowed to print the current date – fine – but prefer ones with a fixed date too).
* "Demonstrate infinite loops safely" = a `while True:` that is exited by a counter/break.
* Installation/terminal-command topics (e.g. Windows commands such as `py --version`, `where python`, `python -m pip install pandas`, `pip list`) : provide the commands as a program with kind="Terminal Commands" whose code is a `.py`-file made of comment lines / a Python script that *prints* the commands and explains them AND, where possible, runs the equivalent Python check (e.g. via sys/platform/subprocess). Keep these valid Python so they download as a real .py file. Clearly label Windows commands as comments starting with `# TERMINAL:` or `# CMD>`.
* explanation: 3-6 sentences in simple language: what it does, how the logic works, important functions/statements, how input is processed, how output is produced. algorithm: 3-8 steps. description: 1-2 sentences. tags: 3-6 lowercase search words. concepts: 2-5 items.
* difficulty: mix Beginner / Intermediate / Advanced sensibly (most Beginner/Intermediate; Advanced for management apps, data structures, DB apps, etc.).
* kind: "Demonstration" (default), "Interactive" (uses input), "Application" (mini-app), "Terminal Commands".
* Python truths: do NOT claim Python has Java-style method overloading – demonstrate default args / *args / singledispatch-like techniques. Abstract classes via `abc`; deque via `collections.deque`; for arrays explain `array` module vs NumPy `ndarray` in explanation/comments.
* Write each file in several chunks if long (create the file then append with additional edits) – but keep ONE `PROGRAMS = [...]` list.

VERIFY: run `python3 scripts/build_data.py --unit N` (from /home/claude/mca-python-lab). It parses and EXECUTES every program and prints PROBLEMS (syntax errors, non-zero exits, short explanations, uncovered syllabus topics, duplicate filenames). Fix until it reports `PROBLEMS: 0`. Also eyeball a few sample outputs by temporarily printing them (the runner writes nothing in --unit mode). Don't touch other units' files, schema.py, or scripts.
Final reply: just the count of programs and the PROBLEMS line (brief).
