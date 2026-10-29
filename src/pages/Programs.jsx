import { useMemo, useState } from 'react';
import { SlidersHorizontal, SearchX, FolderArchive, CheckSquare, Plus } from 'lucide-react';
import { useStore, published } from '../lib/store.js';
import { searchPrograms } from '../lib/search.js';
import { replaceQuery, href } from '../lib/router.js';
import { PageTitle, Empty } from '../components/ui.jsx';
import { UnitFilter, DifficultyFilter, SelectFilter } from '../components/Filters.jsx';
import { ProgramCard } from '../components/Cards.jsx';
import { DownloadAllButton, DownloadUnitButton, runZip } from '../components/actions.jsx';
import { UNITS } from '../data/syllabus.js';

const PAGE = 24;
export default function Programs({ route, fixedUnit }) {
  const s = useStore(); const base = fixedUnit ? `/unit/${fixedUnit}` : '/programs';
  const q = route.q.q || '', unit = fixedUnit ? String(fixedUnit) : route.q.unit || 'all', diff = route.q.diff || 'all', cat = route.q.cat || 'all', kind = route.q.kind || 'all';
  const [limit, setLimit] = useState(PAGE), [showF, setShowF] = useState(false), [selMode, setSelMode] = useState(false), [sel, setSel] = useState([]);
  const all = published(s);
  const upd = (patch) => { setLimit(PAGE); replaceQuery(base, { q, unit: fixedUnit ? '' : unit, diff, cat, kind, ...patch }); };
  const scoped = fixedUnit ? all.filter((p) => p.unit === fixedUnit) : all;
  const counts = useMemo(() => { const c = { all: all.length }; all.forEach((p) => { c[p.unit] = (c[p.unit] || 0) + 1; }); return c; }, [all]);
  const cats = useMemo(() => [...new Set(scoped.filter((p) => unit === 'all' || String(p.unit) === unit).map((p) => p.category))].sort(), [scoped, unit]);
  const kinds = useMemo(() => [...new Set(all.map((p) => p.kind))], [all]);
  const bySearch = useMemo(() => searchPrograms(scoped, q), [scoped, q]);
  const list = bySearch.filter((p) => (unit === 'all' || String(p.unit) === unit) && (diff === 'all' || p.difficulty === diff) && (cat === 'all' || p.category === cat) && (kind === 'all' || p.kind === kind));
  const sorted = q ? list : [...list].sort((a, b) => a.unit - b.unit || (a.number || 0) - (b.number || 0));
  const u = fixedUnit ? UNITS[fixedUnit - 1] : null;
  const toggle = (id) => setSel((x) => (x.includes(id) ? x.filter((i) => i !== id) : [...x, id]));
  const filtersActive = q || diff !== 'all' || cat !== 'all' || kind !== 'all' || (!fixedUnit && unit !== 'all');
  return (
    <div className={u ? `unit-${u.n}` : ''}>
      <PageTitle title={u ? `Unit ${u.n}: ${u.title}` : 'All Python Programs'} sub={u ? u.desc : `Browse, search, copy and download every program in the library.`}>
        <a className="clay-btn clay-mint" href={href('/new', fixedUnit ? { unit: fixedUnit } : undefined)}><Plus size={18} />Add Program</a>
        {u ? <DownloadUnitButton n={u.n} /> : <DownloadAllButton />}
      </PageTitle>
      <p className="font-extrabold mb-4" aria-live="polite">{filtersActive ? `${sorted.length} of ${scoped.length} programs match` : `Total programs: ${scoped.length}`}{q && <span className="text-soft"> for “{q}”</span>}</p>
      <div className="grid lg:grid-cols-[18rem_1fr] gap-6 items-start">
        <aside aria-label="Filters" className="lg:sticky lg:top-24">
          <button className="clay-btn w-full lg:hidden mb-3" aria-expanded={showF} onClick={() => setShowF(!showF)}><SlidersHorizontal size={16} />Filters & search</button>
          <div className={`clay p-5 space-y-5 ${showF ? '' : 'hidden'} lg:block`}>
            <div><label className="label" htmlFor="list-search">Search</label><ListSearch q={q} onChange={(v) => upd({ q: v })} /></div>
            {!fixedUnit && <UnitFilter value={unit} onChange={(v) => upd({ unit: v, cat: 'all' })} counts={counts} />}
            <DifficultyFilter value={diff} onChange={(v) => upd({ diff: v })} />
            <SelectFilter id="f-cat" label="Topic (category)" value={cat} onChange={(v) => upd({ cat: v })} options={cats} />
            <SelectFilter id="f-kind" label="Program type" value={kind} onChange={(v) => upd({ kind: v })} options={kinds} />
            {filtersActive && <button className="clay-btn btn-sm w-full" onClick={() => { setLimit(PAGE); replaceQuery(base, {}); }}>Clear all filters</button>}
            <button className={`clay-btn btn-sm w-full ${selMode ? 'clay-mint' : ''}`} aria-pressed={selMode} onClick={() => { setSelMode(!selMode); setSel([]); }}><CheckSquare size={15} />Select programs for ZIP</button>
          </div>
        </aside>
        <section aria-label="Program list">
          {selMode && <div className="clay-tint p-3 mb-4 flex flex-wrap items-center gap-3"><b>{sel.length} selected</b>
            <button className="clay-btn btn-sm" onClick={() => setSel(sorted.map((p) => p.id))}>Select all {sorted.length} shown</button><button className="clay-btn btn-sm" onClick={() => setSel([])}>Clear</button>
            <button className="clay-btn clay-primary btn-sm" disabled={!sel.length} onClick={() => runZip({ kind: 'selected', programs: all.filter((p) => sel.includes(p.id)), scope: 'Selected Programs' })}><FolderArchive size={15} />Download selected ZIP</button></div>}
          {sorted.length === 0 ? <Empty icon={SearchX} title="No programs found">Try a different word (e.g. “list”, “stack”, “SQLite”) or clear the filters.</Empty> : (
            <>
              <div className="grid sm:grid-cols-2 xl:grid-cols-3 gap-5">{sorted.slice(0, limit).map((p) => <ProgramCard key={p.id} p={p} selectable={selMode} selected={sel.includes(p.id)} onSelect={toggle} />)}</div>
              <div className="text-center mt-8"><p className="text-sm font-bold text-soft mb-3">Showing {Math.min(limit, sorted.length)} of {sorted.length}</p>
                {limit < sorted.length && <button className="clay-btn clay-primary" onClick={() => setLimit(limit + PAGE)}>Load more programs</button>}</div>
            </>)}
        </section>
      </div>
    </div>
  );
}
// Controlled live-filter box inside the page (instant search; no navigation)
function ListSearch({ q, onChange }) {
  return <div className="clay-inset px-4 py-2"><input id="list-search" aria-label="Search Python programs, concepts, or topics"  value={q} onChange={(e) => onChange(e.target.value)} placeholder="Search Python programs, concepts, or topics..." className="bg-transparent outline-none w-full font-bold text-sm" /></div>;
}
