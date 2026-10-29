import { useEffect, useState } from 'react';
import { Pencil, Trash2, History, ArrowLeft, Terminal, Package, ArrowRight, ListChecks, PlayCircle, Lightbulb } from 'lucide-react';
import { useStore, byId, published, addRecent, trashProgram, versionsOf } from '../lib/store.js';
import { href, go } from '../lib/router.js';
import { UnitBadge, DiffBadge, Confirm, toast, Empty, fmtDate } from '../components/ui.jsx';
import { CopyButton, DownloadButton, FavoritesButton, ProgressTracker } from '../components/actions.jsx';
import CodeViewer from '../components/CodeViewer.jsx';
import { CONCEPTS } from '../data/concepts.js';
import { UNITS } from '../data/syllabus.js';
import { SearchX } from 'lucide-react';

const Block = ({ icon: Icon, title, children }) => (
  <section className="clay p-5 sm:p-7"><h2 className="font-extrabold text-xl mb-4 flex items-center gap-2">{Icon && <Icon size={20} className="text-primary" />}{title}</h2>{children}</section>
);
export default function ProgramDetails({ id }) {
  const s = useStore(); const p = byId(id, s); const [del, setDel] = useState(false);
  useEffect(() => { if (p && p.status === 'published') addRecent(id); }, [id, p?.status]);
  if (!p) return <Empty icon={SearchX} title="Program not found">It may have been deleted. <a className="text-primary underline" href={href('/programs')}>Back to all programs</a></Empty>;
  const all = published(s).filter((x) => x.unit === p.unit).sort((a, b) => a.number - b.number);
  const idx = all.findIndex((x) => x.id === p.id);
  const related = all.filter((x) => x.id !== p.id && (x.category === p.category || x.concepts?.some((c) => p.concepts?.includes(c)))).slice(0, 6);
  const notes = CONCEPTS.filter((c) => c.match.test(`${p.title} ${p.category}`)).slice(0, 3);
  const nv = versionsOf(p.id, s).length;
  return (
    <div className={`unit-${p.unit} space-y-6`}>
      <a href={href(p.status === 'published' ? `/unit/${p.unit}` : '/manage')} className="inline-flex items-center gap-1 font-extrabold text-soft hover:text-primary"><ArrowLeft size={16} />{p.status === 'published' ? `Back to Unit ${p.unit}` : 'Back to Manage Programs'}</a>
      {p.status !== 'published' && <div className="clay-tint p-3 font-bold text-amber-800" role="status">This program is a {p.status === 'draft' ? 'draft and is not part of the published collection' : 'deleted program (in Trash)'}.</div>}
      <header className="clay p-6 sm:p-8">
        <div className="flex flex-wrap items-center gap-2 mb-3"><span className="chip bg-ink text-white">Program #{String(p.number ?? 0).padStart(2, '0')}</span><UnitBadge n={p.unit}>Unit {p.unit}: {UNITS[p.unit - 1]?.title}</UnitBadge><span className="chip">{p.category}</span><DiffBadge d={p.difficulty} /><span className="chip bg-sky-100 text-sky-800">{p.kind}</span><span className="chip bg-slate-100 text-slate-600">ID: {p.id}</span></div>
        <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight">{p.title}</h1>
        <p className="text-lg font-semibold text-soft mt-3 max-w-3xl">{p.description}</p>
        {p.concepts?.length > 0 && <div className="mt-4 flex flex-wrap gap-2 items-center"><span className="label !mb-0">Concepts used:</span>{p.concepts.map((c) => <span key={c} className="chip">{c}</span>)}</div>}
        {p.deps?.length > 0 && <p className="mt-4 inline-flex items-center gap-2 clay-tint px-4 py-2 font-bold text-sm"><Package size={16} />Requires: <code>python -m pip install {p.deps.join(' ')}</code></p>}
        <div className="mt-6 flex flex-wrap gap-3 items-center">
          <FavoritesButton id={p.id} /><CopyButton code={p.code} /><DownloadButton program={p} />
          <a className="clay-btn clay-mint" href={href(`/edit/${p.id}`)}><Pencil size={16} />Edit Program</a>
          <a className="clay-btn" href={href(`/versions/${p.id}`)}><History size={16} />Version History{nv ? ` (${nv + 1})` : ''}</a>
          <button className="clay-btn clay-danger" onClick={() => setDel(true)}><Trash2 size={16} />Delete Program</button>
        </div>
        <div className="mt-5"><p className="label">Your progress</p><ProgressTracker id={p.id} /></div>
        <p className="text-xs font-bold text-soft mt-4">Version {p.version || 1} · Last updated {fmtDate(p.updatedAt)}</p>
      </header>
      {p.kind === 'Terminal Commands' && <div className="clay-tint p-4 font-bold flex gap-3 items-start"><Terminal className="text-primary shrink-0" />Lines beginning with <code>#&nbsp;TERMINAL:</code> or <code>#&nbsp;CMD&gt;</code> are Windows terminal commands. Run them in Command Prompt or PowerShell — they are not Python statements. The rest is ordinary Python.</div>}
      {p.algorithm?.length > 0 && <Block icon={ListChecks} title="Algorithm"><ol className="space-y-2">{p.algorithm.map((a, i) => <li key={i} className="flex gap-3"><span className="clay-sm w-8 h-8 grid place-items-center font-extrabold text-primary shrink-0 !rounded-xl">{i + 1}</span><span className="font-semibold pt-1">{a}</span></li>)}</ol></Block>}
      <div className="clay p-5 sm:p-7"><CodeViewer code={p.code} filename={p.filename} /></div>
      {p.explanation && <Block icon={Lightbulb} title="Explanation"><p className="font-semibold leading-relaxed text-ink/90 whitespace-pre-line">{p.explanation}</p></Block>}
      <Block icon={PlayCircle} title="Sample Input and Output">
        <div className="grid md:grid-cols-2 gap-5">
          <div><p className="label">Sample input{p.args?.length ? ' / arguments' : ''}</p><pre className="codebox code-font p-4 whitespace-pre-wrap break-words min-h-[3rem]">{[p.args?.length ? `$ python ${p.filename} ${p.args.join(' ')}` : '', p.sampleInput].filter(Boolean).join('\n') || '(no input needed)'}</pre></div>
          <div><p className="label">Sample output</p><pre className="codebox code-font p-4 whitespace-pre-wrap break-words overflow-auto max-h-96 min-h-[3rem]">{p.sampleOutput || '(no output recorded)'}</pre></div>
        </div>
        <p className="text-xs font-bold text-soft mt-3">{p.origin === 'seed' && p.version === 1 ? 'Output captured by actually running this program with the sample input shown.' : 'Sample output is the text saved with this program; it was not generated by running the edited code.'}</p>
      </Block>
      {notes.length > 0 && <Block title="Important Concepts"><div className="grid md:grid-cols-3 gap-4">{notes.map((c) => <a key={c.slug} href={href(`/concepts`, { open: c.slug })} className="clay-tint p-4 block hover:-translate-y-0.5 transition"><p className="font-extrabold">{c.name}</p><p className="text-sm font-semibold text-soft mt-1 line-clamp-4">{c.explain}</p></a>)}</div></Block>}
      {related.length > 0 && <Block title="Related Programs"><ul className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">{related.map((r) => <li key={r.id}><a className="clay-sm p-3 block font-bold hover:text-primary" href={href(`/program/${r.id}`)}><span className="text-soft text-xs block">#{r.number} · {r.category}</span>{r.title}</a></li>)}</ul></Block>}
      <nav className="flex justify-between gap-3" aria-label="Previous and next program">
        {idx > 0 ? <a className="clay-btn" href={href(`/program/${all[idx - 1].id}`)}><ArrowLeft size={16} />Previous</a> : <span />}
        {idx >= 0 && idx < all.length - 1 && <a className="clay-btn" href={href(`/program/${all[idx + 1].id}`)}>Next<ArrowRight size={16} /></a>}
      </nav>
      <Confirm open={del} danger title="Delete this Python program?" confirmLabel="Move to Trash" onCancel={() => setDel(false)} onConfirm={() => { trashProgram(p.id); setDel(false); toast('Moved to Trash. You can restore it from Manage → Trash.'); go('/manage'); }}>
        <DeleteInfo p={p} />
      </Confirm>
    </div>
  );
}
export const DeleteInfo = ({ p }) => (
  <div><p className="font-semibold mb-3">Are you sure you want to delete this Python program?</p>
    <dl className="clay-tint p-4 space-y-1 font-bold"><div><dt className="inline text-soft">Title: </dt><dd className="inline">{p.title}</dd></div><div><dt className="inline text-soft">Unit: </dt><dd className="inline">{p.unit ? `Unit ${p.unit}: ${UNITS[p.unit - 1].title}` : 'Not assigned'}</dd></div><div><dt className="inline text-soft">Filename: </dt><dd className="inline"><code>{p.filename}</code></dd></div></dl>
    <p className="text-sm text-soft font-semibold mt-3">It will be moved to the Trash (soft delete): hidden from search, units, favorites, statistics and ZIP exports. You can restore it later.</p></div>
);
