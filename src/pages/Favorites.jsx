import { Heart } from 'lucide-react';
import { useStore, published } from '../lib/store.js';
import { PageTitle, Empty } from '../components/ui.jsx';
import { ProgramCard } from '../components/Cards.jsx';
import { href } from '../lib/router.js';
export default function Favorites() {
  const s = useStore(); const list = published(s).filter((p) => s.prefs.favorites.includes(p.id));
  return (<div><PageTitle title="Favorites" sub={`${list.length} saved program(s), stored in this browser.`} />
    {list.length === 0 ? <Empty icon={Heart} title="No favorites yet">Tap the heart on any program to save it here. <a className="text-primary underline" href={href('/programs')}>Browse programs</a></Empty> : <div className="grid sm:grid-cols-2 xl:grid-cols-3 gap-5">{list.map((p) => <ProgramCard key={p.id} p={p} />)}</div>}</div>);
}
