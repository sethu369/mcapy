import { Eye, Pencil, ArrowRight, FolderOpen, CheckCircle2 } from 'lucide-react';
import { href, go } from '../lib/router.js';
import { UnitBadge, DiffBadge } from './ui.jsx';
import { CopyButton, DownloadButton, FavoritesButton, DownloadUnitButton } from './actions.jsx';
import { useStore, published, progressOf } from '../lib/store.js';
import { UNIT_TOPICS } from '../data/syllabus.js';

export function ProgramCard({ p, selectable, selected, onSelect }) {
  const s = useStore(); const prog = progressOf(p.id, s);
  return (
    <article className={`clay p-5 flex flex-col gap-3 unit-${p.unit} relative`} aria-labelledby={`t-${p.id}`}>
      <div className="flex items-start justify-between gap-2">
        <div className="flex flex-wrap items-center gap-2">
          {selectable && <input type="checkbox" className="w-5 h-5 accent-[#5b4fd9]" checked={!!selected} onChange={() => onSelect(p.id)} aria-label={`Select ${p.title}`} />}
          <span className="chip bg-ink text-white">#{String(p.number ?? 0).padStart(2, '0')}</span><UnitBadge n={p.unit} /><DiffBadge d={p.difficulty} />
        </div>
        <FavoritesButton id={p.id} small />
      </div>
      <div>
        <h3 id={`t-${p.id}`} className="font-extrabold text-lg leading-snug"><a href={href(`/program/${p.id}`)} className="hover:text-primary">{p.title}</a></h3>
        <p className="text-xs font-extrabold text-soft mt-1 uppercase tracking-wide">{p.category}{p.kind !== 'Demonstration' ? ` · ${p.kind}` : ''}</p>
      </div>
      <p className="text-sm font-semibold text-soft flex-1 line-clamp-3">{p.description}</p>
      <div className="flex items-center gap-2 text-xs font-bold">
        {prog === 'Completed' && <span className="chip bg-mint-light text-mint-dark"><CheckCircle2 size={12} />Completed</span>}
        {prog === 'Practicing' && <span className="chip bg-amber-100 text-amber-800">Practicing</span>}
        {p.status === 'draft' && <span className="chip bg-amber-100 text-amber-800">Draft</span>}
        {p.origin === 'user' && <span className="chip bg-sky-100 text-sky-800">Your program</span>}
      </div>
      <div className="flex flex-wrap gap-2">
        <a className="clay-btn clay-primary btn-sm" href={href(`/program/${p.id}`)}><Eye size={15} />View Program</a>
        <CopyButton code={p.code} small label="Copy Code" /><DownloadButton program={p} small />
        <a className="clay-btn clay-icon !w-9 !h-9" href={href(`/edit/${p.id}`)} aria-label={`Edit ${p.title}`}><Pencil size={15} /></a>
      </div>
    </article>
  );
}
export function UnitCard({ u }) {
  const s = useStore(); const progs = published(s).filter((p) => p.unit === u.n);
  const done = progs.filter((p) => progressOf(p.id, s) === 'Completed').length; const pct = progs.length ? Math.round((done / progs.length) * 100) : 0;
  return (
    <article className={`clay p-6 flex flex-col gap-3 unit-${u.n}`} aria-labelledby={`u-${u.n}`}>
      <div className="flex items-center justify-between"><span className="w-14 h-14 rounded-3xl grid place-items-center text-2xl font-extrabold text-white shadow-[inset_-4px_-4px_8px_rgba(0,0,0,.2),inset_4px_4px_8px_rgba(255,255,255,.35),6px_8px_14px_rgba(80,70,160,.3)]" style={{ background: 'var(--u)' }}>{u.n}</span>
        <span className="chip unit-badge text-sm">{progs.length} programs</span></div>
      <h3 id={`u-${u.n}`} className="font-extrabold text-xl leading-snug">Unit {u.n}: {u.title}</h3>
      <p className="text-sm font-semibold text-soft">{u.desc}</p>
      <div><p className="label">Topics covered</p><p className="text-xs font-bold text-ink/80 line-clamp-3">{UNIT_TOPICS[u.n].slice(0, 9).join(' · ')}{UNIT_TOPICS[u.n].length > 9 ? ' …' : ''}</p></div>
      <div><div className="flex justify-between text-xs font-extrabold text-soft mb-1"><span>Your progress</span><span>{done}/{progs.length} completed</span></div>
        <div className="clay-inset h-3 overflow-hidden" role="progressbar" aria-valuenow={pct} aria-valuemin="0" aria-valuemax="100" aria-label={`Unit ${u.n} completion`}><div className="h-full rounded-full" style={{ width: `${pct}%`, background: 'var(--u)' }} /></div></div>
      <div className="flex flex-wrap gap-2 mt-auto pt-1">
        <a className="clay-btn clay-primary btn-sm" href={href(`/unit/${u.n}`)}><FolderOpen size={15} />Explore Unit<ArrowRight size={14} /></a>
        <DownloadUnitButton n={u.n} small label="Download Unit ZIP" />
      </div>
    </article>
  );
}
