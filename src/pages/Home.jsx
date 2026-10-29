import { Rocket, Layers, Sparkles, Clock, Flame, BookOpen, FolderArchive, Search, Download, MousePointerClick, ArrowRight, Terminal } from 'lucide-react';
import { useStore, published } from '../lib/store.js';
import { href } from '../lib/router.js';
import { UNITS } from '../data/syllabus.js';
import { CONCEPTS } from '../data/concepts.js';
import { UnitCard, ProgramCard } from '../components/Cards.jsx';
import { DownloadAllButton, zipAll } from '../components/actions.jsx';
import { SearchBar } from '../components/Navbar.jsx';
import { highlightLine } from '../lib/python.js';

const POPULAR = [/hello world/i, /factorial/i, /fibonacci/i, /prime number/i, /palindrome/i, /student management|student record/i, /stack/i, /linked list/i, /inheritance/i, /sqlite|database/i];
const HERO = `# Welcome to MCA Python Lab
def greet(student):
    return f"Hello, {student}!"

for unit in range(1, 6):
    print(greet("MCA"), "Unit", unit)`;
const Section = ({ icon: Icon, title, children, action }) => (
  <section className="mt-14"><div className="flex items-end justify-between gap-3 mb-5"><h2 className="text-2xl sm:text-3xl font-extrabold flex items-center gap-3"><span className="clay-sm w-11 h-11 grid place-items-center !rounded-2xl text-primary"><Icon size={22} /></span>{title}</h2>{action}</div>{children}</section>
);
export default function Home() {
  const s = useStore(); const progs = published(s);
  const popular = []; POPULAR.forEach((rx) => { const m = progs.find((p) => rx.test(p.title) && !popular.includes(p)); if (m) popular.push(m); });
  const recentAdded = [...progs].sort((a, b) => b.createdAt.localeCompare(a.createdAt) || b.unit - a.unit || b.number - a.number).slice(0, 6);
  const viewed = s.prefs.recent.map((id) => progs.find((p) => p.id === id)).filter(Boolean).slice(0, 6);
  const stats = [['Total Programs', progs.length, 'text-primary'], ['Total Units', new Set(progs.map((p) => p.unit)).size, 'text-sky-600'], ['Python Concepts', CONCEPTS.length, 'text-mint-dark'], ['Available for Download', progs.length, 'text-rose-500']];
  const steps = [[Search, 'Search or browse', 'Find a program by topic, unit, difficulty or any word in the code.'], [BookOpen, 'Read & understand', 'Study the algorithm, explanation and real sample output.'], [Download, 'Copy or download', 'Copy the code or download the .py file — or the whole unit as a ZIP.'], [MousePointerClick, 'Track & customise', 'Mark progress, favourite programs, and edit or add your own.']];
  return (
    <div>
      <section className="grid lg:grid-cols-[1.1fr_1fr] gap-8 items-center pt-6">
        <div>
          <span className="chip clay-sm !bg-white !text-primary !text-sm !py-1.5 !px-4 mb-5"><Sparkles size={14} />MCA Semester 1 · MCA 102 A</span>
          <h1 className="text-5xl sm:text-6xl font-extrabold tracking-tight leading-[1.05]">Master <span className="text-primary">Python</span> Programming</h1>
          <p className="text-xl font-semibold text-soft mt-5 max-w-xl">Your complete MCA Semester 1 Python practical program library.</p>
          <div className="flex flex-wrap gap-3 mt-8">
            <a className="clay-btn clay-primary !py-3 !px-6" href={href('/programs')}><Rocket size={18} />Explore Programs</a>
            <a className="clay-btn !py-3 !px-6" href={href('/units')}><Layers size={18} />Browse Units</a>
            <DownloadAllButton primary={false} className="clay-mint !py-3 !px-6" />
          </div>
          <div className="mt-8 max-w-lg"><SearchBar id="hero-search" /></div>
        </div>
        <div className="relative" aria-hidden="true">
          <div className="clay p-5 rotate-[-2deg]"><div className="flex gap-2 mb-3"><i className="w-3 h-3 rounded-full bg-rose-400" /><i className="w-3 h-3 rounded-full bg-amber-300" /><i className="w-3 h-3 rounded-full bg-emerald-400" /><span className="ml-2 text-xs font-extrabold text-soft">hello_mca.py</span></div>
            <pre className="code-font codebox p-4 overflow-hidden" dangerouslySetInnerHTML={{ __html: highlightLine(HERO) }} />
            <div className="clay-inset !rounded-2xl mt-3 p-3 code-font text-[12px] flex items-center gap-2"><Terminal size={14} className="text-mint-dark" />Hello, MCA! Unit 1 … Unit 5</div></div>
          <div className="clay-sm absolute -top-4 -right-2 px-4 py-2 font-extrabold text-primary rotate-6">print()</div>
          <div className="clay-sm absolute -bottom-5 left-4 px-4 py-2 font-extrabold text-mint-dark rotate-[-5deg]">for i in range(5):</div>
          <div className="clay-sm absolute top-1/2 -right-1 sm:-right-5 px-4 py-2 font-extrabold text-rose-500 rotate-3">class</div>
        </div>
      </section>
      <section aria-label="Library statistics" className="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-14">
        {stats.map(([l, v, c]) => <div key={l} className="clay p-5 text-center"><p className={`text-4xl sm:text-5xl font-extrabold ${c}`}>{v}</p><p className="font-extrabold text-soft mt-1 text-sm">{l}</p></div>)}
      </section>
      <Section icon={Layers} title="The Five Units" action={<a className="clay-btn btn-sm" href={href('/units')}>All units<ArrowRight size={14} /></a>}>
        <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-6">{UNITS.map((u) => <UnitCard key={u.n} u={u} />)}
          <div className="clay p-6 flex flex-col justify-between gap-4 bg-gradient-to-br from-white to-primary-light"><div><FolderArchive className="text-primary mb-3" size={32} /><h3 className="font-extrabold text-xl">Download everything</h3><p className="font-semibold text-soft mt-2">One ZIP with all {progs.length} programs in unit folders, plus README, syllabus, manifest and requirements.txt.</p></div><button className="clay-btn clay-primary" onClick={zipAll}><FolderArchive size={17} />MCA_Python_Programs.zip</button></div></div>
      </Section>
      {viewed.length > 0 && <Section icon={Clock} title="Recently Viewed"><div className="grid sm:grid-cols-2 xl:grid-cols-3 gap-5">{viewed.map((p) => <ProgramCard key={p.id} p={p} />)}</div></Section>}
      <Section icon={Flame} title="Popular Python Programs"><div className="grid sm:grid-cols-2 xl:grid-cols-3 gap-5">{popular.slice(0, 6).map((p) => <ProgramCard key={p.id} p={p} />)}</div></Section>
      <Section icon={Sparkles} title="Recently Added"><div className="grid sm:grid-cols-2 xl:grid-cols-3 gap-5">{recentAdded.map((p) => <ProgramCard key={p.id} p={p} />)}</div></Section>
      <Section icon={BookOpen} title="Python Learning Topics" action={<a className="clay-btn btn-sm" href={href('/concepts')}>All concepts<ArrowRight size={14} /></a>}>
        <div className="flex flex-wrap gap-3">{CONCEPTS.map((c) => <a key={c.slug} href={href('/concepts', { open: c.slug })} className={`clay-btn unit-${c.unit}`}><span className="w-2.5 h-2.5 rounded-full" style={{ background: 'var(--u)' }} />{c.name}</a>)}</div>
      </Section>
      <Section icon={MousePointerClick} title="How to Use This Website">
        <ol className="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">{steps.map(([I, t, d], i) => <li key={t} className="clay p-5"><span className="clay-sm w-10 h-10 grid place-items-center !rounded-2xl font-extrabold text-primary mb-3">{i + 1}</span><I className="text-primary mb-2" size={22} /><h3 className="font-extrabold">{t}</h3><p className="text-sm font-semibold text-soft mt-1">{d}</p></li>)}</ol>
      </Section>
    </div>
  );
}
