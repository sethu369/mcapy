import { PageTitle } from '../components/ui.jsx';
import { UnitCard } from '../components/Cards.jsx';
import { UNITS } from '../data/syllabus.js';
import { DownloadAllButton } from '../components/actions.jsx';
export default function Units() {
  return (<div><PageTitle title="Unit-wise Programs" sub="Five syllabus units of MCA 102 A: Programming in Python. Open a unit to see only its programs, or download the unit as a ZIP."><DownloadAllButton /></PageTitle>
    <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-6">{UNITS.map((u) => <UnitCard key={u.n} u={u} />)}</div></div>);
}
