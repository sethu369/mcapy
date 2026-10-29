import { useSyncExternalStore } from 'react';
import seed from '../data/programs.json';
import { detectDeps } from './python.js';

const DB_NAME = 'mca-python-lab', STORE = 'kv', KEY = 'state-v1';
export const DIFFICULTIES = ['Beginner', 'Intermediate', 'Advanced'];
export const KINDS = ['Demonstration', 'Interactive', 'Application', 'Terminal Commands'];
const SEED_DATE = '2026-10-28T00:00:00.000Z';

/* ---------------- persistence (IndexedDB, with localStorage fallback) ---------------- */
const idb = () => new Promise((res, rej) => {
  try {
    const r = indexedDB.open(DB_NAME, 1);
    r.onupgradeneeded = () => r.result.createObjectStore(STORE);
    r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
  } catch (e) { rej(e); }
});
async function dbGet() {
  try { const db = await idb(); return await new Promise((res, rej) => { const q = db.transaction(STORE).objectStore(STORE).get(KEY); q.onsuccess = () => res(q.result); q.onerror = () => rej(q.error); }); }
  catch { try { const t = localStorage.getItem('mca-state-fallback'); return t ? JSON.parse(t) : undefined; } catch { return undefined; } }
}
let storageMode = 'indexeddb';
async function dbSet(v) {
  try { const db = await idb(); await new Promise((res, rej) => { const tx = db.transaction(STORE, 'readwrite'); tx.objectStore(STORE).put(v, KEY); tx.oncomplete = res; tx.onerror = () => rej(tx.error); }); storageMode = 'indexeddb'; }
  catch { try { localStorage.setItem('mca-state-fallback', JSON.stringify(v)); storageMode = 'localstorage'; } catch { storageMode = 'memory'; } }
}
export const getStorageMode = () => storageMode;
const lsGet = (k, d) => { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch { return d; } };
const lsSet = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* storage unavailable */ } };

/* ---------------- state ---------------- */
const fromSeed = () => {
  const programs = seed.map((p) => ({
    id: p.id, unit: p.unit, number: p.number, title: p.title, category: p.category, difficulty: p.difficulty,
    description: p.description, concepts: p.concepts, code: p.code, algorithm: p.algorithm, explanation: p.explanation,
    sampleInput: p.sampleInput, sampleOutput: p.sampleOutput, filename: p.filename, tags: p.tags, topics: p.topics,
    deps: p.deps, kind: p.kind, args: p.args, createdAt: SEED_DATE, updatedAt: SEED_DATE, status: 'published', origin: 'seed', version: 1,
  }));
  const counters = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, d: 0 };
  programs.forEach((p) => { counters[p.unit] = Math.max(counters[p.unit], p.number); });
  return { programs, versions: {}, counters };
};
let state = { ready: false, ...fromSeed(), prefs: { favorites: lsGet('mca.fav', []), progress: lsGet('mca.progress', {}), recent: lsGet('mca.recent', []), practiceDone: lsGet('mca.practice', []) } };
const subs = new Set();
const emit = () => { state = { ...state }; subs.forEach((f) => f()); };
let timer = null;
const persist = () => { clearTimeout(timer); timer = setTimeout(() => dbSet({ programs: state.programs, versions: state.versions, counters: state.counters }), 150); };
export const subscribe = (f) => { subs.add(f); return () => subs.delete(f); };
export const getState = () => state;
export const useStore = () => useSyncExternalStore(subscribe, getState);

export async function initStore() {
  const saved = await dbGet();
  if (saved && Array.isArray(saved.programs)) {
    state = { ...state, programs: saved.programs, versions: saved.versions || {}, counters: saved.counters || state.counters, ready: true };
  } else { state = { ...state, ready: true }; }
  subs.forEach((f) => f());
}

/* ---------------- selectors ---------------- */
export const published = (s = state) => s.programs.filter((p) => p.status === 'published');
export const drafts = (s = state) => s.programs.filter((p) => p.status === 'draft');
export const trashed = (s = state) => s.programs.filter((p) => p.status === 'trashed');
export const byId = (id, s = state) => s.programs.find((p) => p.id === id);
export const versionsOf = (id, s = state) => s.versions[id] || [];

/* ---------------- validation ---------------- */
const RESERVED = /^(con|prn|aux|nul|com\d|lpt\d)\.py$/i;
export const slug = (t) => (t || '').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '').slice(0, 50);
export const suggestFilename = (title, unit, ignoreId) => {
  let base = slug(title) || 'program', name = base + '.py', i = 2;
  while (state.programs.some((p) => p.id !== ignoreId && p.unit === unit && p.filename === name)) name = `${base}_${i++}.py`;
  return name;
};
export function validate(d, { mode = 'publish', existingId = null } = {}) {
  const e = {}, isDraft = mode === 'draft';
  if (!String(d.title || '').trim()) e.title = 'Program title is required.';
  if (!isDraft) {
    if (![1, 2, 3, 4, 5].includes(Number(d.unit))) e.unit = 'Please choose a syllabus unit.';
    if (!String(d.code || '').trim()) e.code = 'Python source code is required.';
    if (!String(d.category || '').trim()) e.category = 'Category is required.';
    if (!DIFFICULTIES.includes(d.difficulty)) e.difficulty = 'Choose Beginner, Intermediate or Advanced.';
    if (!String(d.description || '').trim()) e.description = 'Description is required.';
  }
  const fn = String(d.filename || '').trim();
  if (fn || !isDraft) {
    if (!fn) e.filename = 'Python filename is required (e.g. check_integer.py).';
    else if (!/^[A-Za-z0-9_][A-Za-z0-9_-]{0,79}\.py$/.test(fn)) e.filename = 'Filename must be letters, digits, "_" or "-", end with .py and contain no spaces or folders.';
    else if (RESERVED.test(fn)) e.filename = 'This filename is reserved by the operating system.';
    else if (Number(d.unit) && state.programs.some((p) => p.id !== existingId && p.unit === Number(d.unit) && p.filename.toLowerCase() === fn.toLowerCase())) {
      const clash = state.programs.find((p) => p.id !== existingId && p.unit === Number(d.unit) && p.filename.toLowerCase() === fn.toLowerCase());
      e.filename = `Unit ${d.unit} already has "${fn}"${clash?.status === 'trashed' ? ' (in Trash)' : ''}. Use a different name, e.g. ${suggestFilename(fn.replace(/\.py$/, ''), Number(d.unit), existingId)}.`;
      e.filenameSuggestion = suggestFilename(fn.replace(/\.py$/, ''), Number(d.unit), existingId);
    }
  }
  const id = String(d.id || '').trim();
  if (id) {
    if (!/^[A-Za-z0-9][A-Za-z0-9_-]{1,59}$/.test(id)) e.id = 'Program ID may contain letters, digits, "-" and "_" only (2-60 characters).';
    else if (state.programs.some((p) => p.id.toLowerCase() === id.toLowerCase() && p.id !== existingId)) e.id = `Program ID "${id}" is already used. IDs are never reused, even after deletion.`;
  }
  return e;
}

/* ---------------- helpers ---------------- */
const now = () => new Date().toISOString();
const list = (v) => (Array.isArray(v) ? v : String(v || '').split(/[,\n]/)).map((s) => s.trim()).filter(Boolean);
const lines = (v) => (Array.isArray(v) ? v : String(v || '').split('\n')).map((s) => s.replace(/^\s*\d+[.)]\s*/, '').trim()).filter(Boolean);
export function nextId(unit) {
  const u = Number(unit) || 'd';
  let n = state.counters[u] || 0, id;
  const prefix = u === 'd' ? 'draft-' : `unit${u}-program-`;
  do { n += 1; id = `${prefix}${String(n).padStart(3, '0')}`; } while (state.programs.some((p) => p.id.toLowerCase() === id.toLowerCase()) || (state.versions[id]));
  return { id, n };
}
const normalise = (d, base = {}) => ({
  ...base, title: String(d.title || '').trim(), unit: Number(d.unit) || null, category: String(d.category || '').trim(),
  difficulty: d.difficulty || 'Beginner', description: String(d.description || '').trim(), code: String(d.code || '').replace(/\r\n?/g, '\n'),
  algorithm: lines(d.algorithm), explanation: String(d.explanation || '').trim(), sampleInput: String(d.sampleInput || ''),
  sampleOutput: String(d.sampleOutput || ''), concepts: list(d.concepts), tags: list(d.tags), filename: String(d.filename || '').trim(),
  kind: d.kind || base.kind || 'Demonstration', topics: base.topics || [], args: base.args || [],
});
const withDeps = (p) => ({ ...p, deps: [...new Set([...(p.deps || []), ...detectDeps(p.code)])] });

/* ---------------- CRUD ---------------- */
export function createProgram(d, mode = 'publish') {
  const errors = validate(d, { mode });
  if (Object.keys(errors).length) return { ok: false, errors };
  const unit = Number(d.unit) || 'd';
  let id = String(d.id || '').trim(), number = null;
  if (mode === 'draft' && !Number(d.unit)) { const g = nextId('d'); if (!id) id = g.id; state.counters.d = Math.max(state.counters.d, g.n); }
  else {
    const g = nextId(unit); number = g.n; state.counters[unit] = Math.max(state.counters[unit] || 0, g.n);
    if (!id) id = g.id;
  }
  const t = now();
  const p = withDeps({ ...normalise(d), id, number, status: mode === 'draft' ? 'draft' : 'published', origin: 'user', createdAt: t, updatedAt: t, version: 1 });
  state.programs = [...state.programs, p]; persist(); emit();
  return { ok: true, program: p };
}
export function updateProgram(id, d, { keepVersion = true, note = '' } = {}) {
  const old = byId(id); if (!old) return { ok: false, errors: { _: 'Program not found.' } };
  const mode = old.status === 'draft' ? 'draft' : 'publish';
  const errors = validate({ ...d, id }, { mode, existingId: id });
  if (Object.keys(errors).length) return { ok: false, errors };
  const t = now();
  let number = old.number, unit = Number(d.unit) || old.unit;
  if (unit && unit !== old.unit) { const g = nextId(unit); number = g.n; state.counters[unit] = Math.max(state.counters[unit] || 0, g.n); }
  const p = withDeps({ ...normalise(d, old), id, number, unit, updatedAt: t, version: (old.version || 1) + 1 });
  const changed = ['title', 'unit', 'category', 'difficulty', 'description', 'code', 'algorithm', 'explanation', 'sampleInput', 'sampleOutput', 'concepts', 'tags', 'filename'].some((k) => JSON.stringify(old[k]) !== JSON.stringify(p[k]));
  if (!changed) return { ok: true, program: old, unchanged: true };
  if (keepVersion) state.versions = { ...state.versions, [id]: [...(state.versions[id] || []), { ...old, savedAt: t, note }] };
  state.programs = state.programs.map((x) => (x.id === id ? p : x)); persist(); emit();
  return { ok: true, program: p };
}
const setStatus = (id, status) => { state.programs = state.programs.map((p) => (p.id === id ? { ...p, status, updatedAt: now(), ...(status === 'trashed' ? { trashedAt: now(), statusBeforeTrash: p.status } : {}) } : p)); persist(); emit(); };
export const trashProgram = (id) => setStatus(id, 'trashed');
export function restoreProgram(id) {
  const p = byId(id); if (!p) return { ok: false };
  const e = validate(p, { mode: 'publish', existingId: id });
  const back = p.statusBeforeTrash === 'draft' ? 'draft' : 'published';
  if (back === 'published' && e.filename) return { ok: false, errors: e };
  setStatus(id, back); return { ok: true };
}
export function purgeProgram(id) {
  state.programs = state.programs.filter((p) => p.id !== id);
  // keep versions entry marker so the ID can never be reused
  state.versions = { ...state.versions, [id]: state.versions[id] || [] };
  const pr = { ...state.prefs, favorites: state.prefs.favorites.filter((x) => x !== id), recent: state.prefs.recent.filter((x) => x !== id), progress: { ...state.prefs.progress } };
  delete pr.progress[id]; state.prefs = pr; lsSet('mca.fav', pr.favorites); lsSet('mca.recent', pr.recent); lsSet('mca.progress', pr.progress);
  persist(); emit();
}
export function publishDraft(id, d) {
  const old = byId(id); if (!old) return { ok: false, errors: { _: 'Draft not found.' } };
  const data = d || old; const errors = validate({ ...data, id }, { mode: 'publish', existingId: id });
  if (Object.keys(errors).length) return { ok: false, errors };
  const unit = Number(data.unit); let number = old.number;
  if (old.unit !== unit || number == null) { const g = nextId(unit); number = g.n; state.counters[unit] = Math.max(state.counters[unit] || 0, g.n); }
  const p = withDeps({ ...normalise(data, old), id, unit, number, status: 'published', updatedAt: now() });
  state.programs = state.programs.map((x) => (x.id === id ? p : x)); persist(); emit();
  return { ok: true, program: p };
}
export function restoreVersion(id, versionNo) {
  const snap = (state.versions[id] || []).find((v) => v.version === versionNo); const cur = byId(id);
  if (!snap || !cur) return { ok: false };
  const t = now();
  const keep = (({ title, unit, category, difficulty, description, code, algorithm, explanation, sampleInput, sampleOutput, concepts, tags, filename }) => ({ title, unit, category, difficulty, description, code, algorithm, explanation, sampleInput, sampleOutput, concepts, tags, filename }))(snap);
  const e = validate({ ...keep, id }, { mode: 'publish', existingId: id });
  if (e.filename) keep.filename = suggestFilename(keep.filename.replace(/\.py$/, ''), keep.unit, id);
  state.versions = { ...state.versions, [id]: [...state.versions[id], { ...cur, savedAt: t, note: `Before restoring version ${versionNo}` }] };
  const p = withDeps({ ...cur, ...keep, updatedAt: t, version: cur.version + 1, restoredFrom: versionNo });
  state.programs = state.programs.map((x) => (x.id === id ? p : x)); persist(); emit();
  return { ok: true, program: p };
}
// items: [{filename,title,code,unit,action:'new'|'replace', replaceId}]
export function importPrograms(items) {
  let added = 0, replaced = 0; const t = now(); const out = [];
  for (const it of items) {
    if (it.action === 'replace' && byId(it.replaceId)) {
      const r = updateProgram(it.replaceId, { ...byId(it.replaceId), code: it.code, title: it.title || byId(it.replaceId).title, filename: byId(it.replaceId).filename }, { note: 'Replaced by import' });
      if (r.ok) { replaced++; out.push(it.replaceId); } continue;
    }
    const filename = it.filename;
    const r = createProgram({ id: it.id && !byId(it.id) ? it.id : '', title: it.title, unit: it.unit, category: it.category || 'Imported', difficulty: it.difficulty || 'Beginner', description: it.description || `Imported from ${it.originalName || filename}.`, code: it.code, filename, concepts: [], tags: ['imported'], algorithm: '', explanation: 'Imported program. Add an explanation by editing this program.' });
    if (r.ok) { added++; out.push(r.program.id); }
  }
  return { added, replaced, ids: out };
}
export function resetCollection() {
  const s = fromSeed(); state.programs = s.programs; state.versions = {}; state.counters = s.counters; persist(); emit();
}

/* ---------------- local preferences ---------------- */
const setPrefs = (patch) => { state.prefs = { ...state.prefs, ...patch }; emit(); };
export function toggleFavorite(id) {
  const f = state.prefs.favorites; const n = f.includes(id) ? f.filter((x) => x !== id) : [...f, id]; lsSet('mca.fav', n); setPrefs({ favorites: n });
}
export const PROGRESS = ['Not Started', 'Practicing', 'Completed'];
export function setProgress(id, status) {
  const p = { ...state.prefs.progress }; if (status === 'Not Started') delete p[id]; else p[id] = status; lsSet('mca.progress', p); setPrefs({ progress: p });
}
export const progressOf = (id, s = state) => s.prefs.progress[id] || 'Not Started';
export function addRecent(id) {
  const r = [id, ...state.prefs.recent.filter((x) => x !== id)].slice(0, 12); lsSet('mca.recent', r); setPrefs({ recent: r });
}
export function togglePracticeDone(id) {
  const d = state.prefs.practiceDone; const n = d.includes(id) ? d.filter((x) => x !== id) : [...d, id]; lsSet('mca.practice', n); setPrefs({ practiceDone: n });
}
export function importPrefs(favorites, progress) { lsSet('mca.fav', favorites); lsSet('mca.progress', progress); setPrefs({ favorites, progress }); }
