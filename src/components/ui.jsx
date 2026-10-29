import { useEffect, useRef, useState, useSyncExternalStore } from 'react';
import { X, CheckCircle2, AlertTriangle, Info, Loader2, MoreVertical } from 'lucide-react';

/* ---------- toasts ---------- */
let toasts = [], tsubs = new Set(), tid = 0;
const temit = () => tsubs.forEach((f) => f());
export function toast(message, type = 'success') {
  const id = ++tid; toasts = [...toasts, { id, message, type }]; temit();
  setTimeout(() => { toasts = toasts.filter((t) => t.id !== id); temit(); }, type === 'error' ? 6000 : 3200);
}
export function ToastHost() {
  const list = useSyncExternalStore((f) => { tsubs.add(f); return () => tsubs.delete(f); }, () => toasts);
  const Icon = { success: CheckCircle2, error: AlertTriangle, info: Info };
  return (
    <div className="fixed bottom-4 left-1/2 -translate-x-1/2 z-[100] flex flex-col gap-2 w-[min(92vw,420px)]" role="status" aria-live="polite">
      {list.map((t) => { const I = Icon[t.type]; return (
        <div key={t.id} className={`clay-sm pop flex items-start gap-3 px-4 py-3 font-bold ${t.type === 'error' ? 'text-rose-700' : t.type === 'info' ? 'text-primary-dark' : 'text-mint-dark'}`}>
          <I size={20} className="shrink-0 mt-0.5" /><span className="text-ink text-sm">{t.message}</span>
        </div>); })}
    </div>
  );
}

/* ---------- modal / confirm ---------- */
export function Modal({ open, onClose, title, children, wide, footer, labelledBy = 'modal-title' }) {
  const ref = useRef(null);
  useEffect(() => {
    if (!open) return;
    const prev = document.activeElement; const onKey = (e) => { if (e.key === 'Escape') onClose?.(); };
    document.addEventListener('keydown', onKey); document.body.style.overflow = 'hidden';
    setTimeout(() => ref.current?.querySelector('[data-autofocus], input, textarea, select, button')?.focus(), 30);
    return () => { document.removeEventListener('keydown', onKey); document.body.style.overflow = ''; prev?.focus?.(); };
  }, [open, onClose]);
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-[90] flex items-end sm:items-center justify-center p-0 sm:p-4 bg-[#2a2560]/35 backdrop-blur-sm" onMouseDown={(e) => e.target === e.currentTarget && onClose?.()}>
      <div ref={ref} role="dialog" aria-modal="true" aria-labelledby={labelledBy} className={`clay pop w-full ${wide ? 'sm:max-w-4xl' : 'sm:max-w-lg'} max-h-[92vh] flex flex-col rounded-b-none sm:rounded-b-[28px]`}>
        <div className="flex items-center justify-between gap-3 px-5 sm:px-7 pt-5 pb-3">
          <h2 id={labelledBy} className="text-xl font-extrabold">{title}</h2>
          <button className="clay-btn clay-icon" onClick={onClose} aria-label="Close dialog"><X size={18} /></button>
        </div>
        <div className="px-5 sm:px-7 pb-4 overflow-y-auto">{children}</div>
        {footer && <div className="px-5 sm:px-7 pb-5 pt-2 flex flex-wrap gap-3 justify-end">{footer}</div>}
      </div>
    </div>
  );
}
export function Confirm({ open, title, children, confirmLabel = 'Confirm', danger, onConfirm, onCancel, cancelLabel = 'Cancel' }) {
  return (
    <Modal open={open} onClose={onCancel} title={title} footer={<>
      <button className="clay-btn" onClick={onCancel} data-autofocus>{cancelLabel}</button>
      <button className={`clay-btn ${danger ? 'clay-danger' : 'clay-primary'}`} onClick={onConfirm}>{confirmLabel}</button></>}>
      {children}
    </Modal>
  );
}

/* ---------- misc ---------- */
export const Spinner = ({ size = 18 }) => <Loader2 size={size} className="spin" aria-hidden="true" />;
export const UnitBadge = ({ n, children }) => <span className={`unit-${n} unit-badge chip`}>{children ?? `Unit ${n}`}</span>;
const DIFF = { Beginner: 'bg-mint-light text-mint-dark', Intermediate: 'bg-amber-100 text-amber-800', Advanced: 'bg-rose-100 text-rose-700' };
export const DiffBadge = ({ d }) => <span className={`chip ${DIFF[d] || ''}`}>{d}</span>;
export const Empty = ({ icon: Icon, title, children }) => (
  <div className="clay-tint p-8 text-center">{Icon && <Icon className="mx-auto mb-3 text-primary" size={34} />}<p className="font-extrabold text-lg">{title}</p><div className="text-soft font-semibold mt-1">{children}</div></div>
);
export const PageTitle = ({ title, sub, children }) => (
  <div className="flex flex-wrap items-end justify-between gap-4 mb-6">
    <div><h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight">{title}</h1>{sub && <p className="text-soft font-semibold mt-1 max-w-2xl">{sub}</p>}</div>
    <div className="flex flex-wrap gap-3">{children}</div>
  </div>
);
export const Field = ({ label, error, hint, children, htmlFor, required }) => (
  <div><label htmlFor={htmlFor} className="label">{label}{required && <span className="text-rose-600"> *</span>}</label>{children}
    {hint && !error && <p className="text-xs text-soft font-semibold mt-1">{hint}</p>}
    {error && <p className="text-sm text-rose-700 font-bold mt-1" role="alert">{error}</p>}</div>
);
/* accessible action menu (used on mobile where a row of icons would overflow) */
export function ActionMenu({ label = 'Actions', items }) {
  const [open, setOpen] = useState(false); const ref = useRef(null);
  useEffect(() => { if (!open) return; const h = (e) => { if (!ref.current?.contains(e.target)) setOpen(false); }; const k = (e) => e.key === 'Escape' && setOpen(false); document.addEventListener('mousedown', h); document.addEventListener('keydown', k); return () => { document.removeEventListener('mousedown', h); document.removeEventListener('keydown', k); }; }, [open]);
  return (
    <div className="relative" ref={ref}>
      <button className="clay-btn clay-icon" aria-haspopup="menu" aria-expanded={open} aria-label={label} onClick={() => setOpen(!open)}><MoreVertical size={18} /></button>
      {open && <div role="menu" className="clay-sm absolute right-0 z-30 mt-2 w-48 p-2 pop">
        {items.map((it) => <button key={it.label} role="menuitem" className={`w-full text-left px-3 py-2 rounded-xl font-bold text-sm hover:bg-primary-light flex items-center gap-2 ${it.danger ? 'text-rose-700' : ''}`} onClick={() => { setOpen(false); it.onClick(); }}>{it.icon}{it.label}</button>)}
      </div>}
    </div>
  );
}
export const fmtDate = (iso) => { try { return new Date(iso).toLocaleString(undefined, { dateStyle: 'medium', timeStyle: 'short' }); } catch { return iso; } };
export const fmtDay = (iso) => { try { return new Date(iso).toLocaleDateString(undefined, { dateStyle: 'medium' }); } catch { return iso; } };
