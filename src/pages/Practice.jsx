import { useMemo, useState } from 'react';
import { Eye, EyeOff, CheckCircle2, Dumbbell } from 'lucide-react';
import practice from '../data/practice.json';
import { useStore, togglePracticeDone } from '../lib/store.js';
import { replaceQuery } from '../lib/router.js';
import { PageTitle, UnitBadge, DiffBadge, Empty } from '../components/ui.jsx';
import { UnitFilter, DifficultyFilter, SelectFilter } from '../components/Filters.jsx';
import CodeViewer from '../components/CodeViewer.jsx';

export default function Practice({ route }) {
  const s = useStore(); const { unit = 'all', diff = 'all', topic = 'all', q = '' } = route.q; const [shown, setShown] = useState({});
  const upd = (p) => replaceQuery('/practice', { unit, diff, topic, q, ...p });
  const topics = useMemo(() => [...new Set(practice.filter((x) => unit === 'all' || String(x.unit) === unit).map((x) => x.topic))].sort(), [unit]);
  const list = practice.filter((x) => (unit === 'all' || String(x.unit) === unit) && (diff === 'all' || x.difficulty === diff) && (topic === 'all' || x.topic === topic) && (!q || `${x.title} ${x.description} ${x.topic}`.toLowerCase().includes(q.toLowerCase())));
  const done = practice.filter((x) => s.prefs.practiceDone.includes(x.id)).length;
  return (
    <div><PageTitle title="Practice Programs" sub={`${practice.length} university-style questions across all five units. Try first, then reveal the solution. No sign-in needed.`} />
      <div className="clay p-5 mb-6 grid gap-5">
        <div className="grid md:grid-cols-[1fr_16rem] gap-4"><div><label className="label" htmlFor="p-q">Search practice questions</label><div className="clay-inset px-4 py-2"><input id="p-q" value={q} onChange={(e) => upd({ q: e.target.value })} placeholder="Search practice questions…" className="bg-transparent outline-none w-full font-bold text-sm" /></div></div>
          <SelectFilter id="p-topic" label="Topic" value={topic} onChange={(v) => upd({ topic: v })} options={topics} /></div>
        <div className="flex flex-wrap gap-6"><UnitFilter value={unit} onChange={(v) => upd({ unit: v, topic: 'all' })} /><DifficultyFilter value={diff} onChange={(v) => upd({ diff: v })} /></div>
      </div>
      <p className="font-extrabold mb-4" aria-live="polite">{list.length} of {practice.length} questions · {done} solved by you</p>
      {list.length === 0 ? <Empty title="No questions match" /> : <div className="grid lg:grid-cols-2 gap-5">{list.map((x, i) => {
        const open = shown[x.id]; const solved = s.prefs.practiceDone.includes(x.id);
        return (
          <article key={x.id} className={`clay p-5 space-y-3 unit-${x.unit}`}>
            <div className="flex flex-wrap items-center gap-2"><span className="chip bg-ink text-white">Q{i + 1}</span><UnitBadge n={x.unit} /><span className="chip">{x.topic}</span><DiffBadge d={x.difficulty} />{solved && <span className="chip bg-mint-light text-mint-dark"><CheckCircle2 size={12} />Solved</span>}</div>
            <h2 className="font-extrabold text-lg">{x.title}</h2><p className="font-semibold">{x.description}</p>
            {x.hint && <p className="text-sm font-semibold text-soft"><b>Hint:</b> {x.hint}</p>}
            <div className="grid sm:grid-cols-2 gap-3"><div><p className="label">Sample input{x.args?.length ? ' / arguments' : ''}</p><pre className="codebox code-font p-3 whitespace-pre-wrap min-h-[2.5rem]">{[x.args?.length ? `python solution.py ${x.args.join(' ')}` : '', x.sampleInput].filter(Boolean).join('\n') || '(none)'}</pre></div>
              <div><p className="label">Expected output</p><pre className="codebox code-font p-3 whitespace-pre-wrap max-h-48 overflow-auto min-h-[2.5rem]">{x.expectedOutput || '(no output)'}</pre></div></div>
            <div className="flex flex-wrap gap-2"><button className="clay-btn clay-primary btn-sm" aria-expanded={!!open} onClick={() => setShown({ ...shown, [x.id]: !open })}>{open ? <EyeOff size={15} /> : <Eye size={15} />}{open ? 'Hide Solution' : 'Reveal Solution'}</button>
              <button className="clay-btn btn-sm" aria-pressed={solved} onClick={() => togglePracticeDone(x.id)}><CheckCircle2 size={15} />{solved ? 'Unmark solved' : 'Mark as solved'}</button></div>
            {open && <CodeViewer code={x.solution} filename={`practice_${x.id.split('-')[1]}.py`} title="Solution" />}
          </article>); })}</div>}
    </div>
  );
}
