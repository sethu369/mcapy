import { useState, useMemo } from 'react';
import { ArrowLeft, RotateCcw, Download, GitCompare, Eye } from 'lucide-react';
import { useStore, byId, versionsOf, restoreVersion } from '../lib/store.js';
import { href } from '../lib/router.js';
import { Confirm, Empty, toast, fmtDate } from '../components/ui.jsx';
import { diffLines } from '../lib/diff.js';
import { downloadPython } from '../lib/zip.js';
import { CodeBody } from '../components/CodeViewer.jsx';
import { History } from 'lucide-react';

export default function Versions({ id }) {
  const s = useStore(); const cur = byId(id, s);
  const old = versionsOf(id, s);
  const rows = useMemo(() => cur ? [...old.map((v) => ({ ...v, isCurrent: false })), { ...cur, isCurrent: true, savedAt: cur.updatedAt }].sort((a, b) => b.version - a.version) : [], [old, cur]);
  const [view, setView] = useState(null), [cmpA, setCmpA] = useState(null), [cmpB, setCmpB] = useState(null), [rest, setRest] = useState(null);
  if (!cur) return <Empty icon={History} title="Program not found" />;
  const find = (n) => rows.find((r) => r.version === n);
  const a = find(cmpA), b = find(cmpB);
  const diff = a && b ? diffLines(a.code, b.code) : null;
  const viewing = view != null ? find(view) : null;
  return (
    <div className="space-y-6">
      <a href={href(`/program/${id}`)} className="inline-flex items-center gap-1 font-extrabold text-soft hover:text-primary"><ArrowLeft size={16} />Back to program</a>
      <header><h1 className="text-3xl font-extrabold">Version History</h1><p className="text-soft font-semibold">{cur.title} · <code>{cur.id}</code> · {rows.length} version(s)</p></header>
      {rows.length === 1 && <div className="clay-tint p-4 font-bold">No earlier versions yet. A version is saved automatically each time you edit and save this program (keep “Save previous version” ticked).</div>}
      <div className="clay p-3 sm:p-5 overflow-x-auto"><table className="w-full text-left min-w-[640px]"><caption className="sr-only">Versions</caption>
        <thead><tr className="text-soft text-sm"><th className="p-2">Version</th><th className="p-2">Updated</th><th className="p-2">Title</th><th className="p-2">Compare</th><th className="p-2 text-right">Actions</th></tr></thead>
        <tbody>{rows.map((r) => (
          <tr key={r.version} className="border-t border-primary/10 align-middle">
            <td className="p-2 font-extrabold">v{r.version} {r.isCurrent && <span className="chip bg-mint-light text-mint-dark ml-1">Current</span>}</td>
            <td className="p-2 text-sm font-semibold">{fmtDate(r.savedAt || r.updatedAt)}{r.note && <span className="block text-xs text-soft">{r.note}</span>}</td>
            <td className="p-2 font-bold">{r.title}</td>
            <td className="p-2"><div className="flex gap-3 text-xs font-extrabold">
              <label className="flex items-center gap-1"><input type="radio" name="ca" checked={cmpA === r.version} onChange={() => setCmpA(r.version)} />A</label>
              <label className="flex items-center gap-1"><input type="radio" name="cb" checked={cmpB === r.version} onChange={() => setCmpB(r.version)} />B</label></div></td>
            <td className="p-2"><div className="flex gap-2 justify-end">
              <button className="clay-btn btn-sm" onClick={() => setView(view === r.version ? null : r.version)}><Eye size={14} />View</button>
              <button className="clay-btn btn-sm" onClick={() => { downloadPython({ code: r.code, filename: r.filename.replace(/\.py$/, `_v${r.version}.py`) }); toast(`Downloaded version ${r.version}`); }}><Download size={14} />Download</button>
              {!r.isCurrent && <button className="clay-btn btn-sm clay-mint" onClick={() => setRest(r)}><RotateCcw size={14} />Restore</button>}</div></td>
          </tr>))}</tbody></table></div>
      {viewing && <section className="clay p-5"><h2 className="font-extrabold text-lg mb-3">Version {viewing.version}: {viewing.title} <code className="text-sm text-soft">{viewing.filename}</code></h2><CodeBody code={viewing.code} /></section>}
      <section className="clay p-5" aria-label="Compare versions">
        <h2 className="font-extrabold text-lg mb-1 flex items-center gap-2"><GitCompare size={18} className="text-primary" />Compare versions</h2>
        <p className="text-sm text-soft font-semibold mb-3">Pick A and B in the table above. <span className="text-rose-700">Red = only in A</span>, <span className="text-mint-dark">green = only in B</span>.</p>
        {!diff ? <p className="font-bold text-soft">Select one version as A and another as B.</p> : (
          <div className="codebox overflow-auto max-h-[32rem]"><pre className="code-font py-3 min-w-max">{diff.map((d, i) => <div key={i} className={`px-4 whitespace-pre ${d.t === 'add' ? 'bg-emerald-100 text-emerald-900' : d.t === 'del' ? 'bg-rose-100 text-rose-900' : ''}`}>{d.t === 'add' ? '+ ' : d.t === 'del' ? '- ' : '  '}{d.s || ' '}</div>)}</pre></div>)}
        {diff && !diff.some((d) => d.t !== 'same') && <p className="font-bold text-mint-dark mt-2">The two versions have identical code.</p>}
      </section>
      <Confirm open={!!rest} title={`Restore version ${rest?.version}?`} confirmLabel="Restore this version" onCancel={() => setRest(null)} onConfirm={() => { const r = restoreVersion(id, rest.version); setRest(null); r.ok ? toast(`Version ${rest.version} restored as the new current version (v${r.program.version}). Your previous current version was kept in history.`) : toast('Restore failed', 'error'); }}>
        <p className="font-semibold">The current version (v{cur.version}) will <b>not</b> be lost: it is saved in history, and the restored content is saved as a new version.</p>
      </Confirm>
    </div>
  );
}
