import { Download } from 'lucide-react';
import { COURSE, UNITS, syllabusText } from '../data/syllabus.js';
import { PageTitle } from '../components/ui.jsx';
import { downloadText } from '../lib/zip.js';
import { href } from '../lib/router.js';
import { useStore, published } from '../lib/store.js';

export function SyllabusViewer() {
  const s = useStore(); const progs = published(s);
  return (
    <div className="space-y-6">{UNITS.map((u) => (
      <section key={u.n} className={`clay p-6 sm:p-8 unit-${u.n}`} aria-labelledby={`syl-${u.n}`}>
        <div className="flex flex-wrap items-center justify-between gap-3 mb-4"><h2 id={`syl-${u.n}`} className="text-2xl font-extrabold flex items-center gap-3"><span className="w-11 h-11 rounded-2xl grid place-items-center text-white" style={{ background: 'var(--u)' }}>{u.n}</span>UNIT {u.n}</h2>
          <a className="clay-btn btn-sm" href={href(`/unit/${u.n}`)}>{progs.filter((p) => p.unit === u.n).length} programs →</a></div>
        <div className="space-y-3 text-lg font-semibold leading-relaxed">{u.syllabus.map((b, i) => <div key={i}>{b.head && <p className="font-extrabold">{b.head}</p>}{b.text && <p className="text-ink/90">{b.text}</p>}</div>)}</div>
      </section>))}</div>
  );
}
export default function Syllabus() {
  return (<div><PageTitle title={COURSE.semester} sub={`${COURSE.code}: ${COURSE.name}`}><button className="clay-btn" onClick={() => downloadText(syllabusText(), 'syllabus.txt')}><Download size={16} />Download syllabus.txt</button></PageTitle><SyllabusViewer /></div>);
}
