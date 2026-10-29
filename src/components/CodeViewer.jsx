import { useMemo, useState } from 'react';
import { Maximize2, Minimize2, Type, Download } from 'lucide-react';
import { highlightLines, esc } from '../lib/python.js';
import { CopyButton } from './actions.jsx';
import { downloadPython } from '../lib/zip.js';
import { Modal, toast } from './ui.jsx';

function Body({ code, plain, tall }) {
  const lines = useMemo(() => (plain ? code.split('\n').map(esc) : highlightLines(code)), [code, plain]);
  const n = code.endsWith('\n') ? lines.length - 1 : lines.length;
  return (
    <div className={`codebox overflow-auto ${tall ? 'max-h-[75vh]' : 'max-h-[28rem]'}`} tabIndex={0} role="region" aria-label="Python source code">
      <pre className="code-font m-0 py-3 min-w-max"><code>
        {lines.slice(0, n).map((h, i) => (
          <div key={i} className="flex"><span className="select-none text-right w-12 shrink-0 pr-3 text-[#a7a3d6]" aria-hidden="true">{i + 1}</span><span className="pr-6 whitespace-pre" dangerouslySetInnerHTML={{ __html: h || ' ' }} /></div>))}
      </code></pre>
    </div>
  );
}
export default function CodeViewer({ code, filename = 'program.py', title = 'Python Source Code', extra }) {
  const [plain, setPlain] = useState(false), [big, setBig] = useState(false);
  const prog = { code, filename };
  const bar = (
    <div className="flex flex-wrap items-center gap-2">
      <CopyButton code={code} small />
      <button className="clay-btn btn-sm" onClick={() => { downloadPython(prog); toast(`Downloaded ${filename}`); }} aria-label={`Download ${filename}`}><Download size={15} />Download .py</button>
      <button className="clay-btn btn-sm" aria-pressed={plain} onClick={() => setPlain(!plain)}><Type size={15} />{plain ? 'Highlight' : 'Clear formatting'}</button>
      <button className="clay-btn btn-sm" onClick={() => setBig(!big)}>{big ? <Minimize2 size={15} /> : <Maximize2 size={15} />}{big ? 'Close' : 'Expand code'}</button>
      {extra}
    </div>);
  return (
    <section aria-label={title}>
      <div className="flex flex-wrap items-center justify-between gap-3 mb-3"><h3 className="font-extrabold text-lg">{title} <code className="text-sm text-soft font-bold">{filename}</code></h3>{bar}</div>
      <Body code={code} plain={plain} />
      <Modal open={big} onClose={() => setBig(false)} wide title={filename}><div className="mb-3">{bar}</div><Body code={code} plain={plain} tall /></Modal>
    </section>
  );
}
export { Body as CodeBody };
