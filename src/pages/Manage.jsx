import { useMemo, useState } from 'react';
import { Plus, Eye, Pencil, Trash2, Upload, Download, FolderArchive, FileClock, Archive, RotateCcw, Rocket, ShieldAlert, History, RefreshCcw } from 'lucide-react';
import { useStore, published, drafts, trashed, progressOf, trashProgram, restoreProgram, purgeProgram, resetCollection, getStorageMode } from '../lib/store.js';
import { href, go } from '../lib/router.js';
import { PageTitle, Confirm, Modal, toast, ActionMenu, Empty, fmtDate, fmtDay, UnitBadge, DiffBadge } from '../components/ui.jsx';
import { DownloadAllButton, runZip, zipUnit } from '../components/actions.jsx';
import { SelectFilter } from '../components/Filters.jsx';
import { UNITS } from '../data/syllabus.js';
import { DeleteInfo } from './ProgramDetails.jsx';
import ImportDialog from './ImportDialog.jsx';

export function ManageTabs({ path }) {
  const s = useStore();
  const tabs = [['/manage', 'Dashboard', published(s).length], ['/drafts', 'Draft Programs', drafts(s).length], ['/trash', 'Trash', trashed(s).length]];
  return <nav aria-label="Program management sections" className="flex flex-wrap gap-2 mb-6">{tabs.map(([p, l, n]) => <a key={p} href={href(p)} aria-current={path === p ? 'page' : undefined} className={`clay-btn ${path === p ? 'clay-primary' : ''}`}>{l}<span className="chip !bg-white/70 !text-ink">{n}</span></a>)}</nav>;
}
const Stat = ({ label, value, sub, cls = '' }) => <div className={`clay p-5 ${cls}`}><p className="text-sm font-extrabold text-soft">{label}</p><p className="text-4xl font-extrabold mt-1" style={{ color: 'var(--u, #5b4fd9)' }}>{value}</p>{sub && <p className="text-xs font-bold text-soft mt-1">{sub}</p>}</div>;

export default function Manage() {
  const s = useStore(); const all = published(s);
  const [q, setQ] = useState(''), [unit, setUnit] = useState('all'), [cat, setCat] = useState('all'), [diff, setDiff] = useState('all'), [page, setPage] = useState(0);
  const [sel, setSel] = useState([]), [del, setDel] = useState(null), [imp, setImp] = useState(false), [exp, setExp] = useState(false), [reset, setReset] = useState(false);
  const PER = 25;
  const cats = useMemo(() => [...new Set(all.filter((p) => unit === 'all' || String(p.unit) === unit).map((p) => p.category))].sort(), [all, unit]);
  const rows = useMemo(() => all.filter((p) => (unit === 'all' || String(p.unit) === unit) && (cat === 'all' || p.category === cat) && (diff === 'all' || p.difficulty === diff) && (!q || (p.title + ' ' + p.id + ' ' + p.filename).toLowerCase().includes(q.toLowerCase()))).sort((a, b) => a.unit - b.unit || a.number - b.number), [all, q, unit, cat, diff]);
  const pages = Math.max(1, Math.ceil(rows.length / PER)); const cur = Math.min(page, pages - 1); const slice = rows.slice(cur * PER, cur * PER + PER);
  const completed = all.filter((p) => progressOf(p.id, s) === 'Completed').length;
  const favs = all.filter((p) => s.prefs.favorites.includes(p.id));
  const recentCreated = [...all].sort((a, b) => b.createdAt.localeCompare(a.createdAt) || b.number - a.number).slice(0, 5);
  const recentUpdated = [...all].filter((p) => p.updatedAt !== p.createdAt || p.version > 1).sort((a, b) => b.updatedAt.localeCompare(a.updatedAt)).slice(0, 5);
  const one = sel.length === 1 ? all.find((p) => p.id === sel[0]) : null;
  const toggle = (id) => setSel((x) => (x.includes(id) ? x.filter((i) => i !== id) : [...x, id]));
  const allShown = slice.length > 0 && slice.every((p) => sel.includes(p.id));
  return (
    <div>
      <PageTitle title="Manage Programs" sub="Create, view, edit and delete the Python programs in your collection. Everything updates search, units, downloads and ZIP exports instantly." />
      <ManageTabs path="/manage" />
      <div className="clay-tint p-3 mb-6 flex gap-3 items-start text-sm font-bold text-ink/80"><ShieldAlert className="text-amber-600 shrink-0" size={20} /><p>Program management is available to the local website user and is <b>not protected by an account system</b>. Changes are saved in this browser ({getStorageMode() === 'indexeddb' ? 'IndexedDB' : getStorageMode() === 'localstorage' ? 'localStorage' : 'memory only — will be lost on refresh'}) on this device only; download a ZIP to back up your work.</p></div>
      <section aria-label="Statistics" className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
        <Stat label="Total programs" value={all.length} sub={`${drafts(s).length} drafts · ${trashed(s).length} in trash`} /><Stat label="Completed" value={completed} sub={`of ${all.length} programs`} />
        <Stat label="Favorites" value={favs.length} /><Stat label="Units" value={new Set(all.map((p) => p.unit)).size} sub={`${new Set(all.map((p) => p.category)).size} categories`} />
      </section>
      <section aria-label="Programs per unit" className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4 mb-6">{UNITS.map((u) => <div key={u.n} className={`clay-sm p-4 unit-${u.n}`}><p className="text-xs font-extrabold text-soft">Unit {u.n}</p><p className="text-3xl font-extrabold" style={{ color: 'var(--u)' }}>{all.filter((p) => p.unit === u.n).length}</p><p className="text-xs font-bold text-soft truncate">{u.short}</p></div>)}</section>
      <div className="grid md:grid-cols-2 gap-5 mb-6">
        {[['Recently created', recentCreated], ['Recently updated', recentUpdated]].map(([t, l]) => (
          <section key={t} className="clay p-5 min-w-0"><h2 className="font-extrabold mb-3">{t}</h2>{l.length === 0 ? <p className="text-sm font-semibold text-soft">Nothing yet — edit a program and it will appear here.</p> : <ul className="space-y-2">{l.map((p) => <li key={p.id} className="flex items-center justify-between gap-2"><a className="font-bold hover:text-primary truncate" href={href(`/program/${p.id}`)}>{p.title}</a><span className="text-xs font-bold text-soft shrink-0">{fmtDay(t.includes('updated') ? p.updatedAt : p.createdAt)}</span></li>)}</ul>}</section>))}
      </div>
      <section aria-label="Program table" className="clay p-4 sm:p-6">
        <div className="flex flex-wrap gap-3 mb-4">
          <a className="clay-btn clay-mint" href={href('/new')}><Plus size={17} />Add New Program</a>
          <a className={`clay-btn ${one ? '' : 'pointer-events-none opacity-50'}`} aria-disabled={!one} tabIndex={one ? 0 : -1} href={one ? href(`/program/${one.id}`) : undefined}><Eye size={17} />View Program</a>
          <a className={`clay-btn ${one ? '' : 'pointer-events-none opacity-50'}`} aria-disabled={!one} tabIndex={one ? 0 : -1} href={one ? href(`/edit/${one.id}`) : undefined}><Pencil size={17} />Edit Program</a>
          <button className="clay-btn" disabled={!one} onClick={() => setDel(one)}><Trash2 size={17} />Delete Program</button>
          <button className="clay-btn" onClick={() => setImp(true)}><Upload size={17} />Import Programs</button>
          <button className="clay-btn" onClick={() => setExp(true)}><Download size={17} />Export Programs</button>
          <DownloadAllButton />
        </div>
        <p className="text-xs font-bold text-soft mb-3">Tip: tick one row to enable View / Edit / Delete in the toolbar, or tick several to export them together.</p>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mb-4">
          <div><label className="label" htmlFor="m-q">Program title</label><div className="clay-inset px-4 py-2"><input id="m-q" className="bg-transparent outline-none w-full font-bold text-sm" placeholder="Search title, ID or filename" value={q} onChange={(e) => { setQ(e.target.value); setPage(0); }} /></div></div>
          <SelectFilter id="m-unit" label="Unit" value={unit} onChange={(v) => { setUnit(v); setCat('all'); setPage(0); }} options={UNITS.map((u) => String(u.n))} />
          <SelectFilter id="m-cat" label="Category" value={cat} onChange={(v) => { setCat(v); setPage(0); }} options={cats} />
          <SelectFilter id="m-diff" label="Difficulty" value={diff} onChange={(v) => { setDiff(v); setPage(0); }} options={['Beginner', 'Intermediate', 'Advanced']} />
        </div>
        <p className="text-sm font-extrabold mb-2" aria-live="polite">{rows.length} program(s){sel.length ? ` · ${sel.length} selected` : ''}</p>
        <div className="overflow-x-auto -mx-1 px-1">
          <table className="w-full text-left min-w-[860px]"><caption className="sr-only">Programs</caption>
            <thead><tr className="text-soft text-sm"><th className="p-2 w-8"><input type="checkbox" className="w-5 h-5 accent-[#5b4fd9]" aria-label="Select all shown" checked={allShown} onChange={() => setSel(allShown ? sel.filter((i) => !slice.some((p) => p.id === i)) : [...new Set([...sel, ...slice.map((p) => p.id)])])} /></th>
              <th className="p-2">Program ID</th><th className="p-2">Program Title</th><th className="p-2">Unit</th><th className="p-2">Category</th><th className="p-2">Difficulty</th><th className="p-2">Last Updated</th><th className="p-2 text-right">Actions</th></tr></thead>
            <tbody>{slice.map((p) => (
              <tr key={p.id} className={`border-t border-primary/10 ${sel.includes(p.id) ? 'bg-primary-light/60' : ''}`}>
                <td className="p-2"><input type="checkbox" className="w-5 h-5 accent-[#5b4fd9]" checked={sel.includes(p.id)} onChange={() => toggle(p.id)} aria-label={`Select ${p.title}`} /></td>
                <td className="p-2 font-mono text-xs font-bold">{p.id}</td>
                <td className="p-2 font-bold max-w-xs"><a className="hover:text-primary" href={href(`/program/${p.id}`)}>{p.title}</a><span className="block text-xs text-soft font-mono">{p.filename}{p.version > 1 ? ` · v${p.version}` : ''}</span></td>
                <td className="p-2"><UnitBadge n={p.unit} /></td><td className="p-2 text-sm font-semibold">{p.category}</td><td className="p-2"><DiffBadge d={p.difficulty} /></td>
                <td className="p-2 text-xs font-bold text-soft whitespace-nowrap">{fmtDate(p.updatedAt)}</td>
                <td className="p-2"><div className="flex justify-end gap-2">
                  <div className="hidden md:flex gap-2"><a className="clay-btn clay-icon !w-9 !h-9" aria-label={`View ${p.title}`} title="View" href={href(`/program/${p.id}`)}><Eye size={15} /></a><a className="clay-btn clay-icon !w-9 !h-9" aria-label={`Edit ${p.title}`} title="Edit" href={href(`/edit/${p.id}`)}><Pencil size={15} /></a><button className="clay-btn clay-icon !w-9 !h-9" aria-label={`Delete ${p.title}`} title="Delete" onClick={() => setDel(p)}><Trash2 size={15} className="text-rose-600" /></button></div>
                  <div className="md:hidden"><ActionMenu label={`Actions for ${p.title}`} items={[{ label: 'View', icon: <Eye size={15} />, onClick: () => go(`/program/${p.id}`) }, { label: 'Edit', icon: <Pencil size={15} />, onClick: () => go(`/edit/${p.id}`) }, { label: 'Delete', icon: <Trash2 size={15} />, danger: true, onClick: () => setDel(p) }]} /></div></div></td>
              </tr>))}</tbody></table>
          {rows.length === 0 && <div className="p-6"><Empty title="No programs match these filters" /></div>}
        </div>
        {pages > 1 && <div className="flex items-center justify-center gap-3 mt-4"><button className="clay-btn btn-sm" disabled={cur === 0} onClick={() => setPage(cur - 1)}>Previous</button><span className="font-bold text-sm">Page {cur + 1} of {pages}</span><button className="clay-btn btn-sm" disabled={cur >= pages - 1} onClick={() => setPage(cur + 1)}>Next</button></div>}
      </section>
      <div className="mt-6 flex justify-end"><button className="clay-btn btn-sm" onClick={() => setReset(true)}><RefreshCcw size={14} />Reset collection to the original programs</button></div>
      <Confirm open={!!del} danger title="Delete Python Program" confirmLabel="Delete Program" onCancel={() => setDel(null)} onConfirm={() => { trashProgram(del.id); setSel((x) => x.filter((i) => i !== del.id)); toast(`“${del.title}” moved to Trash. Restore it from the Trash tab.`); setDel(null); }}>{del && <DeleteInfo p={del} />}</Confirm>
      <Confirm open={reset} danger title="Reset the whole collection?" confirmLabel="Reset everything" onCancel={() => setReset(false)} onConfirm={() => { resetCollection(); setReset(false); setSel([]); toast('Collection reset to the original programs.'); }}><p className="font-semibold">All your added programs, edits, drafts, trash and version history will be permanently removed and the original {291} programs restored. Favorites and progress are kept. This cannot be undone.</p></Confirm>
      <ImportDialog open={imp} onClose={() => setImp(false)} />
      <Modal open={exp} onClose={() => setExp(false)} title="Export Programs" footer={<button className="clay-btn" onClick={() => setExp(false)}>Close</button>}>
        <p className="text-sm font-semibold text-soft mb-4">ZIPs are generated from your latest saved programs. Drafts and deleted programs are never included.</p>
        <div className="grid gap-3">
          <button className="clay-btn clay-primary justify-start" onClick={() => { setExp(false); runZip({ kind: 'all', programs: all, scope: 'All Programs' }); }}><FolderArchive size={17} />All published programs ({all.length})</button>
          <button className="clay-btn justify-start" disabled={!sel.length} onClick={() => { setExp(false); runZip({ kind: 'selected', programs: all.filter((p) => sel.includes(p.id)), scope: 'Selected Programs' }); }}><Archive size={17} />Selected programs ({sel.length})</button>
          <button className="clay-btn justify-start" disabled={!rows.length || rows.length === all.length} onClick={() => { setExp(false); runZip({ kind: 'selected', programs: rows, scope: 'Filtered Programs' }); }}><Archive size={17} />Programs matching current filters ({rows.length})</button>
          <div className="flex flex-wrap gap-2">{UNITS.map((u) => <button key={u.n} className="clay-btn btn-sm" onClick={() => { setExp(false); zipUnit(u.n); }}>Unit {u.n} ({all.filter((p) => p.unit === u.n).length})</button>)}</div>
        </div>
      </Modal>
    </div>
  );
}

export function Drafts({ path }) {
  const s = useStore(); const list = drafts(s).sort((a, b) => b.updatedAt.localeCompare(a.updatedAt)); const [del, setDel] = useState(null);
  return (
    <div><PageTitle title="Draft Programs" sub="Incomplete programs live here. They are not searchable or included in downloads until you publish them."><a className="clay-btn clay-mint" href={href('/new')}><Plus size={17} />Add New Program</a></PageTitle>
      <ManageTabs path={path} />
      {list.length === 0 ? <Empty icon={FileClock} title="No drafts">Use “Save as Draft” on the Add New Program form to keep unfinished work here.</Empty> : (
        <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-5">{list.map((p) => (
          <article key={p.id} className="clay p-5 space-y-2"><div className="flex flex-wrap gap-2"><span className="chip bg-amber-100 text-amber-800">Draft</span>{p.unit ? <UnitBadge n={p.unit} /> : <span className="chip bg-slate-100 text-slate-600">No unit</span>}</div>
            <h3 className="font-extrabold text-lg">{p.title}</h3><p className="text-xs font-mono text-soft">{p.id} · {p.filename || 'no filename yet'}</p>
            <p className="text-xs font-bold text-soft">{p.code.split('\n').filter(Boolean).length} lines of code · modified {fmtDate(p.updatedAt)}</p>
            <div className="flex flex-wrap gap-2 pt-2"><a className="clay-btn btn-sm" href={href(`/edit/${p.id}`)}><Pencil size={14} />Edit Draft</a>
              <a className="clay-btn clay-primary btn-sm" href={href(`/edit/${p.id}`)}><Rocket size={14} />Publish Program</a>
              <button className="clay-btn btn-sm" onClick={() => setDel(p)}><Trash2 size={14} />Delete Draft</button></div></article>))}</div>)}
      <Confirm open={!!del} danger title="Delete this draft permanently?" confirmLabel="Delete Draft" onCancel={() => setDel(null)} onConfirm={() => { purgeProgram(del.id); toast('Draft deleted permanently.'); setDel(null); }}><p className="font-semibold">“{del?.title}” is only a draft, so it is deleted permanently (there is no Trash for drafts).</p></Confirm>
    </div>
  );
}
export function Trash({ path }) {
  const s = useStore(); const list = trashed(s).sort((a, b) => (b.trashedAt || '').localeCompare(a.trashedAt || '')); const [purge, setPurge] = useState(null), [all, setAll] = useState(false);
  return (
    <div><PageTitle title="Trash" sub="Deleted programs are kept here. Restore them, or delete them permanently (this cannot be undone)." >{list.length > 0 && <button className="clay-btn clay-danger" onClick={() => setAll(true)}><Trash2 size={16} />Empty Trash</button>}</PageTitle>
      <ManageTabs path={path} />
      {list.length === 0 ? <Empty icon={Trash2} title="Trash is empty" /> : (
        <div className="grid md:grid-cols-2 gap-4">{list.map((p) => (
          <article key={p.id} className="clay p-5 space-y-2"><div className="flex flex-wrap gap-2 items-center"><UnitBadge n={p.unit} /><span className="chip bg-rose-100 text-rose-700">Deleted {p.trashedAt ? fmtDate(p.trashedAt) : ''}</span></div>
            <h3 className="font-extrabold text-lg">{p.title}</h3><p className="text-xs font-mono text-soft">{p.id} · {p.filename}</p>
            <div className="flex flex-wrap gap-2 pt-2"><button className="clay-btn clay-mint btn-sm" onClick={() => { const r = restoreProgram(p.id); r.ok ? toast(`“${p.title}” restored.`) : toast(r.errors?.filename || 'Cannot restore: filename is in use.', 'error'); }}><RotateCcw size={14} />Restore</button>
              <button className="clay-btn clay-danger btn-sm" onClick={() => setPurge(p)}><Trash2 size={14} />Delete permanently</button></div></article>))}</div>)}
      <Confirm open={!!purge} danger title="Delete permanently?" confirmLabel="Delete permanently" onCancel={() => setPurge(null)} onConfirm={() => { purgeProgram(purge.id); toast('Program deleted permanently.'); setPurge(null); }}><p className="font-semibold"><b>{purge?.title}</b> and its version history will be removed for good. This is different from moving to Trash and cannot be undone. Its ID will never be reused.</p></Confirm>
      <Confirm open={all} danger title="Empty the Trash?" confirmLabel={`Delete ${list.length} permanently`} onCancel={() => setAll(false)} onConfirm={() => { list.forEach((p) => purgeProgram(p.id)); setAll(false); toast('Trash emptied.'); }}><p className="font-semibold">{list.length} program(s) will be permanently deleted.</p></Confirm>
    </div>
  );
}
