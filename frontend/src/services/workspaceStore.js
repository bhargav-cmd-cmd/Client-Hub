export const WORKSPACE_KEY = 'clienthub-workspace-v2';
export const emptyWorkspace = () => ({ clients: [], projects: [], documents: [], activity: [] });

const sampleIds = {
  clients: new Set(['c1', 'c2', 'c3', 'c4', 'c5']),
  projects: new Set(['p1', 'p2', 'p3', 'p4', 'p5']),
  documents: new Set(['d1', 'd2', 'd3']),
  activity: new Set(['a1', 'a2', 'a3']),
};
const validWorkspace = data => data && Object.keys(sampleIds).every(key => Array.isArray(data[key]));
const withoutSamples = data => Object.fromEntries(Object.keys(sampleIds).map(key => [key,
  data[key].filter(record => !sampleIds[key].has(record.id)),
]));

export function readWorkspace() {
  try {
    const current = JSON.parse(localStorage.getItem(WORKSPACE_KEY));
    if (validWorkspace(current)) return withoutSamples(current);
    const previous = JSON.parse(localStorage.getItem('clienthub-demo-v1'));
    if (validWorkspace(previous)) {
      // Remove only the original demo records; retain anything the user added.
      // Keep the old storage key as a backup of the previous workspace.
      return withoutSamples(previous);
    }
  } catch { /* A fresh workspace is also usable when storage is unavailable. */ }
  return emptyWorkspace();
}
