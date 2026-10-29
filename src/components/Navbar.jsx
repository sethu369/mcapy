import { useEffect, useRef, useState } from 'react';
import { Code2, Menu, X, Search, Heart, Settings2 } from 'lucide-react';
import { go, href } from '../lib/router.js';
import { useStore, published } from '../lib/store.js';
import { suggestions } from '../lib/search.js';
import { UnitBadge } from './ui.jsx';

export const NAV = [
  ['/', 'Home'], ['/programs', 'Programs'], ['/units', 'Units'], ['/concepts', 'Concepts'], ['/practice', 'Practice'], ['/syllabus', 'Syllabus'], ['/manage', 'Manage Programs'], ['/about', 'About'],
];
export function SearchBar({ initial = '', autoFocus, onDone, className = '', id = 'site-search' }) {
  const s = useStore(); const [q, setQ] = useState(initial); const [open, setOpen] = useState(false); const [idx, setIdx] = useState(-1);
  const progs = published(s); const sug = open ? suggestions(progs, q) : [];
  const box = useRef(null);
  useEffect(() => setQ(initial), [initial]);
  useEffect(() => { const h = (e) => { if (!box.current?.contains(e.target)) setOpen(false); }; document.addEventListener('mousedown', h); return () => document.removeEventListener('mousedown', h); }, []);
  const submit = (text) => { setOpen(false); onDone?.(); go('/programs', { q: text }); };
  const pick = (x) => (x.kind === 'program' ? (setOpen(false), onDone?.(), go(`/program/${x.id}`)) : submit(x.text));
  const onKey = (e) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); setOpen(true); setIdx((i) => Math.min(sug.length - 1, i + 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setIdx((i) => Math.max(-1, i - 1)); }
    else if (e.key === 'Enter') { e.preventDefault(); idx >= 0 && sug[idx] ? pick(sug[idx]) : submit(q); }
    else if (e.key === 'Escape') { setOpen(false); setIdx(-1); }
  };
  return (
    <div className={`relative ${className}`} ref={box} role="search">
      <div className="clay-inset flex items-center gap-2 px-4 py-2">
        <Search size={18} className="text-soft shrink-0" aria-hidden="true" />
        <input id={id} type="search" autoFocus={autoFocus} value={q} onChange={(e) => { setQ(e.target.value); setOpen(true); setIdx(-1); }} onFocus={() => setOpen(true)} onKeyDown={onKey}
          placeholder="Search Python programs, concepts, or topics..." aria-label="Search Python programs, concepts, or topics" role="combobox" aria-expanded={open && sug.length > 0} aria-controls={`${id}-list`} aria-autocomplete="list"
          className="bg-transparent outline-none w-full font-bold text-sm placeholder:text-soft/70 [&::-webkit-search-cancel-button]:hidden" />
        {q && <button type="button" className="shrink-0 text-soft hover:text-ink" aria-label="Clear search" onClick={() => { setQ(''); setIdx(-1); }}><X size={16} /></button>}
      </div>
      {open && sug.length > 0 && (
        <ul id={`${id}-list`} role="listbox" className="clay-sm absolute left-0 right-0 mt-2 z-50 p-2 max-h-80 overflow-auto pop">
          {!q && <li className="px-3 py-1 text-xs font-extrabold text-soft uppercase">Try searching</li>}
          {sug.map((x, i) => (
            <li key={x.text + i} role="option" aria-selected={i === idx} onMouseDown={(e) => { e.preventDefault(); pick(x); }} onMouseEnter={() => setIdx(i)}
              className={`px-3 py-2 rounded-xl cursor-pointer font-bold text-sm flex items-center gap-2 ${i === idx ? 'bg-primary-light' : ''}`}>
              <Search size={14} className="text-soft" /><span className="truncate flex-1">{x.text}</span>{x.unit && <UnitBadge n={x.unit} />}
            </li>))}
        </ul>)}
    </div>
  );
}
export default function Navbar({ path }) {
  const [open, setOpen] = useState(false); const [sOpen, setSOpen] = useState(false);
  const { prefs } = useStore();
  useEffect(() => { setOpen(false); setSOpen(false); }, [path]);
  const active = (p) => (p === '/' ? path === '/' : path.startsWith(p) || (p === '/units' && path.startsWith('/unit')) || (p === '/programs' && (path.startsWith('/program') || path === '/favorites')) || (p === '/manage' && /^\/(new|edit|drafts|trash)/.test(path)));
  return (
    <header className="sticky top-0 z-40 px-3 sm:px-5 pt-3">
      <nav aria-label="Main navigation" className="clay mx-auto max-w-7xl !rounded-[26px] px-4 py-2.5 flex items-center gap-3">
        <a href={href('/')} className="flex items-center gap-2 font-extrabold text-lg shrink-0" aria-label="MCA Python Lab home">
          <span className="clay-primary clay-btn !p-0 w-10 h-10 !rounded-2xl"><Code2 size={22} /></span><span className="hidden sm:inline">MCA Python Lab</span><span className="sm:hidden">Python Lab</span>
        </a>
        <ul className="hidden xl:flex items-center gap-1 ml-3 flex-1">
          {NAV.map(([p, l]) => <li key={p}><a href={href(p)} aria-current={active(p) ? 'page' : undefined} className={`px-3 py-2 rounded-full font-extrabold text-sm whitespace-nowrap ${active(p) ? 'clay-inset !rounded-full text-primary' : 'text-soft hover:text-ink'}`}>{l}</a></li>)}
        </ul>
        <div className="hidden lg:block flex-1 xl:flex-none xl:w-64 2xl:w-80 ml-auto xl:ml-0"><SearchBar id="nav-search" /></div>
        <div className="ml-auto lg:ml-0 flex items-center gap-2">
          <a href={href('/favorites')} className="clay-btn clay-icon relative" aria-label={`Favorites (${prefs.favorites.length})`}><Heart size={18} />{prefs.favorites.length > 0 && <span className="absolute -top-1 -right-1 bg-rose-500 text-white text-[10px] font-extrabold rounded-full min-w-[18px] h-[18px] grid place-items-center px-1">{prefs.favorites.length}</span>}</a>
          <button className="clay-btn clay-icon lg:hidden" aria-label="Search" aria-expanded={sOpen} onClick={() => { setSOpen(!sOpen); setOpen(false); }}><Search size={18} /></button>
          <button className="clay-btn clay-icon xl:hidden" aria-label="Menu" aria-expanded={open} aria-controls="mobile-menu" onClick={() => { setOpen(!open); setSOpen(false); }}>{open ? <X size={18} /> : <Menu size={18} />}</button>
        </div>
      </nav>
      {sOpen && <div className="clay mx-auto max-w-7xl mt-2 p-3 lg:hidden"><SearchBar id="m-search" autoFocus onDone={() => setSOpen(false)} /></div>}
      {open && (
        <div id="mobile-menu" className="clay mx-auto max-w-7xl mt-2 p-3 xl:hidden pop">
          <ul className="grid grid-cols-2 gap-2">{NAV.map(([p, l]) => <li key={p}><a href={href(p)} aria-current={active(p) ? 'page' : undefined} className={`block px-4 py-3 rounded-2xl font-extrabold text-sm ${active(p) ? 'clay-inset !rounded-2xl text-primary' : 'clay-sm'}`}>{l}</a></li>)}</ul>
        </div>)}
    </header>
  );
}
