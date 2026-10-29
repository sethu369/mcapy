import { useEffect, useState, useSyncExternalStore } from 'react';
// Tiny hash router with query params and a "leave guard" for unsaved changes.
let guard = null, pending = null; const subs = new Set(); let current = location.hash || '#/';
const emit = () => subs.forEach((f) => f());
export function setGuard(fn) { guard = fn; }
export function parse(hash = location.hash) {
  const h = (hash || '#/').replace(/^#/, '') || '/';
  const [path, qs = ''] = h.split('?');
  return { path: path || '/', parts: (path || '/').split('/').filter(Boolean).map(decodeURIComponent), q: Object.fromEntries(new URLSearchParams(qs)) };
}
export function href(path, q) {
  const qs = q ? new URLSearchParams(Object.entries(q).filter(([, v]) => v !== '' && v != null && v !== 'all')).toString() : '';
  return '#' + path + (qs ? '?' + qs : '');
}
export function go(path, q) { const t = href(path, q); if (location.hash !== t) location.hash = t; }
export function replaceQuery(path, q) { history.replaceState(null, '', href(path, q)); current = location.hash; emit(); }
let confirmHandler = null;
export function onLeaveConfirm(fn) { confirmHandler = fn; }
window.addEventListener('hashchange', () => {
  const target = location.hash;
  if (guard && guard()) {
    history.replaceState(null, '', current);
    pending = target;
    confirmHandler && confirmHandler(() => { guard = null; const t = pending; pending = null; location.hash = t; });
    return;
  }
  current = target; window.scrollTo({ top: 0 }); emit();
});
window.addEventListener('beforeunload', (e) => { if (guard && guard()) { e.preventDefault(); e.returnValue = ''; } });
export function useRoute() {
  return useSyncExternalStore((cb) => { subs.add(cb); return () => subs.delete(cb); }, () => current, () => '#/') && parse(current);
}
