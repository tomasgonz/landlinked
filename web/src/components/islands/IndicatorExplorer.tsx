import { useState, useEffect, useRef } from 'react';
import { Chart, registerables } from 'chart.js';
import { indicators, categorizedIndicators } from '../../lib/indicators-data';

Chart.register(...registerables);

const AVAILABLE_GROUPS = [
  'lldcs', 'ldcs', 'sids', 'g77', 'oecd', 'eu',
  'g20', 'aosis', 'lmcs', 'lics', 'brics',
];

const GROUP_LABELS: Record<string, string> = {
  lldcs: 'LLDCs', ldcs: 'LDCs', sids: 'SIDS', oecd: 'OECD',
  eu: 'EU', g20: 'G20', g77: 'G77', brics: 'BRICS',
  aosis: 'AOSIS', lmcs: 'LMCs', lics: 'LICs',
};

const CATEGORIES = categorizedIndicators;

const INDICATOR_NAMES: Record<string, string> = Object.fromEntries(
  Object.entries(indicators).map(([code, meta]) => [code, meta.description])
);

const COLORS = ['#003366', '#0097A7', '#6B7280', '#D97706', '#9333EA', '#DC2626', '#16A34A', '#7C3AED'];

interface Props {
  groupCountries?: Record<string, { name: string; iso3: string }[]>;
}

export default function IndicatorExplorer({ groupCountries = {} }: Props) {
  const [selectedGroups, setSelectedGroups] = useState<string[]>(['lldcs']);
  const [selectedCategory, setSelectedCategory] = useState('General');
  const [selectedIndicator, setSelectedIndicator] = useState('SP.POP.TOTL');
  const [selectedCountry, setSelectedCountry] = useState('');
  const [chartData, setChartData] = useState<Record<string, { dates: string[]; values: number[] }>>({});
  const [countryData, setCountryData] = useState<{ group: string; dates: string[]; countries: { name: string; id: string; values: (number | null)[] }[] } | null>(null);
  const [loading, setLoading] = useState(false);
  const [showMethodology, setShowMethodology] = useState(false);
  const [showTable, setShowTable] = useState(false);
  const chartRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<Chart | null>(null);

  const availableIndicators = CATEGORIES[selectedCategory] || [];

  // Derive country list from selected groups (deduplicated, sorted)
  const countries = (() => {
    const seen = new Set<string>();
    const result: { name: string; iso3: string }[] = [];
    for (const gid of selectedGroups) {
      for (const c of groupCountries[gid] || []) {
        if (!seen.has(c.iso3)) {
          seen.add(c.iso3);
          result.push(c);
        }
      }
    }
    return result.sort((a, b) => a.name.localeCompare(b.name));
  })();

  // Clear country selection when it's no longer in the filtered list
  useEffect(() => {
    if (selectedCountry && !countries.some(c => c.iso3 === selectedCountry)) {
      setSelectedCountry('');
    }
  }, [selectedGroups]);

  // Track the country name returned by the API so we can identify it in chartData
  const countryName = countries.find(c => c.iso3 === selectedCountry)?.name ?? '';

  useEffect(() => {
    if (!selectedIndicator || selectedGroups.length === 0) return;
    setLoading(true);
    let url = `/data/indicator-data?code=${selectedIndicator}&groups=${selectedGroups.join(',')}&detail=1`;
    if (selectedCountry) url += `&country=${selectedCountry}`;
    fetch(url)
      .then(r => r.json())
      .then(data => {
        const { _countryData, ...rest } = data;
        setChartData(rest);
        setCountryData(_countryData ?? null);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [selectedIndicator, selectedGroups, selectedCountry]);

  useEffect(() => {
    if (!chartRef.current || Object.keys(chartData).length === 0) return;

    if (chartInstance.current) chartInstance.current.destroy();

    const allDates = new Set<string>();
    for (const s of Object.values(chartData)) {
      for (const d of s.dates) allDates.add(d);
    }
    const labels = [...allDates].sort();

    const datasets = Object.entries(chartData).map(([group, series], i) => {
      const dataMap = new Map(series.dates.map((d, j) => [d, series.values[j]]));
      const isCountry = countryName !== '' && group === countryName;
      return {
        label: GROUP_LABELS[group] || group,
        data: labels.map(l => dataMap.get(l) ?? null),
        borderColor: COLORS[i % COLORS.length],
        backgroundColor: COLORS[i % COLORS.length] + '20',
        tension: 0.3,
        pointRadius: isCountry ? 2 : 1,
        borderWidth: 2,
        borderDash: isCountry ? [6, 3] : [],
      };
    });

    chartInstance.current = new Chart(chartRef.current, {
      type: 'line',
      data: { labels, datasets },
      options: {
        responsive: true,
        interaction: { mode: 'index', intersect: false },
        plugins: { legend: { position: 'bottom' } },
        scales: {
          x: { title: { display: true, text: 'Year' } },
          y: { title: { display: true, text: INDICATOR_NAMES[selectedIndicator] || selectedIndicator } },
        },
      },
    });

    return () => { chartInstance.current?.destroy(); };
  }, [chartData]);

  function toggleGroup(g: string) {
    setSelectedGroups(prev =>
      prev.includes(g) ? prev.filter(x => x !== g) : [...prev, g]
    );
  }

  return (
    <div className="indicator-explorer">
      <div className="filter-row">
        <div>
          <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.25rem', color: '#4A5568' }}>
            Groups
          </label>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.3rem' }}>
            {AVAILABLE_GROUPS.map(g => (
              <button
                key={g}
                onClick={() => toggleGroup(g)}
                style={{
                  padding: '0.3rem 0.6rem',
                  border: '1px solid',
                  borderColor: selectedGroups.includes(g) ? '#003366' : '#CBD5E0',
                  borderRadius: '4px',
                  background: selectedGroups.includes(g) ? '#003366' : '#fff',
                  color: selectedGroups.includes(g) ? '#fff' : '#4A5568',
                  cursor: 'pointer',
                  fontSize: '0.8rem',
                  fontWeight: 500,
                }}
              >
                {GROUP_LABELS[g] || g.toUpperCase()}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="filter-row">
        <div>
          <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.25rem', color: '#4A5568' }}>
            Category
          </label>
          <select value={selectedCategory} onChange={e => {
            setSelectedCategory(e.target.value);
            const codes = CATEGORIES[e.target.value] || [];
            if (codes.length > 0) setSelectedIndicator(codes[0]);
          }}>
            {Object.keys(CATEGORIES).map(c => <option key={c} value={c}>{c}</option>)}
          </select>
        </div>
        <div>
          <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.25rem', color: '#4A5568' }}>
            Indicator
          </label>
          <select value={selectedIndicator} onChange={e => setSelectedIndicator(e.target.value)}>
            {availableIndicators.map(code => (
              <option key={code} value={code}>{INDICATOR_NAMES[code] || code}</option>
            ))}
          </select>
        </div>
        {countries.length > 0 && (
          <div>
            <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.25rem', color: '#4A5568' }}>
              Compare Country
            </label>
            <select value={selectedCountry} onChange={e => setSelectedCountry(e.target.value)}>
              <option value="">— No country —</option>
              {countries.map(c => (
                <option key={c.iso3} value={c.iso3}>{c.name}</option>
              ))}
            </select>
          </div>
        )}
      </div>

      {loading && <p style={{ color: '#718096' }}>Loading...</p>}

      {Object.keys(chartData).length > 0 && (
        <div style={{ marginTop: '1rem' }}>
          <div className="comparison-card-header">
            <h3>{INDICATOR_NAMES[selectedIndicator] || selectedIndicator}</h3>
            <div className="card-subtitle">{selectedIndicator}{indicators[selectedIndicator]?.unit && ` (${indicators[selectedIndicator].unit})`} | Groups: {selectedGroups.map(g => GROUP_LABELS[g] || g.toUpperCase()).join(', ')}{countryName && ` | Country: ${countryName}`}</div>
          </div>

          {/* Methodology toggle */}
          <button
            onClick={() => setShowMethodology(v => !v)}
            style={{
              background: 'none', border: 'none', cursor: 'pointer',
              color: '#003366', fontSize: '0.82rem', fontWeight: 500,
              padding: '0.4rem 0', display: 'flex', alignItems: 'center', gap: '0.3rem',
            }}
          >
            {showMethodology ? '▾' : '▸'} Methodology
          </button>
          {showMethodology && (() => {
            const meta = indicators[selectedIndicator];
            if (!meta) return null;
            const codeStyle: React.CSSProperties = { background: '#EDF2F7', padding: '0.15rem 0.45rem', borderRadius: '3px', fontFamily: 'monospace', fontSize: '0.82rem' };
            const sectionStyle: React.CSSProperties = { marginTop: '0.6rem', paddingTop: '0.5rem', borderTop: '1px solid #E2E8F0' };
            const varStyle: React.CSSProperties = { fontStyle: 'italic', color: '#003366' };
            const weightMeta = meta.agg === 'weighted' && meta.weight_by ? indicators[meta.weight_by] : null;
            return (
              <div style={{
                background: '#F7F8FA', border: '1px solid #E2E8F0', borderRadius: '8px',
                padding: '1rem 1.25rem', marginBottom: '0.75rem', fontSize: '0.85rem', lineHeight: 1.8,
              }}>
                {/* Data source */}
                <div><strong>Data source:</strong> {meta.source}{meta.source_db && ` — ${meta.source_db}`}.{' '}
                  {meta.source === 'World Bank' && 'Values are collected from national statistical offices, central banks, and international organisations, then harmonised for cross-country comparability.'}
                  {meta.source === 'UN SDG' && 'Values are compiled from national and international sources to track progress toward the Sustainable Development Goals.'}
                  {meta.source === 'FAOSTAT' && 'Values are collected from national statistical offices and international organisations, covering food, agriculture, and natural resource domains.'}
                  {meta.source === 'IMF' && 'Values are from IMF staff estimates and projections, providing forward-looking macroeconomic and fiscal data.'}
                  {meta.source_url && <>{' '}<a href={meta.source_url} target="_blank" rel="noopener noreferrer" style={{ color: '#003366', fontSize: '0.82rem' }}>(view source)</a></>}
                </div>

                {/* Methodology note */}
                {meta.methodology && (
                  <div><strong>Methodology:</strong> {meta.methodology}</div>
                )}

                {/* Indicator code + unit */}
                <div><strong>Indicator code:</strong> <code style={codeStyle}>{selectedIndicator}</code>{meta.unit && <> · <strong>Unit:</strong> {meta.unit}</>}</div>

                {/* Aggregation method */}
                <div style={sectionStyle}>
                  <strong>Aggregation method: </strong>
                  {meta.agg === 'sum' && <>
                    <strong style={{ color: '#003366' }}>Sum (additive)</strong>
                    <div style={{ margin: '0.3rem 0 0.2rem' }}>
                      The group-level value is the arithmetic sum of all member-country values for each year. This method is appropriate for extensive (absolute) quantities where the group total has a meaningful interpretation.
                    </div>
                  </>}
                  {meta.agg === 'mean' && <>
                    <strong style={{ color: '#003366' }}>Simple average (unweighted mean)</strong>
                    <div style={{ margin: '0.3rem 0 0.2rem' }}>
                      The group-level value is the arithmetic mean across all member countries with available data for each year. Every country contributes equally regardless of size. This method is used when no natural weighting variable exists or when each country's observation is considered equally representative.
                    </div>
                  </>}
                  {meta.agg === 'weighted' && <>
                    <strong style={{ color: '#003366' }}>Weighted average</strong>
                    <div style={{ margin: '0.3rem 0 0.2rem' }}>
                      The group-level value is a weighted mean, where each country's contribution is proportional to its weight. This prevents small countries from having equal influence to large ones and produces an aggregate that better reflects the group's overall level. Only country-year pairs where both the indicator value and the weight are available are included.
                    </div>
                  </>}
                </div>

                {/* Formula */}
                <div style={sectionStyle}>
                  <strong>Formula:</strong>
                  {meta.agg === 'sum' && (
                    <div style={{ margin: '0.4rem 0', padding: '0.5rem 0.75rem', background: '#EDF2F7', borderRadius: '6px', fontFamily: 'monospace', fontSize: '0.88rem' }}>
                      <div>V<sub>group</sub>(t) = <span style={varStyle}>v</span><sub>1</sub>(t) + <span style={varStyle}>v</span><sub>2</sub>(t) + ... + <span style={varStyle}>v</span><sub>n</sub>(t) = Σ<sub>i=1..n</sub> <span style={varStyle}>v</span><sub>i</sub>(t)</div>
                    </div>
                  )}
                  {meta.agg === 'mean' && (
                    <div style={{ margin: '0.4rem 0', padding: '0.5rem 0.75rem', background: '#EDF2F7', borderRadius: '6px', fontFamily: 'monospace', fontSize: '0.88rem' }}>
                      <div>V<sub>group</sub>(t) = Σ<sub>i=1..n</sub> <span style={varStyle}>v</span><sub>i</sub>(t) / <span style={varStyle}>n</span>(t)</div>
                    </div>
                  )}
                  {meta.agg === 'weighted' && (
                    <div style={{ margin: '0.4rem 0', padding: '0.5rem 0.75rem', background: '#EDF2F7', borderRadius: '6px', fontFamily: 'monospace', fontSize: '0.88rem' }}>
                      <div>V<sub>group</sub>(t) = Σ<sub>i=1..n</sub> (<span style={varStyle}>v</span><sub>i</sub>(t) × <span style={varStyle}>w</span><sub>i</sub>(t)) / Σ<sub>i=1..n</sub> <span style={varStyle}>w</span><sub>i</sub>(t)</div>
                    </div>
                  )}
                </div>

                {/* Variable definitions */}
                <div style={sectionStyle}>
                  <strong>Variable definitions:</strong>
                  <table style={{ marginTop: '0.3rem', fontSize: '0.83rem', borderCollapse: 'collapse', width: '100%' }}>
                    <tbody>
                      <tr>
                        <td style={{ padding: '0.2rem 0.75rem 0.2rem 0', whiteSpace: 'nowrap', verticalAlign: 'top' }}><span style={varStyle}>V<sub>group</sub>(t)</span></td>
                        <td style={{ padding: '0.2rem 0' }}>Aggregated group value for year <span style={varStyle}>t</span></td>
                      </tr>
                      <tr>
                        <td style={{ padding: '0.2rem 0.75rem 0.2rem 0', whiteSpace: 'nowrap', verticalAlign: 'top' }}><span style={varStyle}>v<sub>i</sub>(t)</span></td>
                        <td style={{ padding: '0.2rem 0' }}>Value of "{meta.description}" for country <span style={varStyle}>i</span> in year <span style={varStyle}>t</span></td>
                      </tr>
                      <tr>
                        <td style={{ padding: '0.2rem 0.75rem 0.2rem 0', whiteSpace: 'nowrap', verticalAlign: 'top' }}><span style={varStyle}>n</span>{meta.agg === 'mean' ? <>(t)</> : null}</td>
                        <td style={{ padding: '0.2rem 0' }}>
                          {meta.agg === 'mean'
                            ? <>Number of member countries with non-missing data in year <span style={varStyle}>t</span> (varies by year)</>
                            : 'Total number of member countries in the group'}
                        </td>
                      </tr>
                      <tr>
                        <td style={{ padding: '0.2rem 0.75rem 0.2rem 0', whiteSpace: 'nowrap', verticalAlign: 'top' }}><span style={varStyle}>t</span></td>
                        <td style={{ padding: '0.2rem 0' }}>Year (calendar year of observation)</td>
                      </tr>
                      {meta.agg === 'weighted' && weightMeta && (
                        <tr>
                          <td style={{ padding: '0.2rem 0.75rem 0.2rem 0', whiteSpace: 'nowrap', verticalAlign: 'top' }}><span style={varStyle}>w<sub>i</sub>(t)</span></td>
                          <td style={{ padding: '0.2rem 0' }}>Weight for country <span style={varStyle}>i</span> in year <span style={varStyle}>t</span>, drawn from indicator <code style={codeStyle}>{meta.weight_by}</code> — "{weightMeta.description}"</td>
                        </tr>
                      )}
                    </tbody>
                  </table>
                </div>

                {/* Weight indicator detail */}
                {meta.agg === 'weighted' && weightMeta && (
                  <div style={sectionStyle}>
                    <strong>Weight indicator:</strong> <code style={codeStyle}>{meta.weight_by}</code>
                    <div style={{ marginTop: '0.2rem' }}>
                      Each country's value is weighted by its "{weightMeta.description}" in the same year. This means countries with larger <span style={varStyle}>w<sub>i</sub></span> values exert proportionally more influence on the group aggregate. For example, if the weight is population, a country with 100 million people contributes 10× more to the average than a country with 10 million.
                    </div>
                  </div>
                )}

                {/* Missing data handling */}
                <div style={sectionStyle}>
                  <strong>Missing data handling:</strong>
                  <div style={{ marginTop: '0.2rem' }}>
                    {meta.agg === 'sum' && 'Countries with missing values for a given year are excluded from the sum for that year. This means the group total may undercount the true aggregate in years where coverage is incomplete. Trends should be interpreted with awareness that year-to-year changes may partly reflect changes in data availability.'}
                    {meta.agg === 'mean' && <>The denominator <span style={varStyle}>n</span>(t) counts only countries with non-null values in year <span style={varStyle}>t</span>. If fewer countries report in a given year, the average is computed over the available subset. This can introduce composition effects — apparent trend changes may reflect shifts in which countries reported rather than genuine changes.</>}
                    {meta.agg === 'weighted' && 'A country-year pair is included only when both the indicator value and the weight value are available. If either is missing, that country is excluded from the numerator and denominator for that year. This ensures the weighted average is not biased by unweighted observations.'}
                  </div>
                </div>

                {/* Interpretation guidance */}
                <div style={sectionStyle}>
                  <strong>Interpretation:</strong>
                  <div style={{ marginTop: '0.2rem' }}>
                    {meta.agg === 'sum' && 'The displayed value represents the total across all member countries. It is directly comparable across groups and over time (subject to data availability). When comparing a single country to the group, the "% of group total" shown on metric cards indicates that country\'s share of the group aggregate.'}
                    {meta.agg === 'mean' && 'The displayed value represents the typical (average) level across member countries, treating each country equally. It is useful for comparing what a "representative" country in each group looks like, but does not reflect the group\'s aggregate magnitude.'}
                    {meta.agg === 'weighted' && `The displayed value represents a size-adjusted average across member countries. It answers "what is the ${meta.description.toLowerCase()} experienced by the average unit of ${weightMeta?.description.toLowerCase() ?? 'weight'} in this group?" rather than "what does the average country look like?"`}
                  </div>
                </div>
              </div>
            );
          })()}

          <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap', margin: '1rem 0' }}>
            {(() => {
              const meta = indicators[selectedIndicator];
              const isSumIndicator = meta?.agg === 'sum';
              // For country share: find the first selected group's latest total
              let groupTotal: number | null = null;
              if (isSumIndicator && countryName) {
                for (const gid of selectedGroups) {
                  const gs = chartData[gid];
                  if (gs && gs.values.length > 0) {
                    groupTotal = gs.values[gs.values.length - 1];
                    break;
                  }
                }
              }
              return Object.entries(chartData).map(([group, series]) => {
                if (series.values.length === 0) return null;
                const latest = series.values[series.values.length - 1];
                const latestDate = series.dates[series.dates.length - 1];
                const isCountryCard = countryName !== '' && group === countryName;
                const sharePercent = isCountryCard && isSumIndicator && groupTotal && groupTotal !== 0
                  ? ((latest / groupTotal) * 100)
                  : null;
                return (
                  <div key={group} className="metric-card" style={{ flex: '1', minWidth: '150px' }}>
                    <div className="metric-label">{GROUP_LABELS[group] || group} ({latestDate})</div>
                    <div className="metric-value">{latest.toLocaleString('en-US', { maximumFractionDigits: 2 })}</div>
                    {sharePercent !== null && (
                      <div style={{ fontSize: '0.78rem', color: '#718096', marginTop: '0.15rem' }}>
                        {sharePercent.toFixed(1)}% of group total
                      </div>
                    )}
                  </div>
                );
              });
            })()}
          </div>

          <canvas ref={chartRef} style={{ maxHeight: '400px' }} />

          {/* Data table & CSV download controls */}
          <div style={{ display: 'flex', gap: '0.5rem', marginTop: '1rem' }}>
            <button
              onClick={() => setShowTable(v => !v)}
              style={{
                padding: '0.4rem 0.8rem', border: '1px solid #CBD5E0', borderRadius: '4px',
                background: showTable ? '#003366' : '#fff', color: showTable ? '#fff' : '#4A5568',
                cursor: 'pointer', fontSize: '0.8rem', fontWeight: 500,
              }}
            >
              {showTable ? 'Hide Country Data' : 'Show Country Data'}
            </button>
            {countryData && (
              <button
                onClick={() => {
                  if (!countryData) return;
                  const { dates, countries: ctrs, group } = countryData;
                  const header = ['Date', ...ctrs.map(c => c.name), `${GROUP_LABELS[group] || group} (Total)`];
                  // Build group totals per date from chartData
                  const groupSeries = chartData[group];
                  const groupMap = new Map<string, number>();
                  if (groupSeries) {
                    groupSeries.dates.forEach((d, i) => groupMap.set(d, groupSeries.values[i]));
                  }
                  const rows = dates.map((d, di) => {
                    const vals = ctrs.map(c => c.values[di] !== null && c.values[di] !== undefined ? String(c.values[di]) : '');
                    const total = groupMap.get(d);
                    return [d, ...vals, total !== undefined ? String(total) : ''].join(',');
                  });
                  const csv = [header.join(','), ...rows].join('\n');
                  const blob = new Blob([csv], { type: 'text/csv' });
                  const a = document.createElement('a');
                  a.href = URL.createObjectURL(blob);
                  a.download = `${selectedIndicator}_${selectedGroups[0] || 'data'}.csv`;
                  a.click();
                  URL.revokeObjectURL(a.href);
                }}
                style={{
                  padding: '0.4rem 0.8rem', border: '1px solid #CBD5E0', borderRadius: '4px',
                  background: '#fff', color: '#4A5568', cursor: 'pointer', fontSize: '0.8rem', fontWeight: 500,
                }}
              >
                Download CSV
              </button>
            )}
          </div>

          {/* Country data table */}
          {showTable && countryData && (
            <div className="country-data-table-wrap">
              <table className="country-data-table">
                <thead>
                  <tr>
                    <th>Date</th>
                    {countryData.countries.map(c => <th key={c.id}>{c.name}</th>)}
                    <th style={{ fontWeight: 700 }}>{GROUP_LABELS[countryData.group] || countryData.group} (Total)</th>
                  </tr>
                </thead>
                <tbody>
                  {countryData.dates.map((d, di) => {
                    const groupSeries = chartData[countryData.group];
                    const groupMap = new Map<string, number>();
                    if (groupSeries) {
                      groupSeries.dates.forEach((gd, gi) => groupMap.set(gd, groupSeries.values[gi]));
                    }
                    const total = groupMap.get(d);
                    return (
                      <tr key={d}>
                        <td>{d}</td>
                        {countryData.countries.map(c => (
                          <td key={c.id}>{c.values[di] !== null && c.values[di] !== undefined ? c.values[di]!.toLocaleString('en-US', { maximumFractionDigits: 2 }) : '—'}</td>
                        ))}
                        <td style={{ fontWeight: 700 }}>{total !== undefined ? total.toLocaleString('en-US', { maximumFractionDigits: 2 }) : '—'}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
