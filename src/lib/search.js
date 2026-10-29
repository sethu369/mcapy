import { UNITS } from '../data/syllabus.js';
const cache = new WeakMap();
const hay = (p) => {
  let h = cache.get(p);
  if (!h) {
    h = { title: p.title.toLowerCase(), desc: p.description.toLowerCase(), meta: [p.category, p.kind, ...(p.concepts || []), ...(p.tags || []), ...(p.topics || []), UNITS[p.unit - 1]?.title || ''].join(' ').toLowerCase(), code: p.code.toLowerCase(), file: p.filename.toLowerCase() };
    cache.set(p, h);
  }
  return h;
};
export const searchPrograms = (programs, q) => {
  const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
  if (!terms.length) return programs;
  const scored = [];
  for (const p of programs) {
    const h = hay(p); let score = 0, ok = true;
    for (const t of terms) {
      let s = 0;
      if (h.title.includes(t)) s += 10 + (h.title.startsWith(t) ? 3 : 0);
      if (h.meta.includes(t)) s += 5;
      if (h.file.includes(t)) s += 4;
      if (h.desc.includes(t)) s += 3;
      if (h.code.includes(t)) s += 1;
      if (!s) { ok = false; break; } score += s;
    }
    if (ok) scored.push([score, p]);
  }
  return scored.sort((a, b) => b[0] - a[0] || a[1].unit - b[1].unit || (a[1].number || 0) - (b[1].number || 0)).map((x) => x[1]);
};
export const EXAMPLE_SEARCHES = ['Integer', 'Factorial', 'Fibonacci', 'Lists', 'Tuples', 'Dictionary', 'Class', 'Inheritance', 'Exception', 'Array', 'Stack', 'Queue', 'SQLite'];
export const suggestions = (programs, q, max = 7) => {
  const t = q.trim().toLowerCase(); if (!t) return EXAMPLE_SEARCHES.slice(0, max).map((s) => ({ kind: 'term', text: s }));
  const out = [], seen = new Set();
  const terms = new Set();
  programs.forEach((p) => [...(p.tags || []), ...(p.concepts || []), p.category].forEach((x) => { if (x && x.toLowerCase().includes(t)) terms.add(x.toLowerCase()); }));
  [...terms].sort((a, b) => (a.startsWith(t) ? 0 : 1) - (b.startsWith(t) ? 0 : 1) || a.length - b.length).slice(0, 3).forEach((x) => { out.push({ kind: 'term', text: x }); seen.add(x); });
  programs.filter((p) => p.title.toLowerCase().includes(t)).slice(0, max - out.length).forEach((p) => out.push({ kind: 'program', text: p.title, id: p.id, unit: p.unit }));
  return out;
};
