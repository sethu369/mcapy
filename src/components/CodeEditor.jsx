import { useEffect, useMemo, useRef, useState } from 'react';
import { Maximize2, Minimize2, Search, Eye, Download, MousePointerSquareDashed, Wand2, ShieldQuestion, X } from 'lucide-react';
import { highlight, quickStructureCheck, tidyCode, esc } from '../lib/python.js';
import { CopyButton } from './actions.jsx';
import { downloadPython } from '../lib/zip.js';
import { toast } from './ui.jsx';
import { CodeBody } from './CodeViewer.jsx';

/** Textarea-over-highlight code editor: line numbers, tab indentation, find/replace, expand. */
export default function CodeEditor({ value, onChange, filename = 'program.py', dirty, error, id = 'code-editor' }) {
  const ta = useRef(null), pre = useRef(null), gut = useRef(null);
  const [big, setBig] = useState(false), [find, setFind] = useState(false), [preview, setPreview] = useState(false);
  const [q, setQ] = useState(''), [r, setR] = useState(''), [chk, setChk] = useState(null);
  const html = useMemo(() => highlight(value), [value]);
  const count = value.split('\n').length;
  const sync = () => { if (pre.current && ta.current) { pre.current.scrollTop = ta.current.scrollTop; pre.current.scrollLeft = ta.current.scrollLeft; gut.current.scrollTop = ta.current.scrollTop; } };
  useEffect(sync, [value]);
  const set = (v, a, b) => { onChange(v); requestAnimationFrame(() => { if (ta.current && a != null) { ta.current.selectionStart = a; ta.current.selectionEnd = b ?? a; } }); };
  const onKey = (e) => {
    const t = e.target, s = t.selectionStart, en = t.selectionEnd, v = t.value;
    if (e.key === 'Tab') {
      e.preventDefault();
      const ls = v.lastIndexOf('\n', s - 1) + 1, block = v.slice(ls, en);
      if (s !== en && block.includes('\n') || e.shiftKey) {
        const lines = v.slice(ls, en).split('\n');
        const out = lines.map((l) => (e.shiftKey ? l.replace(/^( {1,4}|\t)/, '') : '    ' + l));
        const nv = v.slice(0, ls) + out.join('\n') + v.slice(en); set(nv, ls, ls + out.join('\n').length);
      } else set(v.slice(0, s) + '    ' + v.slice(en), s + 4);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      const ls = v.lastIndexOf('\n', s - 1) + 1, line = v.slice(ls, s), indent = line.match(/^\s*/)[0] + (/:\s*$/.test(line) ? '    ' : '');
      set(v.slice(0, s) + '\n' + indent + v.slice(en), s + 1 + indent.length);
    } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'f') { e.preventDefault(); setFind(true); }
  };
  const matches = q ? value.split(q).length - 1 : 0;
  const findNext = () => {
    if (!q || !ta.current) return; const t = ta.current; let i = value.indexOf(q, t.selectionEnd); if (i < 0) i = value.indexOf(q);
    if (i < 0) { toast('Text not found', 'info'); return; }
    t.focus(); t.setSelectionRange(i, i + q.length);
    const lineNo = value.slice(0, i).split('\n').length; t.scrollTop = Math.max(0, (lineNo - 4) * 20.8);
  };
  const replaceOne = () => { const t = ta.current; if (!q) return; if (value.slice(t.selectionStart, t.selectionEnd) === q) { set(value.slice(0, t.selectionStart) + r + value.slice(t.selectionEnd), t.selectionStart + r.length); } findNext(); };
  const replaceAll = () => { if (!q || !matches) return; onChange(value.split(q).join(r)); toast(`Replaced ${matches} occurrence(s)`); };
  const box = (
    <div className={big ? 'fixed inset-0 z-[95] bg-canvas p-3 sm:p-6 flex flex-col' : ''}>
      <div className="flex flex-wrap items-center gap-2 mb-3">
        <CopyButton code={value} small />
        <button type="button" className="clay-btn btn-sm" onClick={() => { ta.current?.focus(); ta.current?.select(); }}><MousePointerSquareDashed size={15} />Select all</button>
        <button type="button" className="clay-btn btn-sm" aria-pressed={find} onClick={() => setFind(!find)}><Search size={15} />Find / Replace</button>
        <button type="button" className="clay-btn btn-sm" onClick={() => { onChange(tidyCode(value)); toast('Whitespace tidied (tabs → 4 spaces, trailing spaces removed). Not a full code formatter.', 'info'); }}><Wand2 size={15} />Tidy whitespace</button>
        <button type="button" className="clay-btn btn-sm" aria-pressed={preview} onClick={() => setPreview(!preview)}><Eye size={15} />{preview ? 'Back to editor' : 'Preview code'}</button>
        <button type="button" className="clay-btn btn-sm" onClick={() => { downloadPython({ code: value, filename }); toast(`Downloaded ${filename}`); }}><Download size={15} />Download code</button>
        <button type="button" className="clay-btn btn-sm" onClick={() => setBig(!big)}>{big ? <Minimize2 size={15} /> : <Maximize2 size={15} />}{big ? 'Exit full screen' : 'Expand editor'}</button>
        {dirty && <span className="chip bg-amber-100 text-amber-800" role="status">● Unsaved Changes</span>}
      </div>
      {find && (
        <div className="clay-tint p-3 mb-3 flex flex-wrap gap-2 items-center">
          <input className="clay-field !w-44 !py-1.5" aria-label="Find text" placeholder="Find…" value={q} onChange={(e) => setQ(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && (e.preventDefault(), findNext())} />
          <input className="clay-field !w-44 !py-1.5" aria-label="Replace with" placeholder="Replace with…" value={r} onChange={(e) => setR(e.target.value)} />
          <button type="button" className="clay-btn btn-sm" onClick={findNext}>Find next</button>
          <button type="button" className="clay-btn btn-sm" onClick={replaceOne}>Replace</button>
          <button type="button" className="clay-btn btn-sm" onClick={replaceAll}>Replace all</button>
          <span className="text-sm font-bold text-soft">{q ? `${matches} match(es)` : ''}</span>
          <button type="button" className="clay-btn clay-icon !w-8 !h-8 ml-auto" aria-label="Close find" onClick={() => setFind(false)}><X size={14} /></button>
        </div>)}
      {preview ? <CodeBody code={value} tall={big} /> : (
        <div className={`codebox relative flex overflow-hidden ${big ? 'flex-1' : 'h-[26rem]'} ${error ? 'ring-2 ring-rose-400' : ''}`}>
          <div ref={gut} className="code-font select-none text-right text-[#a7a3d6] py-3 pl-2 pr-3 overflow-hidden shrink-0" aria-hidden="true" style={{ minWidth: '3.2rem' }}>
            {Array.from({ length: count }, (_, i) => <div key={i}>{i + 1}</div>)}<div style={{ height: 40 }} />
          </div>
          <div className="relative flex-1 overflow-hidden">
            <pre ref={pre} className="code-font absolute inset-0 m-0 py-3 pr-4 overflow-hidden whitespace-pre pointer-events-none" aria-hidden="true" dangerouslySetInnerHTML={{ __html: html + '\n\n' }} />
            <textarea id={id} ref={ta} value={value} spellCheck={false} autoCapitalize="off" autoCorrect="off" wrap="off" aria-label="Python source code editor"
              onChange={(e) => onChange(e.target.value)} onScroll={sync} onKeyDown={onKey}
              className="code-font absolute inset-0 w-full h-full py-3 pr-4 bg-transparent text-transparent caret-[#4a3fc0] resize-none outline-none whitespace-pre overflow-auto" style={{ WebkitTextFillColor: 'transparent' }} />
          </div>
        </div>)}
      <div className="flex flex-wrap items-center gap-3 mt-3 text-sm font-bold text-soft">
        <span>{count} lines · {value.length} characters</span>
        <span className="chip bg-amber-50 text-amber-800 !normal-case"><ShieldQuestion size={13} />Syntax not validated — no Python backend is available; code is stored as text and never executed.</span>
        <button type="button" className="clay-btn btn-sm" onClick={() => setChk(quickStructureCheck(value))}>Quick bracket/quote check</button>
        {chk && <span className={chk.ok ? 'text-mint-dark' : 'text-rose-700'} role="status">{chk.msg}</span>}
      </div>
    </div>
  );
  return box;
}
