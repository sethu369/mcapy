import { useEffect, useMemo, useRef, useState } from 'react';
import { Save, FileClock, Eraser, X, Eye, RotateCcw, Rocket } from 'lucide-react';
import { useStore, byId, createProgram, updateProgram, publishDraft, DIFFICULTIES, KINDS, nextId, suggestFilename, validate } from '../lib/store.js';
import { go, setGuard, href } from '../lib/router.js';
import { UNITS, UNIT_LABEL } from '../data/syllabus.js';
import { Field, toast, Modal, Confirm, Empty, PageTitle, DiffBadge, UnitBadge } from '../components/ui.jsx';
import CodeEditor from '../components/CodeEditor.jsx';
import CodeViewer from '../components/CodeViewer.jsx';
import { SearchX } from 'lucide-react';

const blank = (unit = '') => ({ id: '', title: '', unit: unit ? String(unit) : '', category: '', difficulty: 'Beginner', kind: 'Demonstration', description: '', code: '', algorithm: '', explanation: '', sampleInput: '', sampleOutput: '', concepts: '', tags: '', filename: '' });
const toForm = (p) => ({ id: p.id, title: p.title, unit: p.unit ? String(p.unit) : '', category: p.category || '', difficulty: p.difficulty || 'Beginner', kind: p.kind || 'Demonstration', description: p.description || '', code: p.code || '', algorithm: (p.algorithm || []).join('\n'), explanation: p.explanation || '', sampleInput: p.sampleInput || '', sampleOutput: p.sampleOutput || '', concepts: (p.concepts || []).join(', '), tags: (p.tags || []).join(', '), filename: p.filename || '' });

export default function ProgramForm({ id, route }) {
  const s = useStore(); const existing = id ? byId(id, s) : null;
  const isEdit = !!existing; const isDraft = existing?.status === 'draft';
  const initial = useMemo(() => (existing ? toForm(existing) : blank(route.q.unit)), [existing?.id]); // eslint-disable-line
  const [f, setF] = useState(initial); const [err, setErr] = useState({}); const [keep, setKeep] = useState(true);
  const [fnTouched, setFnTouched] = useState(isEdit); const [prev, setPrev] = useState(false), [clear, setClear] = useState(false), [reset, setReset] = useState(false);
  const dirty = JSON.stringify(f) !== JSON.stringify(initial);
  const dref = useRef(dirty); dref.current = dirty;
  useEffect(() => { setGuard(() => dref.current); return () => setGuard(null); }, []);
  useEffect(() => { setF(initial); setErr({}); }, [initial]);
  const cats = useMemo(() => [...new Set(s.programs.filter((p) => !f.unit || String(p.unit) === f.unit).map((p) => p.category))].filter(Boolean).sort(), [s.programs, f.unit]);
  if (id && !existing) return <Empty icon={SearchX} title="Program not found">It may have been permanently deleted.</Empty>;
  const set = (k) => (e) => { const v = e.target ? e.target.value : e; setF((x) => { const n = { ...x, [k]: v }; if (k === 'title' && !fnTouched) n.filename = v.trim() ? suggestFilename(v, Number(x.unit) || null, existing?.id) : ''; return n; }); setErr((x) => ({ ...x, [k]: undefined })); };
  const autoId = !isEdit && f.unit ? nextId(f.unit).id : 'generated automatically';
  const leave = (to) => { go(to); };
  const done = (p, msg) => { setGuard(null); toast(msg); go(`/program/${p.id}`); };
  const fail = (e) => { setErr(e); toast('Please fix the highlighted fields.', 'error'); setTimeout(() => document.querySelector('[role="alert"]')?.scrollIntoView({ block: 'center', behavior: 'smooth' }), 50); };
  const save = () => {
    if (isEdit && !isDraft) { const r = updateProgram(existing.id, f, { keepVersion: keep }); if (!r.ok) return fail(r.errors); r.unchanged ? (setGuard(null), toast('No changes to save.', 'info'), go(`/program/${existing.id}`)) : done(r.program, `Changes saved. “${r.program.title}” is now version ${r.program.version}.`); }
    else if (isDraft) { const r = publishDraft(existing.id, f); if (!r.ok) return fail(r.errors); done(r.program, `“${r.program.title}” published to Unit ${r.program.unit}.`); }
    else { const r = createProgram(f, 'publish'); if (!r.ok) return fail(r.errors); done(r.program, `Program saved to Unit ${r.program.unit}. Total programs updated; it is now searchable and included in ZIP downloads.`); }
  };
  const saveDraft = () => {
    const r = isDraft ? updateProgram(existing.id, f, { keepVersion: false }) : createProgram(f, 'draft'); if (!r.ok) return fail(r.errors);
    setGuard(null); toast('Draft saved. It is not part of the published collection until you publish it.'); go('/drafts');
  };
  const sample = suggestFilename(f.title || 'program', Number(f.unit) || null, existing?.id);
  return (
    <form onSubmit={(e) => { e.preventDefault(); save(); }} noValidate className="space-y-6">
      <PageTitle title={isDraft ? 'Edit Draft' : isEdit ? 'Edit Program' : 'Add New Program'} sub={isEdit ? `${existing.title} · ${existing.id}` : 'Create a new Python program in any syllabus unit.'}>
        {dirty && <span className="chip bg-amber-100 text-amber-800 !text-sm" role="status">● Unsaved Changes</span>}
      </PageTitle>
      <section className="clay p-5 sm:p-7 grid md:grid-cols-2 gap-5" aria-label="Program details">
        <div className="md:col-span-2"><Field label="Program title" required error={err.title} htmlFor="f-title"><input id="f-title" className="clay-field" value={f.title} onChange={set('title')} placeholder="e.g. Check Whether a Number Is an Integer" /></Field></div>
        <Field label="Program ID" error={err.id} htmlFor="f-id" hint={isEdit ? 'The original ID is preserved and cannot be changed.' : `Leave blank to auto-generate (next: ${autoId}). IDs are never reused.`}>
          <input id="f-id" className="clay-field" value={f.id} onChange={set('id')} readOnly={isEdit} placeholder={autoId} /></Field>
        <Field label="Unit" required error={err.unit} htmlFor="f-unit"><select id="f-unit" className="clay-field" value={f.unit} onChange={set('unit')}><option value="">Select a unit…</option>{UNITS.map((u) => <option key={u.n} value={u.n}>{UNIT_LABEL(u.n)}</option>)}</select></Field>
        <Field label="Category / Topic" required error={err.category} htmlFor="f-cat" hint="Choose an existing topic or type a new one."><input id="f-cat" list="cat-list" className="clay-field" value={f.category} onChange={set('category')} placeholder="e.g. Data Types" /><datalist id="cat-list">{cats.map((c) => <option key={c} value={c} />)}</datalist></Field>
        <div className="grid grid-cols-2 gap-4">
          <Field label="Difficulty" required error={err.difficulty} htmlFor="f-diff"><select id="f-diff" className="clay-field" value={f.difficulty} onChange={set('difficulty')}>{DIFFICULTIES.map((d) => <option key={d}>{d}</option>)}</select></Field>
          <Field label="Program type" htmlFor="f-kind"><select id="f-kind" className="clay-field" value={f.kind} onChange={set('kind')}>{KINDS.map((d) => <option key={d}>{d}</option>)}</select></Field></div>
        <div className="md:col-span-2"><Field label="Python filename" required error={err.filename} htmlFor="f-file" hint={`Letters, digits, _ or - ending in .py. Suggestion: ${sample}`}>
          <div className="flex gap-2"><input id="f-file" className="clay-field" value={f.filename} onChange={(e) => { setFnTouched(true); set('filename')(e); }} placeholder="check_integer.py" />
            {err.filenameSuggestion && <button type="button" className="clay-btn clay-mint shrink-0" onClick={() => { setF({ ...f, filename: err.filenameSuggestion }); setErr({ ...err, filename: undefined }); }}>Use {err.filenameSuggestion}</button>}</div></Field></div>
        <div className="md:col-span-2"><Field label="Description" required error={err.description} htmlFor="f-desc"><textarea id="f-desc" rows={2} className="clay-field" value={f.description} onChange={set('description')} placeholder="One or two sentences on what the program does." /></Field></div>
        <Field label="Concepts used" htmlFor="f-con" hint="Comma separated, e.g. input, int(), try-except"><input id="f-con" className="clay-field" value={f.concepts} onChange={set('concepts')} /></Field>
        <Field label="Tags" htmlFor="f-tags" hint="Comma separated search words"><input id="f-tags" className="clay-field" value={f.tags} onChange={set('tags')} /></Field>
      </section>
      <section className="clay p-5 sm:p-7" aria-label="Python source code">
        <h2 className="font-extrabold text-xl mb-1">Python source code <span className="text-rose-600">*</span></h2>
        <p className="text-sm font-semibold text-soft mb-4">Edit freely. Tab / Shift+Tab indent, Ctrl+F opens Find. Your code is saved exactly as typed.</p>
        <CodeEditor value={f.code} onChange={(v) => { setF((x) => ({ ...x, code: v })); setErr((x) => ({ ...x, code: undefined })); }} filename={f.filename || 'program.py'} dirty={dirty && f.code !== initial.code} error={err.code} />
        {err.code && <p className="text-sm text-rose-700 font-bold mt-2" role="alert">{err.code}</p>}
      </section>
      <section className="clay p-5 sm:p-7 grid md:grid-cols-2 gap-5" aria-label="Explanation and samples">
        <Field label="Algorithm" htmlFor="f-alg" hint="One step per line."><textarea id="f-alg" rows={6} className="clay-field font-mono text-sm" value={f.algorithm} onChange={set('algorithm')} /></Field>
        <Field label="Explanation" htmlFor="f-exp"><textarea id="f-exp" rows={6} className="clay-field" value={f.explanation} onChange={set('explanation')} /></Field>
        <Field label="Sample input" htmlFor="f-in"><textarea id="f-in" rows={4} className="clay-field font-mono text-sm" value={f.sampleInput} onChange={set('sampleInput')} /></Field>
        <Field label="Sample output" htmlFor="f-out" hint="Type the output you expect; the website never runs your code."><textarea id="f-out" rows={4} className="clay-field font-mono text-sm" value={f.sampleOutput} onChange={set('sampleOutput')} /></Field>
      </section>
      <div className="clay p-4 flex flex-wrap gap-3 items-center sticky bottom-3 z-20">
        {isEdit && !isDraft && <label className="flex items-center gap-2 font-bold text-sm mr-auto"><input type="checkbox" className="w-5 h-5 accent-[#5b4fd9]" checked={keep} onChange={(e) => setKeep(e.target.checked)} />Save previous version</label>}
        {!isEdit || isDraft ? <span className="mr-auto" /> : null}
        {!isEdit && <><button type="submit" className="clay-btn clay-primary"><Save size={17} />Save Program</button>
          <button type="button" className="clay-btn" onClick={saveDraft}><FileClock size={17} />Save as Draft</button>
          <button type="button" className="clay-btn" onClick={() => setClear(true)}><Eraser size={17} />Clear Form</button></>}
        {isDraft && <><button type="submit" className="clay-btn clay-primary"><Rocket size={17} />Publish Program</button><button type="button" className="clay-btn" onClick={saveDraft}><FileClock size={17} />Save Draft</button></>}
        {isEdit && !isDraft && <><button type="submit" className="clay-btn clay-primary"><Save size={17} />Save Changes</button>
          <button type="button" className="clay-btn" onClick={() => setPrev(true)}><Eye size={17} />Preview Changes</button>
          <button type="button" className="clay-btn" disabled={!dirty} onClick={() => setReset(true)}><RotateCcw size={17} />Reset Changes</button></>}
        <button type="button" className="clay-btn" onClick={() => leave(isEdit && !isDraft ? `/program/${existing.id}` : isDraft ? '/drafts' : '/manage')}><X size={17} />Cancel</button>
      </div>
      <Modal open={prev} onClose={() => setPrev(false)} wide title="Preview of your changes">
        <div className="space-y-4"><div className="flex flex-wrap gap-2">{Number(f.unit) > 0 && <UnitBadge n={Number(f.unit)} />}<span className="chip">{f.category}</span><DiffBadge d={f.difficulty} /></div>
          <h3 className="text-2xl font-extrabold">{f.title}</h3><p className="font-semibold text-soft">{f.description}</p>
          {f.algorithm.trim() && <ol className="list-decimal pl-6 font-semibold space-y-1">{f.algorithm.split('\n').filter(Boolean).map((a, i) => <li key={i}>{a}</li>)}</ol>}
          <CodeViewer code={f.code} filename={f.filename} />
          {f.explanation && <p className="font-semibold whitespace-pre-line">{f.explanation}</p>}
          <p className="text-xs font-bold text-soft">Preview only — nothing has been saved or executed.</p></div>
      </Modal>
      <Confirm open={clear} danger title="Clear the whole form?" confirmLabel="Clear Form" onCancel={() => setClear(false)} onConfirm={() => { setF(blank()); setErr({}); setFnTouched(false); setClear(false); }}><p className="font-semibold">All fields, including the code, will be emptied.</p></Confirm>
      <Confirm open={reset} title="Reset changes?" confirmLabel="Reset Changes" onCancel={() => setReset(false)} onConfirm={() => { setF(initial); setErr({}); setReset(false); toast('Form reset to the saved version', 'info'); }}><p className="font-semibold">Everything you changed since opening this page will be discarded.</p></Confirm>
    </form>
  );
}
