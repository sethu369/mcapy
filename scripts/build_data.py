#!/usr/bin/env python3
"""Validate + execute every program, capture REAL output, emit src/data/*.json.

Usage: python3 scripts/build_data.py [--strict]
"""
import ast, importlib.util, json, os, subprocess, sys, tempfile, re, shutil, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "content"))
UNITS = {1: "Introduction to Python", 2: "Data Types and Operators",
         3: "Control Statements and Arrays",
         4: "Lists, Tuples, Dictionaries and Functions",
         5: "OOPS and Data Structures"}
FOLDERS = {1: "Unit_1_Introduction_to_Python", 2: "Unit_2_Data_Types_and_Operators",
           3: "Unit_3_Control_Statements_and_Arrays",
           4: "Unit_4_Lists_Tuples_Dictionaries_Functions",
           5: "Unit_5_OOPS_Data_Structures_Database"}

def load(path, attr):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, attr)

def run(code, stdin, args):
    d = tempfile.mkdtemp(prefix="mcarun_")
    try:
        f = os.path.join(d, "prog.py")
        open(f, "w").write(code)
        r = subprocess.run([sys.executable, "-I" if False else "-u", f, *args], input=stdin, capture_output=True,
                           text=True, timeout=20, cwd=d)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -9, "", "TIMEOUT"
    finally:
        shutil.rmtree(d, ignore_errors=True)

def main():
    only = int(sys.argv[sys.argv.index("--unit")+1]) if "--unit" in sys.argv else None
    problems = []
    out, practice = [], []
    for u in ([only] if only else ([] if only == 0 else range(1, 6))):
        path = os.path.join(ROOT, "content", "programs", f"unit{u}.py")
        if not os.path.exists(path):
            problems.append(f"missing {path}"); continue
        progs = load(path, "PROGRAMS")
        seen = set()
        for i, p in enumerate(progs, 1):
            pid = f"unit{u}-program-{i:03d}"
            if p["filename"] in seen: problems.append(f"{pid}: duplicate filename {p['filename']}")
            seen.add(p["filename"])
            if not re.fullmatch(r"[a-z0-9_]+\.py", p["filename"]): problems.append(f"{pid}: bad filename {p['filename']}")
            try: ast.parse(p["code"])
            except SyntaxError as e: problems.append(f"{pid} {p['filename']}: SYNTAX {e}"); continue
            rc, so, se = run(p["code"], p["sampleInput"], p["args"])
            if rc != 0 and p["kind"] != "Terminal Commands":
                problems.append(f"{pid} {p['filename']}: exit {rc}: {se.strip().splitlines()[-1:] }")
            if p['category'] in ('Data Structures','Database Connectivity') and p['difficulty']=='Beginner': p['difficulty']='Intermediate'
            p = dict(p); p.update(id=pid, unit=u, number=i, unitTitle=UNITS[u],
                sampleOutput=so.rstrip("\n") if so.strip() else (se.strip() if rc else ""),
                exitCode=rc, verified=(rc == 0))
            if len(p["algorithm"]) < 3: problems.append(f"{pid}: algorithm too short")
            if len(p["explanation"]) < 80: problems.append(f"{pid}: explanation too short")
            if not p["topics"]: problems.append(f"{pid}: no topics")
            out.append(p)
    ppath = os.path.join(ROOT, "content", "programs", "practice.py")
    if os.path.exists(ppath) and (only is None or only == 0):
        for i, q in enumerate(load(ppath, "PRACTICE"), 1):
            try: ast.parse(q["solution"])
            except SyntaxError as e: problems.append(f"practice-{i}: SYNTAX {e}"); continue
            rc, so, se = run(q["solution"], q.get("sampleInput", ""), q.get("args", []))
            if rc != 0: problems.append(f"practice-{i}: exit {rc} {se.strip().splitlines()[-1:]}")
            q = dict(q); q.update(id=f"practice-{i:03d}", expectedOutput=so.rstrip("\n"))
            practice.append(q)
    # syllabus coverage
    topics = json.load(open(os.path.join(ROOT, "content", "syllabus_topics.json")))
    covered = {}
    for p in out:
        for t in p["topics"]: covered.setdefault((p["unit"], t), []).append(p["id"])
    for u, ts in topics.items():
        if only is not None and int(u) != only: continue
        for t in ts:
            if (int(u), t) not in covered: problems.append(f"UNCOVERED syllabus topic: unit {u}: {t}")
    if only is not None:
        print("unit-only check:", len(out), "programs"); print("PROBLEMS:", len(problems)); [print(" -", x) for x in problems]; return 1 if problems else 0
    json.dump(out, open(os.path.join(ROOT, "src", "data", "programs.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(practice, open(os.path.join(ROOT, "src", "data", "practice.json"), "w"), indent=1, ensure_ascii=False)
    per = {u: sum(1 for p in out if p["unit"] == u) for u in range(1, 6)}
    print("programs:", len(out), per, "practice:", len(practice))
    print("PROBLEMS:", len(problems))
    for x in problems: print(" -", x)
    return 1 if problems else 0
if __name__ == "__main__": sys.exit(main())
