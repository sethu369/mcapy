"""Shared helper used by every content/programs/unitN.py file.

Each program is declared with P(...). Real sample output is produced later by
scripts/build_data.py, which actually RUNS the code with `sample_input` / `args`.
"""

def P(title, category, difficulty, description, concepts, filename, code,
      algorithm, explanation, sample_input="", args=None, tags=None, topics=None,
      deps=None, kind="Demonstration"):
    """
    title        : str   - program title
    category    : str   - sub-topic heading (e.g. "Data Types", "Loops")
    difficulty  : "Beginner" | "Intermediate" | "Advanced"
    description : str   - 1-2 sentence summary
    concepts    : list[str] - Python concepts used (e.g. ["input", "int()"])
    filename    : str   - snake_case .py file name, unique inside the unit
    code        : str   - complete, runnable Python 3 source (use a raw ''' string)
    algorithm   : list[str] - 3-8 clear steps
    explanation : str   - simple-language explanation (what/how/key functions/input/output)
    sample_input: str   - text fed to stdin when the program is run (newline separated)
    args        : list[str] | None - command-line arguments for sys.argv programs
    tags        : list[str] - search tags
    topics      : list[str] - EXACT syllabus topic names this program covers
    deps        : list[str] | None - pip packages needed e.g. ["pandas"], ["numpy"]
    kind        : "Demonstration" | "Interactive" | "Application" | "Terminal Commands"
    """
    return dict(title=title, category=category, difficulty=difficulty,
                description=description, concepts=concepts, filename=filename,
                code=code.strip("\n") + "\n", algorithm=algorithm,
                explanation=explanation, sampleInput=sample_input,
                args=args or [], tags=tags or [], topics=topics or [],
                deps=deps or [], kind=kind)
