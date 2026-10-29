import { UNITS } from '../data/syllabus.js';
import { DIFFICULTIES } from '../lib/store.js';
const Pill = ({ on, onClick, children }) => <button type="button" aria-pressed={on} onClick={onClick} className={`clay-btn btn-sm ${on ? 'clay-primary' : ''}`}>{children}</button>;
export function UnitFilter({ value, onChange, counts }) {
  return (<fieldset><legend className="label">Unit</legend><div className="flex flex-wrap gap-2">
    <Pill on={!value || value === 'all'} onClick={() => onChange('all')}>All Units{counts ? ` (${counts.all})` : ''}</Pill>
    {UNITS.map((u) => <Pill key={u.n} on={String(value) === String(u.n)} onClick={() => onChange(String(u.n))}>Unit {u.n}{counts ? ` (${counts[u.n] || 0})` : ''}</Pill>)}
  </div></fieldset>);
}
export function DifficultyFilter({ value, onChange }) {
  return (<fieldset><legend className="label">Difficulty</legend><div className="flex flex-wrap gap-2">
    <Pill on={!value || value === 'all'} onClick={() => onChange('all')}>All</Pill>
    {DIFFICULTIES.map((d) => <Pill key={d} on={value === d} onClick={() => onChange(d)}>{d}</Pill>)}
  </div></fieldset>);
}
export const SelectFilter = ({ label, value, onChange, options, id }) => (
  <div><label htmlFor={id} className="label">{label}</label>
    <select id={id} className="clay-field" value={value || 'all'} onChange={(e) => onChange(e.target.value)}>
      <option value="all">All</option>{options.map((o) => <option key={o} value={o}>{o}</option>)}</select></div>
);
