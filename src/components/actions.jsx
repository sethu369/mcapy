import { useState, useSyncExternalStore } from 'react';
import { Copy, Check, Download, Heart, Archive, FileDown, X, FolderArchive } from 'lucide-react';
import { toast, Spinner, Modal } from './ui.jsx';
import { toggleFavorite, setProgress, progressOf, PROGRESS, useStore, published } from '../lib/store.js';
import { downloadPython, buildZip, downloadBlob, zipNameFor } from '../lib/zip.js';

export async function copyText(text) {
  try { await navigator.clipboard.writeText(text); return true; } catch {
    try { const t = document.createElement('textarea'); t.value = text; t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select(); const ok = document.execCommand('copy'); t.remove(); return ok; } catch { return false; }
  }
}
export function CopyButton({ code, small, label = 'Copy Code' }) {
  const [done, setDone] = useState(false);
  return (
    <button className={`clay-btn ${small ? 'btn-sm' : ''}`} aria-label={`${label}`} onClick={async (e) => { e.stopPropagation(); const ok = await copyText(code); if (ok) { setDone(true); toast('Python code copied to clipboard'); setTimeout(() => setDone(false), 1800); } else toast('Copy failed - select the code and press Ctrl+C', 'error'); }}>
      {done ? <Check size={16} className="text-mint-dark" /> : <Copy size={16} />}{done ? 'Copied!' : label}
    </button>
  );
}
export const DownloadButton = ({ program, small, label = 'Download' }) => (
  <button className={`clay-btn ${small ? 'btn-sm' : ''}`} aria-label={`Download ${program.filename}`} onClick={(e) => { e.stopPropagation(); downloadPython(program); toast(`Downloaded ${program.filename}`); }}><Download size={16} />{label}</button>
);
export const FavoritesButton = ({ id, small }) => {
  const { prefs } = useStore(); const on = prefs.favorites.includes(id);
  return (
    <button className={`clay-btn clay-icon ${small ? '!w-9 !h-9' : ''}`} aria-pressed={on} aria-label={on ? 'Remove from favorites' : 'Add to favorites'} onClick={(e) => { e.stopPropagation(); toggleFavorite(id); toast(on ? 'Removed from favorites' : 'Added to favorites', 'info'); }}>
      <Heart size={18} className={on ? 'fill-rose-500 text-rose-500' : ''} />
    </button>
  );
};
export function ProgressTracker({ id, compact }) {
  const s = useStore(); const cur = progressOf(id, s);
  const col = { 'Not Started': '', Practicing: 'bg-amber-100', Completed: 'clay-mint' };
  return (
    <div role="radiogroup" aria-label="Progress" className="flex flex-wrap gap-2">
      {PROGRESS.map((p) => (
        <button key={p} role="radio" aria-checked={cur === p} onClick={(e) => { e.stopPropagation(); setProgress(id, p); toast(`Marked "${p}"`, 'info'); }} className={`clay-btn btn-sm ${cur === p ? (col[p] || 'bg-primary-light') + ' ring-2 ring-primary/40' : ''}`}>
          {cur === p && <Check size={14} />}{compact ? p.split(' ')[0] : p}
        </button>))}
    </div>
  );
}

/* ---------- ZIP jobs (global progress dialog) ---------- */
let job = null; const subs = new Set(); const emit = () => subs.forEach((f) => f());
export async function runZip({ kind = 'all', unit, programs, scope }) {
  const name = zipNameFor(kind, unit);
  if (!programs.length) { toast('There are no programs to export.', 'error'); return; }
  job = { status: 'loading', name, count: programs.length, percent: 0 }; emit();
  try {
    const { blob, count } = await buildZip(programs, scope, (percent) => { job = { ...job, percent }; emit(); });
    downloadBlob(blob, name); job = { status: 'done', name, count, size: blob.size }; emit();
  } catch (e) { job = { status: 'error', name, message: String(e) }; emit(); }
}
export const zipAll = () => runZip({ kind: 'all', programs: published(), scope: 'All Programs' });
export const zipUnit = (n) => runZip({ kind: 'unit', unit: n, programs: published().filter((p) => p.unit === n), scope: `Unit ${n}` });
export function ZipHost() {
  const j = useSyncExternalStore((f) => { subs.add(f); return () => subs.delete(f); }, () => job);
  if (!j) return null;
  const close = () => { job = null; emit(); };
  return (
    <Modal open onClose={j.status === 'loading' ? undefined : close} title={j.status === 'loading' ? 'Creating ZIP file…' : j.status === 'done' ? 'ZIP file ready' : 'ZIP failed'} footer={j.status !== 'loading' && <button className="clay-btn clay-primary" onClick={close}>Close</button>}>
      {j.status === 'loading' && <div role="status"><p className="font-bold flex items-center gap-2"><Spinner />Packing {j.count} programs into {j.name}</p>
        <div className="clay-inset h-4 mt-4 overflow-hidden"><div className="h-full bg-primary rounded-full transition-all" style={{ width: `${Math.max(6, j.percent)}%` }} /></div></div>}
      {j.status === 'done' && <div className="space-y-2"><p className="font-bold text-mint-dark flex items-center gap-2"><Check size={18} />Download started</p>
        <p><span className="text-soft font-bold">File:</span> <code className="font-bold">{j.name}</code></p>
        <p><span className="text-soft font-bold">Programs included:</span> <b>{j.count}</b></p>
        <p><span className="text-soft font-bold">Size:</span> {(j.size / 1024).toFixed(1)} KB</p>
        <p className="text-sm text-soft font-semibold">Generated from your current saved collection (edits, additions and deletions are reflected; drafts and trash are excluded).</p></div>}
      {j.status === 'error' && <p className="text-rose-700 font-bold">{j.message}</p>}
    </Modal>
  );
}
export function DownloadAllButton({ className = '', primary = true, label = 'Download All Programs' }) {
  return <button className={`clay-btn ${primary ? 'clay-primary' : ''} ${className}`} onClick={zipAll}><FolderArchive size={18} />{label}</button>;
}
export function DownloadUnitButton({ n, small, label }) {
  return <button className={`clay-btn ${small ? 'btn-sm' : ''}`} onClick={(e) => { e.stopPropagation(); zipUnit(n); }} aria-label={label ? `${label} (Unit ${n})` : `Download Unit ${n} Programs`}><Archive size={16} />{label || `Download Unit ${n} Programs`}</button>;
}
