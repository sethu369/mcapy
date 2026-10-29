import { useEffect, useState } from 'react';
import { useRoute, onLeaveConfirm, href } from './lib/router.js';
import { initStore, useStore } from './lib/store.js';
import Navbar from './components/Navbar.jsx';
import Footer from './components/Footer.jsx';
import { ToastHost, Confirm, Empty } from './components/ui.jsx';
import { ZipHost } from './components/actions.jsx';
import Home from './pages/Home.jsx';
import Programs from './pages/Programs.jsx';
import Units from './pages/Units.jsx';
import ProgramDetails from './pages/ProgramDetails.jsx';
import Concepts from './pages/Concepts.jsx';
import Practice from './pages/Practice.jsx';
import Syllabus from './pages/Syllabus.jsx';
import About from './pages/About.jsx';
import Favorites from './pages/Favorites.jsx';
import Manage, { Drafts, Trash } from './pages/Manage.jsx';
import ProgramForm from './pages/ProgramForm.jsx';
import Versions from './pages/Versions.jsx';
import { Compass } from 'lucide-react';

export default function App() {
  const route = useRoute(); const { ready } = useStore(); const [leave, setLeave] = useState(null);
  useEffect(() => { initStore(); onLeaveConfirm((proceed) => setLeave(() => proceed)); }, []);
  const [a, b] = route.parts; let page;
  switch (a) {
    case undefined: page = <Home />; break;
    case 'programs': page = <Programs route={route} />; break;
    case 'units': page = <Units />; break;
    case 'unit': { const n = Number(b); page = n >= 1 && n <= 5 ? <Programs key={n} route={route} fixedUnit={n} /> : <Units />; break; }
    case 'program': page = <ProgramDetails id={b} />; break;
    case 'versions': page = <Versions id={b} />; break;
    case 'concepts': page = <Concepts route={route} />; break;
    case 'practice': page = <Practice route={route} />; break;
    case 'syllabus': page = <Syllabus />; break;
    case 'about': page = <About />; break;
    case 'favorites': page = <Favorites />; break;
    case 'manage': page = <Manage />; break;
    case 'drafts': page = <Drafts path="/drafts" />; break;
    case 'trash': page = <Trash path="/trash" />; break;
    case 'new': page = <ProgramForm key="new" route={route} />; break;
    case 'edit': page = <ProgramForm key={b} id={b} route={route} />; break;
    default: page = <Empty icon={Compass} title="Page not found"><a className="text-primary underline" href={href('/')}>Go home</a></Empty>;
  }
  return (
    <>
      <a href="#main" onClick={(e) => { e.preventDefault(); document.getElementById('main')?.focus(); }} className="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:z-[200] clay-btn">Skip to content</a>
      <Navbar path={route.path} />
      <main id="main" tabIndex={-1} className="mx-auto max-w-7xl px-3 sm:px-5 pt-8 outline-none">{ready ? page : <p className="font-bold text-soft p-10 text-center">Loading your program library…</p>}</main>
      <Footer />
      <ToastHost /><ZipHost />
      <Confirm open={!!leave} title="Leave without saving?" confirmLabel="Discard changes & leave" danger cancelLabel="Keep editing" onCancel={() => setLeave(null)} onConfirm={() => { const f = leave; setLeave(null); f(); }}>
        <p className="font-semibold">You have unsaved changes. If you leave this page they will be lost.</p></Confirm>
    </>
  );
}
