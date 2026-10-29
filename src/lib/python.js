// Lightweight Python syntax highlighter + helper utilities (text only - code is never executed).
const KW = new Set('False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield match case'.split(' '));
const BI = new Set('print input int float str bool list tuple dict set frozenset len range type isinstance enumerate zip map filter sum min max abs round sorted reversed open super object id hash dir help any all iter next chr ord bin hex oct pow divmod complex bytes bytearray format repr vars globals locals callable getattr setattr hasattr delattr property staticmethod classmethod Exception ValueError TypeError KeyError IndexError ZeroDivisionError FileNotFoundError'.split(' '));
export const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const RX = /(#[^\n]*)|((?:[rRbBfFuU]{0,2})(?:"""[\s\S]*?(?:"""|$)|'''[\s\S]*?(?:'''|$)|"(?:\\.|[^"\\\n])*"?|'(?:\\.|[^'\\\n])*'?))|(@[A-Za-z_][\w.]*)|(\b\d[\d_]*\.?\d*(?:[eE][+-]?\d+)?j?\b|\b0[xXbBoO][0-9a-fA-F_]+\b)|([A-Za-z_]\w*)/g;
const W = (c, t) => t.split('\n').map((x) => (x ? `<span class="${c}">${esc(x)}</span>` : '')).join('\n');
export function highlightLine(src) {
  let out = '', last = 0, m, prev = '';
  RX.lastIndex = 0;
  while ((m = RX.exec(src))) {
    out += esc(src.slice(last, m.index));
    const t = m[0];
    if (m[1]) out += W('tok-cm', t);
    else if (m[2]) out += W('tok-str', t);
    else if (m[3]) out += W('tok-dec', t);
    else if (m[4]) out += W('tok-num', t);
    else if (m[5]) {
      if (KW.has(t)) out += `<span class="tok-kw">${t}</span>`;
      else if (prev === 'def' || prev === 'class') out += `<span class="tok-fn">${t}</span>`;
      else if (BI.has(t)) out += `<span class="tok-bi">${t}</span>`;
      else out += t;
      prev = t;
    }
    if (!m[5] && t.trim()) prev = '';
    last = m.index + t.length;
  }
  return out + esc(src.slice(last));
}
// whole-text highlight (handles multi-line strings correctly)
export function highlight(src) { return highlightLine(src) + (src.endsWith('\n') ? ' ' : ''); }

// NOT a Python parser: only reports obviously unbalanced brackets / unterminated single-line strings.
export function quickStructureCheck(code) {
  const stack = [], pairs = { ')': '(', ']': '[', '}': '{' };
  const lines = code.split('\n');
  let inTriple = null;
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i]; let j = 0;
    while (j < ln.length) {
      const c = ln[j];
      if (inTriple) { if (ln.startsWith(inTriple, j)) { inTriple = null; j += 3; continue; } j++; continue; }
      if (c === '#') break;
      if (ln.startsWith('"""', j) || ln.startsWith("'''", j)) { inTriple = ln.substr(j, 3); j += 3; continue; }
      if (c === '"' || c === "'") {
        let k = j + 1; while (k < ln.length && ln[k] !== c) { if (ln[k] === '\\') k++; k++; }
        if (k >= ln.length) return { ok: false, msg: `Line ${i + 1}: string is not closed` };
        j = k + 1; continue;
      }
      if ('([{'.includes(c)) stack.push([c, i + 1]);
      else if (')]}'.includes(c)) { const t = stack.pop(); if (!t || t[0] !== pairs[c]) return { ok: false, msg: `Line ${i + 1}: unexpected '${c}'` }; }
      j++;
    }
  }
  if (inTriple) return { ok: false, msg: 'A triple-quoted string is not closed' };
  if (stack.length) return { ok: false, msg: `Line ${stack[stack.length - 1][1]}: '${stack[stack.length - 1][0]}' is never closed` };
  return { ok: true, msg: 'Brackets and quotes look balanced. (This is NOT a Python syntax check.)' };
}
export function tidyCode(code) {
  return code.replace(/\r\n?/g, '\n').replace(/\t/g, '    ').split('\n').map((l) => l.replace(/\s+$/, '')).join('\n').replace(/\n+$/, '') + '\n';
}
export const THIRD_PARTY = ['pandas', 'numpy', 'matplotlib', 'scipy', 'requests', 'openpyxl'];
export function detectDeps(code) {
  const found = new Set();
  for (const m of code.matchAll(/^\s*(?:import|from)\s+([A-Za-z_]\w*)/gm)) if (THIRD_PARTY.includes(m[1])) found.add(m[1]);
  return [...found];
}

export const highlightLines = (src) => highlightLine(src).split('\n');
