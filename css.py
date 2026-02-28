css_general = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

    /* ── CSS Custom Properties ────────────────────────────────────────── */
    :root {
        --navy:           #003366;
        --navy-light:     #004080;
        --navy-dark:      #002244;
        --teal:           #0097A7;
        --teal-light:     #B2EBF2;
        --bg-primary:     #FFFFFF;
        --bg-card:        #FFFFFF;
        --bg-hover:       #F7F8FA;
        --border-light:   #E2E8F0;
        --border-medium:  #CBD5E0;
        --text-primary:   #1A202C;
        --text-secondary: #4A5568;
        --text-muted:     #718096;
        --font-family:    'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        --radius-sm:      4px;
        --radius-md:      8px;
        --radius-lg:      12px;
        --shadow-sm:      0 1px 3px rgba(0,0,0,0.08);
        --shadow-md:      0 2px 8px rgba(0,0,0,0.10);
    }

    /* ── Global Typography ────────────────────────────────────────────── */
    html, body, [class*="css"]:not([data-testid="stIconMaterial"]) {
        font-family: var(--font-family) !important;
    }

    .stApp {
        font-family: var(--font-family) !important;
    }

    .reportview-container .main .block-container,
    .stApp > header + div > div > div > div > section > div {
        padding: 2rem 2.5rem;
        font-family: var(--font-family) !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: var(--font-family) !important;
        color: var(--navy) !important;
        font-weight: 600 !important;
    }

    h1 {
        font-size: 2.2rem !important;
        letter-spacing: -0.02em;
    }

    h2 {
        font-size: 1.6rem !important;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--border-light);
        margin-bottom: 1rem;
    }

    h3 {
        font-size: 1.25rem !important;
    }

    p, li, span:not([data-testid="stIconMaterial"]), div {
        font-family: var(--font-family) !important;
    }

    /* ── Navy Sidebar ─────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--navy-dark) 0%, var(--navy) 100%) !important;
    }

    [data-testid="stSidebar"] *:not([data-testid="stIconMaterial"]) {
        color: #FFFFFF !important;
        font-family: var(--font-family) !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label {
        color: rgba(255,255,255,0.85) !important;
        font-weight: 500;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    [data-testid="stSidebar"] .stSelectbox > div > div,
    [data-testid="stSidebar"] .stMultiSelect > div > div {
        background-color: rgba(255,255,255,0.1) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: var(--radius-md) !important;
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] .stSelectbox > div > div:hover,
    [data-testid="stSidebar"] .stMultiSelect > div > div:hover {
        border-color: var(--teal) !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.15) !important;
    }

    [data-testid="stSidebar"] .stCaption p {
        color: rgba(255,255,255,0.6) !important;
    }

    /* ── Metric Cards ─────────────────────────────────────────────────── */
    [data-testid="stMetric"] {
        background: var(--bg-card);
        border-left: 4px solid var(--navy);
        border-radius: var(--radius-md);
        padding: 0.75rem 1rem;
        box-shadow: var(--shadow-sm);
    }

    [data-testid="stMetric"] label {
        color: var(--text-muted) !important;
        font-size: 0.8rem !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: var(--navy) !important;
        font-weight: 700 !important;
        font-size: 1.4rem !important;
    }

    /* ── Container / Card Styling ─────────────────────────────────────── */
    [data-testid="stVerticalBlock"] > div > div[data-testid="stExpander"],
    div[data-testid="stContainer"] {
        border-radius: var(--radius-md) !important;
    }

    div.stContainer[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--border-light) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: var(--shadow-sm) !important;
    }

    /* ── Section Header ───────────────────────────────────────────────── */
    .section-header {
        display: flex;
        align-items: center;
        margin: 2rem 0 1rem 0;
        padding: 0;
    }

    .section-header::before {
        content: '';
        display: inline-block;
        width: 5px;
        height: 1.6rem;
        background: var(--navy);
        border-radius: 3px;
        margin-right: 0.75rem;
        flex-shrink: 0;
    }

    .section-header h2 {
        margin: 0 !important;
        padding: 0 !important;
        border-bottom: none !important;
        font-size: 1.5rem !important;
        line-height: 1.4;
    }

    /* ── Card Title ───────────────────────────────────────────────────── */
    .card-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--navy);
        padding: 0.5rem 0;
        margin-bottom: 0.25rem;
        font-family: var(--font-family);
    }

    /* ── Factbook Text ────────────────────────────────────────────────── */
    .factbook-text {
        background: var(--bg-hover);
        border-left: 4px solid var(--teal);
        border-radius: 0 var(--radius-md) var(--radius-md) 0;
        padding: 0.85rem 1.1rem;
        margin: 0.75rem 0;
        font-size: 0.9rem;
        line-height: 1.65;
        color: var(--text-primary);
        font-family: var(--font-family);
    }

    .factbook-text strong {
        color: var(--navy);
        font-weight: 600;
    }

    /* ── Country Meta Item (Right Column) ─────────────────────────────── */
    .country-meta-item {
        background: var(--bg-card);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-md);
        padding: 0.6rem 0.85rem;
        margin-bottom: 0.5rem;
        font-size: 0.88rem;
        line-height: 1.5;
        font-family: var(--font-family);
    }

    .country-meta-item strong {
        display: block;
        color: var(--text-muted);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 0.15rem;
        font-weight: 600;
    }

    /* ── Quote Block ──────────────────────────────────────────────────── */
    .quote-block {
        background: rgba(255,255,255,0.08);
        border-left: 3px solid var(--teal);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 0.65rem 0.85rem;
        margin: 0.75rem 0;
        font-style: italic;
        font-size: 0.85rem;
        line-height: 1.55;
        color: rgba(255,255,255,0.9);
        font-family: var(--font-family);
    }

    .quote-block .quote-author {
        display: block;
        margin-top: 0.35rem;
        font-style: normal;
        font-weight: 600;
        font-size: 0.8rem;
        color: var(--teal-light);
    }

    /* ── Disclaimer Text ──────────────────────────────────────────────── */
    .disclaimer-text {
        font-size: 0.72rem;
        line-height: 1.5;
        color: rgba(255,255,255,0.45);
        margin-top: 1.5rem;
        padding-top: 0.75rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        font-family: var(--font-family);
    }

    /* ── Sidebar Country Item ─────────────────────────────────────────── */
    .sidebar-country-item {
        display: inline-block;
        padding: 0.2rem 0.55rem;
        margin: 0.15rem 0.1rem;
        background: rgba(255,255,255,0.08);
        border-radius: var(--radius-sm);
        font-size: 0.82rem;
        color: rgba(255,255,255,0.85);
        font-family: var(--font-family);
        transition: background 0.2s;
    }

    .sidebar-country-item:hover {
        background: rgba(255,255,255,0.15);
    }

    /* ── AI Q&A Container ─────────────────────────────────────────────── */
    .ai-qa-container {
        background: var(--bg-card);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-lg);
        padding: 1.25rem;
        margin: 1rem 0;
    }

    .ai-qa-container .ai-disclaimer {
        font-size: 0.75rem;
        color: var(--text-muted);
        background: #FFF8E1;
        border: 1px solid #FFE082;
        border-radius: var(--radius-sm);
        padding: 0.5rem 0.75rem;
        margin-top: 0.75rem;
        line-height: 1.5;
        font-family: var(--font-family);
    }

    /* ── Floating Menu ────────────────────────────────────────────────── */
    .floating-menu {
        position: fixed;
        top: 50%;
        right: 0;
        transform: translateY(-50%);
        background: var(--navy);
        padding: 12px 16px;
        border-radius: var(--radius-lg) 0 0 var(--radius-lg);
        box-shadow: var(--shadow-md);
        z-index: 1000;
        transition: transform 0.3s ease;
    }

    .floating-menu .menu-header {
        cursor: pointer;
        font-weight: 600;
        color: #FFFFFF;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding-bottom: 0.25rem;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        margin-bottom: 0.25rem;
        font-family: var(--font-family);
    }

    .menu-content {
        display: none;
    }

    .menu-content a {
        display: block;
        padding: 0.35rem 0.5rem;
        margin: 0.2rem 0;
        text-decoration: none;
        color: rgba(255,255,255,0.85) !important;
        font-weight: 500;
        font-size: 0.82rem;
        border-radius: var(--radius-sm);
        transition: all 0.2s ease;
        font-family: var(--font-family);
    }

    .menu-content a:hover {
        color: #FFFFFF !important;
        background-color: var(--teal);
    }

    .menu-header:hover + .menu-content,
    .menu-content:hover {
        display: block;
    }

    /* ── Download Button ──────────────────────────────────────────────── */
    .stDownloadButton > button {
        background-color: var(--navy) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        font-weight: 500 !important;
        font-family: var(--font-family) !important;
        padding: 0.4rem 1.2rem !important;
        font-size: 0.85rem !important;
        transition: background 0.2s;
    }

    .stDownloadButton > button:hover {
        background-color: var(--navy-light) !important;
    }

    /* ── Chart Spacing & Captions ─────────────────────────────────────── */
    [data-testid="stVegaLiteChart"] {
        margin-top: 0.5rem;
    }

    .stCaption p {
        font-size: 0.78rem !important;
        color: var(--text-muted) !important;
        font-family: var(--font-family) !important;
    }

    /* ── Dataframe Borders ────────────────────────────────────────────── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border-light);
        border-radius: var(--radius-md);
        overflow: hidden;
    }

    /* ── Text Input in Main Area ──────────────────────────────────────── */
    .stTextInput > div > div {
        border-radius: var(--radius-md) !important;
        border-color: var(--border-medium) !important;
        font-family: var(--font-family) !important;
    }

    .stTextInput > div > div:focus-within {
        border-color: var(--navy) !important;
        box-shadow: 0 0 0 1px var(--navy) !important;
    }

    /* ── Hide Streamlit bottom nav bar ───────────────────────────────── */
    [data-testid="stBottomBlockContainer"] {
        display: none !important;
    }

    /* ── Hide broken material icon text in Streamlit UI ──────────────── */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* ── Divider ──────────────────────────────────────────────────────── */
    hr {
        border-color: var(--border-light) !important;
    }

    /* ── Sidebar Branded Header ───────────────────────────────────────── */
    .sidebar-brand {
        padding: 0.5rem 0 1rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        margin-bottom: 1rem;
    }

    .sidebar-brand h1 {
        color: #FFFFFF !important;
        font-size: 1.4rem !important;
        margin: 0 !important;
        letter-spacing: -0.01em;
    }

    .sidebar-brand .brand-subtitle {
        color: rgba(255,255,255,0.6);
        font-size: 0.8rem;
        margin-top: 0.15rem;
        font-family: var(--font-family);
    }

    .sidebar-brand .brand-author {
        color: rgba(255,255,255,0.45);
        font-size: 0.72rem;
        margin-top: 0.25rem;
        font-family: var(--font-family);
    }

    /* ── Groups Page Comparison Card ──────────────────────────────────── */
    .comparison-card-header {
        border-left: 4px solid var(--navy);
        padding-left: 0.75rem;
        margin: 1.5rem 0 0.75rem 0;
    }

    .comparison-card-header h3 {
        margin: 0 !important;
        font-size: 1.1rem !important;
        line-height: 1.3;
    }

    .comparison-card-header .card-subtitle {
        color: var(--text-muted);
        font-size: 0.8rem;
        margin-top: 0.15rem;
        font-family: var(--font-family);
    }

    /* ── Groups Page ─────────────────────────────────────────────────── */
    .group-card {
        background: var(--bg-card);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-md);
        padding: 1.1rem 1.25rem;
        margin-bottom: 0.85rem;
        transition: all 0.2s;
        font-family: var(--font-family);
    }

    .group-card.highlighted {
        border-left: 4px solid var(--teal);
        box-shadow: var(--shadow-md);
        background: #FAFFFE;
    }

    .group-card.dimmed {
        opacity: 0.45;
    }

    .group-card-header {
        display: flex;
        align-items: baseline;
        gap: 0.6rem;
        margin-bottom: 0.35rem;
        flex-wrap: wrap;
    }

    .group-acronym {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--navy);
        font-family: var(--font-family);
    }

    .group-fullname {
        font-size: 0.92rem;
        color: var(--text-secondary);
        font-family: var(--font-family);
    }

    .group-meta {
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
        font-family: var(--font-family);
    }

    .classifier-badge {
        display: inline-block;
        background: var(--bg-hover);
        padding: 0.12rem 0.5rem;
        border-radius: var(--radius-sm);
        font-size: 0.73rem;
        font-weight: 500;
        color: var(--text-secondary);
        font-family: var(--font-family);
    }

    .group-description {
        font-size: 0.85rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 0.65rem;
        font-family: var(--font-family);
    }

    .country-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.3rem;
    }

    .country-chip {
        display: inline-block;
        padding: 0.18rem 0.5rem;
        background: var(--bg-hover);
        border-radius: var(--radius-sm);
        font-size: 0.78rem;
        color: var(--text-primary);
        font-family: var(--font-family);
        transition: all 0.15s;
        line-height: 1.5;
    }

    .country-chip.active {
        background: var(--teal);
        color: #FFFFFF;
        font-weight: 600;
    }

    .membership-summary {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin-bottom: 1.5rem;
    }

    .membership-badge {
        display: inline-block;
        padding: 0.3rem 0.7rem;
        background: var(--navy);
        color: #FFFFFF;
        border-radius: var(--radius-md);
        font-size: 0.82rem;
        font-weight: 500;
        font-family: var(--font-family);
    }

    .groups-stats {
        display: flex;
        gap: 2rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }

    .groups-stat-item {
        text-align: center;
    }

    .groups-stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--navy);
        line-height: 1.2;
        font-family: var(--font-family);
    }

    .groups-stat-label {
        font-size: 0.78rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-family: var(--font-family);
    }

    /* ── Page Navigation Links ───────────────────────────────────────── */
    .nav-links {
        display: flex;
        gap: 0.25rem;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid rgba(255,255,255,0.15);
    }

    .nav-links a {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        color: rgba(255,255,255,0.7) !important;
        text-decoration: none !important;
        font-size: 0.82rem;
        font-weight: 500;
        border-radius: var(--radius-sm);
        transition: all 0.2s;
        font-family: var(--font-family);
    }

    .nav-links a:hover {
        color: #FFFFFF !important;
        background: rgba(255,255,255,0.1);
    }

    .nav-links a.active {
        color: #FFFFFF !important;
        background: var(--teal);
        font-weight: 600;
    }

    /* ── Group Detail Header (Mode C) ────────────────────────────────── */
    .group-detail-header .group-acronym {
        font-size: 2.2rem;
    }

    .group-detail-header .group-fullname {
        font-size: 1.1rem;
    }

    /* ── Story Cards ─────────────────────────────────────────────────── */
    .story-card {
        background: var(--bg-card);
        border: 1px solid var(--border-light);
        border-radius: var(--radius-md);
        padding: 1.1rem 1.25rem;
        margin-bottom: 0.85rem;
        transition: all 0.2s;
        font-family: var(--font-family);
    }

    .story-card:hover {
        border-color: var(--teal);
        box-shadow: var(--shadow-md);
    }

    .story-card h3 {
        color: var(--navy) !important;
        font-size: 1.15rem !important;
    }

    .story-meta {
        font-size: 0.82rem;
        color: var(--text-muted);
        margin: 0.35rem 0 0.5rem 0;
        font-family: var(--font-family);
    }

    .story-preview {
        font-size: 0.88rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin-top: 0.4rem;
        font-family: var(--font-family);
    }

    /* ── Material icons ─ ensure font renders glyphs, not text ──────── */
    /* Streamlit uses Emotion CSS-in-JS with data-testid="stIconMaterial" */
    [data-testid="stIconMaterial"],
    [data-testid="stSidebar"] [data-testid="stIconMaterial"],
    .stApp [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
        font-weight: normal !important;
        font-style: normal !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        white-space: nowrap !important;
        word-wrap: normal !important;
        direction: ltr !important;
        -webkit-font-feature-settings: 'liga' !important;
        font-feature-settings: 'liga' !important;
        -webkit-font-smoothing: antialiased;
    }
</style>
"""

css_menu = """
    <div class="floating-menu">
        <div class="menu-header">Sections</div>
        <div class="menu-content">
            <a href="#environment">Environment</a>
            <a href="#labor-force">Labor Force</a>
            <a href="#population">Population</a>
            <a href="#education">Education</a>
            <a href="#connectivity">Connectivity</a>
            <a href="#economy">Economy</a>
        </div>
    </div>
"""
