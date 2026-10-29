import { href } from '../lib/router.js';
import { COURSE } from '../data/syllabus.js';
import { Code2 } from 'lucide-react';
export default function Footer() {
  return (
    <footer className="px-3 sm:px-5 pb-6 mt-14">
      <div className="clay mx-auto max-w-7xl p-6 sm:p-8 grid gap-6 md:grid-cols-[1.4fr_1fr_1fr]">
        <div>
          <div className="flex items-center gap-2 font-extrabold text-xl"><span className="clay-primary clay-btn !p-0 w-10 h-10 !rounded-2xl"><Code2 size={20} /></span>MCA Python Lab</div>
          <p className="mt-3 font-bold">{COURSE.code}: {COURSE.name}</p><p className="text-soft font-semibold">Semester 1 · Five syllabus units</p>
        </div>
        <nav aria-label="Footer navigation"><p className="label">Explore</p><ul className="space-y-1 font-bold">
          {[['/', 'Home'], ['/programs', 'Programs'], ['/units', 'Units'], ['/syllabus', 'Syllabus'], ['/about', 'About']].map(([p, l]) => <li key={p}><a className="hover:text-primary" href={href(p)}>{l}</a></li>)}</ul></nav>
        <div><p className="label">Notes</p><p className="text-sm text-soft font-semibold">Programs are provided for educational purposes. Your edits, drafts and progress are stored only in this browser.</p></div>
        <p className="md:col-span-3 text-sm font-semibold text-soft border-t border-primary/10 pt-4">© {new Date().getFullYear()} MCA Python Lab. All rights reserved.</p>
      </div>
    </footer>
  );
}
