import { useMemo, useRef, useState } from 'react';
import { Upload, FileCode2 } from 'lucide-react';
import { Modal, Confirm, toast, Spinner } from '../components/ui.jsx';
import { readFiles } from '../lib/importer.js';
import { useStore, importPrograms, suggestFilename, byId } from '../lib/store.js';
import { UNITS, UNIT_LABEL } from '../data/syllabus.js';

export default function ImportDialog({ open, onClose, defaultUnit = 1 }) {
  const s = useStore(); const input = useRef(null);
  const [rows, setRows] = useState([]), [ignored, setIgnored] = useState([]), [busy, setBusy] = useState(false), [bulkUnit, setBulkUnit] = useState(String(defaultUnit)), [confirm, setConfirm] = useState(false), [drag, setDrag] = useState(false);
  const reset = () => { setRows([]); setIgnored([]); };
  const load = async (files) => {
    setBusy(true);
    try { const r = await readFiles([...files], Number(bulkUnit)); setRows((x) => [...x, ...r.items.map((i) => ({ ...i, unit: Number(i.unit) || Number(bulkUnit), action: 'new' }))]); setIgnored((x) => [...x, ...r.ignored]); }
    finally { setBusy(false); }
  };
  // analyse duplicates against the live collection and within the batch
  const view = useMemo(() => {
    const seen = new Map();
    return rows.map((r) => {
      const dupFile = s.programs.find((p) => p.unit === r.unit && p.filename === r.filename);
      const dupId = r.id && byId(r.id, s);
      const key = `${r.unit}/${r.filename}`; const inBatch = seen.has(key); seen.set(key, true);
      const status = dupId ? 'Duplicate program ID' : dupFile ? 'Duplicate filename' : inBatch ? 'Duplicate in this batch' : 'New';
      const target = dupId || dupFile;
      return { ...r, status, target, dup: status !== 'New' };
    });
  }, [rows, s.programs]);
  const upd = (k, patch) => setRows((x) => x.map((r) => (r.key === k ? { ...r, ...patch } : r)));
  const doImport = () => {
    const batch = []; const taken = new Set();
    for (const r of view) {
      if (r.dup && r.action === 'skip') continue;
      if (r.dup && r.action === 'replace' && r.target) { batch.push({ ...r, action: 'replace', replaceId: r.target.id }); continue; }
      let filename = r.filename;
      const clash = (n) => s.programs.some((p) => p.unit === r.unit && p.filename === n) || taken.has(`${r.unit}/${n}`);
      if (clash(filename)) { if (r.action === 'rename' && r.newName && !clash(r.newName)) filename = r.newName; else { let i = 2; const b = filename.replace(/\.py$/, ''); while (clash(`${b}_${i}.py`)) i++; filename = `${b}_${i}.py`; } }
      taken.add(`${r.unit}/${filename}`); batch.push({ ...r, filename, action: 'new', id: r.dupId ? '' : r.id });
    }
    const res = importPrograms(batch); setConfirm(false);
    toast(`Imported ${res.added} new, replaced ${res.replaced}, skipped ${view.length - batch.length}.`); reset(); onClose();
  };
  const replaceCount = view.filter((r) => r.dup && r.action === 'replace').length;
  const importable = view.filter((r) => !(r.dup && r.action === 'skip')).length;
  return (
    <>
      <Modal open={open} onClose={() => { reset(); onClose(); }} wide title="Import Python Programs" footer={<>
        <button className="clay-btn" onClick={() => { reset(); onClose(); }}>Cancel</button>
        <button className="clay-btn clay-primary" disabled={!importable} onClick={() => (replaceCount ? setConfirm(true) : doImport())}>Import {importable || ''} program{importable === 1 ? '' : 's'}</button></>}>
        <p className="text-sm font-semibold text-soft mb-3">Add <b>.py</b> files (one or many) or a <b>.zip</b> of Python programs. Files are only read as text — they are never run. Nothing is overwritten without your confirmation.</p>
        <div className="grid sm:grid-cols-[1fr_auto] gap-3 items-end mb-4">
          <div><label className="label" htmlFor="imp-unit">Assign new files to</label><select id="imp-unit" className="clay-field" value={bulkUnit} onChange={(e) => { setBulkUnit(e.target.value); setRows((x) => x.map((r) => (r.fromManifest ? r : { ...r, unit: Number(e.target.value) }))); }}>{UNITS.map((u) => <option key={u.n} value={u.n}>{UNIT_LABEL(u.n)}</option>)}</select></div>
          <button className="clay-btn clay-primary" onClick={() => input.current?.click()}><Upload size={16} />Choose files…</button>
        </div>
        <input ref={input} type="file" multiple accept=".py,.zip" className="sr-only" aria-label="Choose .py or .zip files" onChange={(e) => { const picked = [...e.target.files]; load(picked).finally(() => { if (input.current) input.current.value = ''; }); }} />
        <div onDragOver={(e) => { e.preventDefault(); setDrag(true); }} onDragLeave={() => setDrag(false)} onDrop={(e) => { e.preventDefault(); setDrag(false); load(e.dataTransfer.files); }}
          className={`clay-tint p-5 text-center font-bold text-soft mb-4 ${drag ? 'ring-2 ring-primary' : ''}`}>{busy ? <span className="inline-flex items-center gap-2"><Spinner />Reading files…</span> : <><FileCode2 className="mx-auto mb-1 text-primary" />Drop .py or .zip files here</>}</div>
        {ignored.length > 0 && <details className="mb-4 clay-tint p-3"><summary className="font-extrabold text-amber-800 cursor-pointer">{ignored.length} file(s) skipped</summary><ul className="text-sm font-semibold mt-2 list-disc pl-5">{ignored.slice(0, 40).map((i, k) => <li key={k}>{i}</li>)}</ul></details>}
        {view.length > 0 && (
          <div className="overflow-x-auto"><table className="w-full text-left text-sm min-w-[760px]"><caption className="sr-only">Import preview</caption>
            <thead><tr className="text-soft"><th className="p-2">Filename</th><th className="p-2">Program title</th><th className="p-2">Size</th><th className="p-2">Unit</th><th className="p-2">Import status</th></tr></thead>
            <tbody>{view.map((r) => (
              <tr key={r.key} className="border-t border-primary/10 align-top">
                <td className="p-2 font-bold"><code>{r.filename}</code>{r.originalName !== r.filename && <span className="block text-xs text-soft">from {r.originalName}</span>}</td>
                <td className="p-2"><input aria-label={`Title for ${r.filename}`} className="clay-field !py-1.5" value={r.title} onChange={(e) => upd(r.key, { title: e.target.value })} /></td>
                <td className="p-2 font-semibold whitespace-nowrap">{r.size < 1024 ? `${r.size} B` : `${(r.size / 1024).toFixed(1)} KB`}</td>
                <td className="p-2"><select aria-label={`Unit for ${r.filename}`} className="clay-field !py-1.5" value={r.unit} onChange={(e) => upd(r.key, { unit: Number(e.target.value), fromManifest: false })}>{UNITS.map((u) => <option key={u.n} value={u.n}>Unit {u.n}</option>)}</select></td>
                <td className="p-2 min-w-[210px]">{!r.dup ? <span className="chip bg-mint-light text-mint-dark">Ready to import</span> : (
                  <div className="space-y-1"><span className="chip bg-amber-100 text-amber-800">{r.status}{r.target ? `: ${r.target.id}` : ''}</span>
                    <select aria-label={`Duplicate action for ${r.filename}`} className="clay-field !py-1.5" value={r.action} onChange={(e) => upd(r.key, { action: e.target.value, newName: r.newName || suggestFilename(r.filename.replace(/\.py$/, ''), r.unit) })}>
                      <option value="new">Import as new program (auto-rename)</option><option value="skip">Skip</option><option value="rename">Rename…</option><option value="replace" disabled={!r.target}>Replace existing</option></select>
                    {r.action === 'rename' && <input aria-label="New filename" className="clay-field !py-1.5" value={r.newName || ''} onChange={(e) => upd(r.key, { newName: e.target.value })} />}</div>)}</td>
              </tr>))}</tbody></table></div>)}
      </Modal>
      <Confirm open={confirm} danger title="Replace existing programs?" confirmLabel="Replace & import" onCancel={() => setConfirm(false)} onConfirm={doImport}>
        <p className="font-semibold">{replaceCount} existing program(s) will have their code replaced by the imported files. Their previous code is kept in Version History so you can restore it.</p></Confirm>
    </>
  );
}
