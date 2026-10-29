import { Target, Layers, ShieldCheck, Download } from 'lucide-react';
import { COURSE, UNITS } from '../data/syllabus.js';
import { PageTitle } from '../components/ui.jsx';
import { downloadText, readmeSiteText } from '../lib/zip.js';

const FEATURES = ['Syllabus-based library of runnable Python programs with real sample output', 'Instant search across titles, descriptions, concepts, tags and source code', 'Filters by unit, difficulty, topic and program type', 'Copy and download individual .py files', 'Download all programs, a single unit or a hand-picked selection as a ZIP', 'Create, edit, delete, import and export your own programs', 'Drafts, Trash and version history with restore', 'Favorites, recently viewed and progress tracking saved in your browser', 'Concept notes and practice questions with solutions'];
const OBJ = ['Write and run basic Python programs with input and output', 'Use data types, operators and control statements correctly', 'Work with arrays, lists, tuples, sets and dictionaries', 'Define functions and understand how arguments are passed', 'Apply object-oriented programming, exceptions and simple data structures', 'Handle dates and times and store data using SQLite'];
export default function About() {
  return (
    <div className="space-y-6 max-w-5xl"><PageTitle title="About MCA Python Lab" />
      <p className="clay p-6 sm:p-8 text-xl font-semibold leading-relaxed">MCA Python Lab is an educational website created to help MCA Semester 1 students learn Python programming through syllabus-based practical programs, explanations, examples, and downloadable source code.</p>
      <div className="grid md:grid-cols-2 gap-6">
        <section className="clay p-6"><h2 className="font-extrabold text-xl mb-3 flex gap-2 items-center"><Target className="text-primary" />Course information</h2><dl className="space-y-2 font-semibold"><div><dt className="label">Semester</dt><dd>Semester 1 (MCA)</dd></div><div><dt className="label">Course</dt><dd>{COURSE.code}: {COURSE.name}</dd></div><div><dt className="label">Five syllabus units</dt><dd><ol className="list-decimal pl-5">{UNITS.map((u) => <li key={u.n}>{u.title}</li>)}</ol></dd></div></dl></section>
        <section className="clay p-6"><h2 className="font-extrabold text-xl mb-3 flex gap-2 items-center"><Layers className="text-primary" />Website purpose</h2><p className="font-semibold">To give students one place to find programs by syllabus unit, understand the logic of each, practise for lab examinations, and keep their own practical collection organised — Python only.</p>
          <h3 className="label mt-5">Learning objectives</h3><ul className="list-disc pl-5 font-semibold space-y-1">{OBJ.map((o) => <li key={o}>{o}</li>)}</ul></section>
      </div>
      <section className="clay p-6"><h2 className="font-extrabold text-xl mb-3">Website features</h2><ul className="grid sm:grid-cols-2 gap-x-8 gap-y-2 font-semibold list-disc pl-5">{FEATURES.map((f) => <li key={f}>{f}</li>)}</ul>
        <button className="clay-btn mt-5" onClick={() => downloadText(readmeSiteText(), 'README.md', 'text/markdown')}><Download size={16} />Download README.md</button></section>
      <section className="clay-tint p-5 flex gap-3"><ShieldCheck className="text-mint-dark shrink-0" /><p className="font-bold text-ink/90"><b>Disclaimer:</b> The programs are provided for educational purposes. Check them against your own syllabus and instructor's guidance. Data you add, edit or delete is stored only in your browser; there is no account system.</p></section>
    </div>
  );
}
