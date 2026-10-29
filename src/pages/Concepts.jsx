import { useMemo, useState } from 'react';
import { BookOpen, ChevronDown } from 'lucide-react';
import { CONCEPTS, conceptPrograms } from '../data/concepts.js';
import { useStore, published } from '../lib/store.js';
import { href, replaceQuery } from '../lib/router.js';
import { PageTitle, UnitBadge } from '../components/ui.jsx';
import { UnitFilter } from '../components/Filters.jsx';
import { highlightLine } from '../lib/python.js';

const Code = ({ code }) => <pre className="codebox code-font p-4 overflow-auto" dangerouslySetInnerHTML={{ __html: highlightLine(code) }} />;
export default function Concepts({ route }) {
  const s = useStore(); const progs = published(s); const open = route.q.open; const unit = route.q.unit || 'all'; const [q, setQ] = useState('');
  const list = CONCEPTS.filter((c) => (unit === 'all' || String(c.unit) === unit) && (!q || (c.name + c.explain).toLowerCase().includes(q.toLowerCase())));
  return (
    <div><PageTitle title="Python Concepts" sub="Short notes with syntax, a runnable example and links to the related practical programs." />
      <div className="clay p-5 mb-6 grid md:grid-cols-[1fr_auto] gap-4 items-end">
        <div><label className="label" htmlFor="c-q">Search concepts</label><div className="clay-inset px-4 py-2"><input id="c-q" value={q} onChange={(e) => setQ(e.target.value)} placeholder="e.g. inheritance, loops, sqlite…" className="bg-transparent outline-none w-full font-bold text-sm" /></div></div>
        <UnitFilter value={unit} onChange={(v) => replaceQuery('/concepts', { unit: v, open })} />
      </div>
      <p className="font-extrabold mb-4">{list.length} concepts</p>
      <div className="space-y-4">{list.map((c) => {
        const isOpen = open === c.slug; const rel = conceptPrograms(c, progs);
        return (
          <article key={c.slug} id={c.slug} className={`clay p-5 unit-${c.unit}`}>
            <h2><button className="w-full flex items-center justify-between gap-3 text-left" aria-expanded={isOpen} aria-controls={`c-${c.slug}`} onClick={() => replaceQuery('/concepts', { unit: unit === 'all' ? '' : unit, open: isOpen ? '' : c.slug })}>
              <span className="flex items-center gap-3 flex-wrap"><span className="clay-sm w-10 h-10 grid place-items-center !rounded-2xl" style={{ color: 'var(--u)' }}><BookOpen size={19} /></span><span className="text-xl font-extrabold">{c.name}</span><UnitBadge n={c.unit} /></span>
              <ChevronDown className={`transition ${isOpen ? 'rotate-180' : ''}`} /></button></h2>
            {isOpen && <div id={`c-${c.slug}`} className="mt-5 grid lg:grid-cols-2 gap-5">
              <div className="space-y-4"><p className="font-semibold leading-relaxed">{c.explain}</p><div><p className="label">Syntax</p><Code code={c.syntax} /></div></div>
              <div className="space-y-4"><div><p className="label">Python example</p><Code code={c.example} /></div></div>
              <div className="lg:col-span-2"><p className="label">Related programs ({rel.length})</p>{rel.length === 0 ? <p className="font-semibold text-soft">No matching program in the current collection.</p> : <ul className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3">{rel.map((p) => <li key={p.id}><a className="clay-sm p-3 block font-bold text-sm hover:text-primary h-full" href={href(`/program/${p.id}`)}><span className="text-xs text-soft block">Unit {p.unit} · #{p.number}</span>{p.title}</a></li>)}</ul>}</div>
            </div>}
          </article>); })}</div>
    </div>
  );
}
