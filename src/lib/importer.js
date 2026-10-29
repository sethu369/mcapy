import JSZip from 'jszip';
// Safe parsing of .py / .zip uploads. Files are only READ AS TEXT - never executed.
export const LIMITS = { fileBytes: 500 * 1024, entries: 400, zipBytes: 20 * 1024 * 1024 };
export const safePath = (p) => {
  const n = p.replace(/\\/g, '/');
  if (!n || n.includes('\0') || n.startsWith('/') || /^[A-Za-z]:/.test(n) || n.split('/').some((seg) => seg === '..')) return null;
  return n;
};
const clean = (n) => n.replace(/^program_\d+_/, '');
export const titleFrom = (code, name) => {
  const doc = code.match(/^\s*(?:#[^\n]*\n)*\s*(?:"""|''')\s*([^\n"']+)/); if (doc && doc[1].trim().length > 3) return doc[1].trim().replace(/\.$/, '');
  for (const l of code.split('\n').slice(0, 6)) { const m = l.match(/^#\s*(?:Program|Title)?\s*:?\s*(.+)$/i); if (m && !/^(!|-\*-|requires|coding|terminal|cmd)/i.test(m[1]) && m[1].length > 3 && m[1].length < 90) return m[1].trim().replace(/\.$/, ''); }
  return clean(name.replace(/\.py$/i, '')).replace(/[_-]+/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()).trim() || 'Imported Program';
};
export const safeFilename = (n) => {
  let b = clean(n.split('/').pop()).replace(/[^A-Za-z0-9_.-]+/g, '_').replace(/^[._-]+/, '');
  if (!/\.py$/i.test(b)) b += '.py'; b = b.replace(/\.py$/i, '').slice(0, 70) + '.py'; return b.toLowerCase();
};
const decode = (buf) => { try { return new TextDecoder('utf-8', { fatal: true }).decode(buf).replace(/^﻿/, '').replace(/\r\n?/g, '\n'); } catch { return null; } };
const unitFromPath = (p) => { const m = p.match(/(?:^|\/)Unit_([1-5])_/i); return m ? Number(m[1]) : null; };
export async function readFiles(fileList, defaultUnit) {
  const items = [], ignored = [];
  const add = (path, size, code, extra = {}) => {
    const filename = safeFilename(path);
    items.push({ key: `${path}-${items.length}`, originalName: path.split('/').pop(), path, filename, title: titleFrom(code, path.split('/').pop()), size, code, unit: unitFromPath(path) || defaultUnit, ...extra });
  };
  for (const f of fileList) {
    const lower = f.name.toLowerCase();
    if (lower.endsWith('.py')) {
      if (f.size > LIMITS.fileBytes) { ignored.push(`${f.name}: larger than ${LIMITS.fileBytes / 1024} KB`); continue; }
      const code = decode(await f.arrayBuffer()); if (code == null) { ignored.push(`${f.name}: not UTF-8 text`); continue; }
      add(f.name, f.size, code);
    } else if (lower.endsWith('.zip')) {
      if (f.size > LIMITS.zipBytes) { ignored.push(`${f.name}: ZIP too large`); continue; }
      let zip; try { zip = await JSZip.loadAsync(await f.arrayBuffer()); } catch { ignored.push(`${f.name}: not a valid ZIP archive`); continue; }
      const entries = Object.values(zip.files).filter((z) => !z.dir);
      if (entries.length > LIMITS.entries) { ignored.push(`${f.name}: more than ${LIMITS.entries} files`); continue; }
      let manifest = {};
      const mf = entries.find((z) => /(^|\/)manifest\.json$/i.test(z.name));
      if (mf) { try { const j = JSON.parse(await mf.async('string')); (j.programs || []).forEach((p) => { manifest[String(p.file || '').split('/').slice(1).join('/')] = p; manifest[String(p.file || '').split('/').pop()] = p; }); } catch { /* ignore bad manifest */ } }
      for (const z of entries) {
        const sp = safePath(z.unsafeOriginalName || z.name);
        if (!sp) { ignored.push(`${z.unsafeOriginalName || z.name}: unsafe path rejected`); continue; }
        if (/(^|\/)(__MACOSX|\.git)\//.test(sp) || /(^|\/)\._/.test(sp)) continue;
        if (!/\.py$/i.test(sp)) { if (!/(manifest\.json|readme|requirements|syllabus|sample_outputs)/i.test(sp)) ignored.push(`${sp}: not a Python file`); continue; }
        const buf = await z.async('uint8array'); if (buf.length > LIMITS.fileBytes) { ignored.push(`${sp}: larger than ${LIMITS.fileBytes / 1024} KB`); continue; }
        const code = decode(buf); if (code == null) { ignored.push(`${sp}: not UTF-8 text`); continue; }
        const mp = manifest[sp.split('/').slice(-2).join('/')] || manifest[sp.split('/').pop()];
        add(sp, buf.length, code, mp ? { id: mp.id, title: mp.title || undefined, unit: mp.unit || unitFromPath(sp) || defaultUnit, category: mp.category, difficulty: mp.difficulty, fromManifest: true } : {});
      }
    } else ignored.push(`${f.name}: only .py and .zip files can be imported`);
  }
  items.forEach((i) => { if (!i.title) i.title = titleFrom(i.code, i.originalName); });
  return { items, ignored };
}
