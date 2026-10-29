import JSZip from 'jszip';
import { UNITS, COURSE, syllabusText } from '../data/syllabus.js';
import { published } from './store.js';
import { detectDeps } from './python.js';

export const ROOT = 'MCA_Python_Programs';
const pad = (n, w = 3) => String(n ?? 0).padStart(w, '0');
export const stem = (f) => f.replace(/\.py$/i, '');
export const pathFor = (p) => `${UNITS[p.unit - 1].folder}/program_${pad(p.number)}_${stem(p.filename)}.py`;
export function downloadBlob(blob, name) {
  const url = URL.createObjectURL(blob); const a = document.createElement('a');
  a.href = url; a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 4000);
}
export const downloadPython = (p) => downloadBlob(new Blob([p.code], { type: 'text/x-python;charset=utf-8' }), p.filename);
export const downloadText = (text, name, type = 'text/plain') => downloadBlob(new Blob([text], { type: type + ';charset=utf-8' }), name);

export const requirementsFor = (progs) => {
  const set = new Set(); progs.forEach((p) => { (p.deps || []).forEach((d) => set.add(d)); detectDeps(p.code).forEach((d) => set.add(d)); });
  return [...set].sort();
};
export function readmeText(progs, scope) {
  const per = UNITS.map((u) => ({ u, n: progs.filter((p) => p.unit === u.n).length })).filter((x) => x.n);
  const reqs = requirementsFor(progs);
  return `# MCA Python Lab - ${scope}
${COURSE.semester} | ${COURSE.code}: ${COURSE.name}

Generated on ${new Date().toLocaleString()} from the MCA Python Lab website.
Total programs in this archive: ${progs.length}

These Python programs are for educational purposes (lab practice and exam preparation).

## Folder structure
${ROOT}/
  README.md              this file
  syllabus.txt           the course syllabus
  MANIFEST.md / manifest.json   list of every program, its unit and file
  SAMPLE_OUTPUTS.md      sample input and output captured for each program
  requirements.txt       third-party packages (only if needed)
${per.map(({ u, n }) => `  ${u.folder}/   (${n} programs)  program_NNN_name.py`).join('\n')}

## How to run a program (Windows)
1. Install Python from https://www.python.org/downloads/ (tick "Add python.exe to PATH").
2. Check the installation:      py --version      or      python --version
3. Open a terminal in this folder and run:
       python ${UNITS[(per[0]?.u.n || 1) - 1].folder}\\program_001_example.py
   (Replace the path with the file you want to run.)
4. Programs that use input() wait for you to type values. Programs that use command-line
   arguments (sys.argv) are run like:  python program_007_name.py 10 20

## Installing required packages
${reqs.length ? `Some programs need third-party packages:\n    python -m pip install -r requirements.txt\n(packages: ${reqs.join(', ')})` : 'None of the programs in this archive need third-party packages.'}
Verify an installation with:  python -m pip list   or   python -m pip show pandas

## Units
${per.map(({ u, n }) => `- Unit ${u.n}: ${u.title} - ${n} programs`).join('\n')}
`;
}
const manifestRows = (progs) => progs.map((p) => ({ id: p.id, unit: p.unit, unitTitle: UNITS[p.unit - 1].title, number: p.number, title: p.title, category: p.category, difficulty: p.difficulty, file: `${ROOT}/${pathFor(p)}`, dependencies: p.deps || [], version: p.version || 1, updatedAt: p.updatedAt }));
export function manifestMd(progs) {
  let s = '# Manifest\n\n| Unit | No. | Title | Category | Difficulty | File |\n|---|---|---|---|---|---|\n';
  progs.forEach((p) => { s += `| ${p.unit} | ${p.number} | ${p.title.replace(/\|/g, '/')} | ${p.category} | ${p.difficulty} | ${pathFor(p)} |\n`; }); return s;
}
export function samplesMd(progs) {
  return '# Sample inputs and outputs\n\nOutputs were captured by actually running the original programs. Edited or user-added programs may show text written by the author.\n\n' +
    progs.map((p) => `## Unit ${p.unit} - #${p.number} ${p.title}\nFile: \`${pathFor(p)}\`\n${p.sampleInput ? `\nInput:\n\`\`\`\n${p.sampleInput}\n\`\`\`\n` : ''}${p.args?.length ? `\nCommand-line arguments: \`${p.args.join(' ')}\`\n` : ''}\nOutput:\n\`\`\`\n${p.sampleOutput || '(no output recorded)'}\n\`\`\`\n`).join('\n');
}
const sortProgs = (a, b) => a.unit - b.unit || a.number - b.number;
/** Build a ZIP from the LATEST saved data (never a pre-built archive). */
export async function buildZip(progs, scope = 'All Programs', onProgress) {
  const list = [...progs].sort(sortProgs); const zip = new JSZip(); const root = zip.folder(ROOT);
  const used = new Set();
  list.forEach((p) => { let path = pathFor(p), i = 2; while (used.has(path)) path = pathFor(p).replace(/\.py$/, `_${i++}.py`); used.add(path); root.file(path, p.code); });
  root.file('README.md', readmeText(list, scope));
  root.file('syllabus.txt', syllabusText());
  root.file('MANIFEST.md', manifestMd(list));
  root.file('manifest.json', JSON.stringify({ course: `${COURSE.code}: ${COURSE.name}`, generatedAt: new Date().toISOString(), totalPrograms: list.length, programs: manifestRows(list) }, null, 2));
  root.file('SAMPLE_OUTPUTS.md', samplesMd(list));
  const reqs = requirementsFor(list);
  root.file('requirements.txt', (reqs.length ? '# Third-party packages used by the programs\n' + reqs.join('\n') : '# No third-party packages are required (standard library only)') + '\n');
  const blob = await zip.generateAsync({ type: 'blob', compression: 'DEFLATE', compressionOptions: { level: 6 } }, (m) => onProgress && onProgress(Math.round(m.percent)));
  return { blob, count: list.length };
}
export const zipNameFor = (kind, n) => (kind === 'all' ? 'MCA_Python_Programs.zip' : kind === 'unit' ? `MCA_Python_Unit_${n}_Programs.zip` : 'MCA_Python_Selected_Programs.zip');
export const publishedSorted = () => published().sort(sortProgs);
export function readmeSiteText() {
  const progs = published();
  return `# MCA Python Lab
MCA Python Lab is an educational website for ${COURSE.semester}, ${COURSE.code}: ${COURSE.name}.
It provides syllabus-based Python practical programs with explanations, sample output and downloadable source code.

## Course details
${COURSE.semester} - ${COURSE.code}: ${COURSE.name}
${UNITS.map((u) => `- Unit ${u.n}: ${u.title} (${progs.filter((p) => p.unit === u.n).length} programs)`).join('\n')}

Total programs currently in the library: ${progs.length}

## Program collection
Programs are grouped by unit and category. Use "Download All Programs" to get MCA_Python_Programs.zip.

## How to run Python programs
1. Install Python for Windows from python.org (tick "Add python.exe to PATH").
2. Verify: py --version
3. Run a program: python program_name.py

## How to install required packages
    python -m pip install pandas numpy
Verify with: python -m pip list

These programs are for educational purposes only.
`;
}
