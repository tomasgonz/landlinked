# Booklet - Country Insights Dashboard

A comprehensive Streamlit application for exploring country-specific data across economic, social, and environmental domains. Booklet aggregates data from the World Bank, REST Countries API, and the CIA World Factbook into interactive dashboards with visualizations, comparative group analysis, and AI-powered Q&A.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Data Sources](#data-sources)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Country Profiles**: Detailed views with flags, capital, borders, climate, industries, trade partners, and geographic maps.
- **144 World Bank Indicators**: Organized across 18 categories including economy, health, education, environment, labor, trade, infrastructure, and more.
- **Group Comparison**: Compare aggregated indicators across 45 country groups (LLDCs, LDCs, SIDS, G77, OECD, EU, G20, BRICS, AOSIS, NATO, ASEAN, and many others) with downloadable Excel exports.
- **AI-Powered Q&A**: Ask questions about any country using OpenAI GPT-4o-mini and get factual, contextual answers.
- **Interactive Maps**: Geographic visualization powered by Folium.
- **Admin Dashboard**: Password-protected interface for data updates, cache management, configuration, and log viewing.
- **Smart Caching**: 30-day indicator cache with rate-limited API calls, concurrent fetching, and automatic retry logic.

## Installation

### Prerequisites

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/) (recommended) or pip

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/tomasgonz/booklet.git
   cd booklet
   ```

2. **Create a virtual environment and install dependencies**

   Using Poetry:
   ```bash
   poetry install
   ```

   Or using pip with a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install streamlit watchdog folium streamlit-folium fpdf html2text openai python-dotenv pyyaml shell xlsxwriter openpyxl
   ```

3. **Configure secrets**

   Create `.streamlit/secrets.toml`:
   ```toml
   [openai]
   api_key = "your-openai-api-key"

   [admin]
   password = "your-admin-password"
   ```

4. **Run the application**

   ```bash
   streamlit run Home.py
   ```

   The dashboard will be available at `http://localhost:8501`.

## Configuration

### Secrets (`.streamlit/secrets.toml`)

| Key | Description |
|-----|-------------|
| `openai.api_key` | OpenAI API key for the AI Q&A feature |
| `admin.password` | Password for the admin dashboard |

This file is excluded from version control via `.gitignore`.

### Application Settings (`config.yaml`)

```yaml
app:
  group_name: "LLDCs"              # Default country group
  show_group_selector: true         # Show/hide group selector in sidebar
  sidebar_width: 300                # Sidebar width in pixels
  css_customizations:
    main_font: "Arial"
    h1_font_size: "2.5rem"
    h1_font_weight: "bold"

display:
  show_quotes: true                 # Show motivational quotes in sidebar
  display_charts: true              # Enable/disable chart rendering
```

These settings can also be modified at runtime through the admin dashboard.

## Usage

### Main Dashboard (`Home.py`)

1. **Select a group** from the sidebar (LLDCs, LDCs, SIDS).
2. **Select a country** from the country list.
3. **Browse sections** using the floating navigation menu:
   - Country profile and geographic info
   - Environment (CO2 emissions, climate)
   - Labor Force statistics
   - Population indicators
   - Education metrics
   - Connectivity data
   - Economy (GDP, inflation, trade, debt)
4. **Ask questions** using the AI Q&A input box for GPT-powered answers about the selected country.

### Group Comparison (`pages/Groups.py`)

1. **Select multiple country groups** to compare.
2. **Select indicator categories** (economy, health, education, etc.).
3. **View comparative line charts** showing trends across groups over time.
4. **Download data** as Excel (XLSX) files.

Aggregation is applied per indicator type: sum, mean, or weighted by population/GDP.

### Admin Dashboard (`admin_page.py`)

Run on a separate port:
```bash
streamlit run admin_page.py --server.port 8502
```

Tabs:
- **Data Update**: Download/refresh World Bank indicators by group, clear cache.
- **Settings**: Modify runtime configuration (group name, display options, CSS).
- **Access Logs**: View Nginx access logs and application journal logs.

### Bulk Data Update

To download all indicators for all groups:
```bash
python data_update.py
```

## Project Structure

```
booklet/
├── Home.py                  # Main dashboard entry point
├── Admin.py                 # Legacy admin utilities (factbook/map import)
├── admin_page.py            # Admin dashboard (runs on port 8502)
├── config.yaml              # Application configuration
├── pyproject.toml           # Poetry project metadata
├── poetry.lock              # Locked dependencies
├── booklet.service          # Systemd service (main app)
├── booklet-admin.service    # Systemd service (admin app)
│
├── pages/
│   └── Groups.py            # Multi-group comparison page
│
├── indicators.py            # World Bank API client with caching
├── indicators_data.py       # 144 indicator definitions & 18 categories
├── groups.py                # Country group management & code conversions
├── country_facts.py         # Country data from REST Countries & Factbook
├── data_ops.py              # Data aggregation & normalization
├── maps.py                  # Geographic coordinate parsing & Folium maps
├── css.py                   # Custom CSS styling
├── quotes.py                # Motivational quotes loader
├── data_update.py           # Batch data download script
│
├── cache/
│   ├── indicators/          # Cached World Bank indicator data (JSON)
│   ├── factbook/            # CIA World Factbook data (270+ countries)
│   ├── groups/              # 45 country group definitions (JSON)
│   ├── maps/                # Country map images
│   ├── country_facts.json   # REST Countries API data
│   ├── countries.json       # Country descriptions/profiles
│   ├── Countrycodesfull.json # Country code mappings
│   └── quotes.json          # Motivational quotes
│
├── .streamlit/
│   └── secrets.toml         # API keys & admin password (not committed)
│
└── .gitignore
```

### Key Modules

| Module | Role |
|--------|------|
| `indicators.py` | World Bank API client. Handles fetching, caching (30-day TTL), rate limiting (0.5s delay), concurrent requests (8 workers), retry logic, and pagination. |
| `indicators_data.py` | Defines 144 indicators across 18 categories, each with source, description, and aggregation method (sum, mean, weighted). |
| `groups.py` | Manages 45 country groupings. Provides ISO3/ISO2/FIPS code conversions. |
| `country_facts.py` | Loads country metadata from REST Countries API and CIA World Factbook. Provides flags, descriptions, and qualitative info. |
| `data_ops.py` | Aggregates indicator data at the group level. Supports sum, mean, and weighted (by population/GDP) aggregation. |
| `maps.py` | Parses DMS coordinates and generates interactive Folium maps. |
| `css.py` | Custom CSS for layout, cards, metrics, and the floating navigation menu. |
| `quotes.py` | Loads and displays random motivational quotes in the sidebar. |

## Architecture

### Data Flow

```
User selects group + country
        │
        ▼
Check local cache (cache/indicators/)
        │
   ┌────┴────┐
   │ Cached?  │
   └────┬────┘
   Yes  │  No
   │    │    │
   │    ▼    │
   │  World Bank API ──► Rate limit (0.5s)
   │    │                  │
   │    ▼                  ▼
   │  Paginate ──► Concurrent fetch (8 workers)
   │    │
   │    ▼
   │  Save to cache (JSON)
   │    │
   └────┴────┐
             ▼
   Normalize to DataFrame
        │
        ▼
   Render charts / compute aggregates / export
```

### Indicator Categories

General, Economy, Inequality & Poverty, Trade & Finance, Investment & Financial Sector, Debt & Aid, Government & Governance, Education, Health, Labor & Employment, Gender, Infrastructure & Technology, Energy, Environment & Climate, Agriculture, Urban Development, Water Sanitation & Waste, Science & Innovation.

### Country Groups

45 country group definitions are available in `cache/groups/`. The most commonly used groups include:

| Code | Group |
|------|-------|
| `lldcs` | Landlocked Developing Countries |
| `ldcs` | Least Developed Countries |
| `sids` | Small Island Developing States |
| `g77` | Group of 77 |
| `oecd` | Organisation for Economic Co-operation and Development |
| `eu` | European Union |
| `g20` | Group of Twenty |
| `brics` | BRICS |
| `aosis` | Alliance of Small Island States |
| `lmcs` | Lower Middle-Income Countries |
| `lics` | Low-Income Countries |
| `nato` | North Atlantic Treaty Organization |
| `asean` | Association of Southeast Asian Nations |
| `un` | United Nations |
| `g24` | Group of Twenty-Four |
| `gcc` | Gulf Cooperation Council |
| `eac` | East African Community |
| `ecowas` | Economic Community of West African States |
| `mercosur` | Southern Common Market |
| `caricom` | Caribbean Community |
| `sadc` | Southern African Development Community |
| `au` | African Union |
| `hics` | High-Income Countries |
| `pif` | Pacific Islands Forum |
| `las` | League of Arab States |
| `oic` | Organisation of Islamic Cooperation |
| `nam` | Non-Aligned Movement |
| `cw` | Commonwealth of Nations |
| `nordic` | Nordic Countries |

Additional groups: `acd`, `acp`, `ag`, `ap`, `can`, `canz`, `cegpl`, `cplp`, `grulac`, `ida`, `ioc`, `oas`, `osce`, `sica`, `umcs`, `weog`, `zangger`.

## Data Sources

- **[World Bank API](https://api.worldbank.org/v2/)** - Economic, social, and environmental indicators
- **[REST Countries API](https://restcountries.com/v3.1/)** - Country metadata (flags, borders, capitals, languages)
- **[CIA World Factbook](https://www.cia.gov/the-world-factbook/)** - Climate, industries, geography, demographics
- **[OpenAI GPT-4o-mini](https://openai.com/)** - AI-powered country Q&A

## Deployment

### Systemd Services

Two systemd unit files are provided for production deployment:

**Main application** (`booklet.service` on port 8501):
```bash
sudo cp booklet.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now booklet
```

**Admin dashboard** (`booklet-admin.service` on port 8502):
```bash
sudo cp booklet-admin.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now booklet-admin
```

Both services bind to `127.0.0.1` and are designed to sit behind a reverse proxy (e.g., Nginx) for HTTPS termination.

### Reverse Proxy

Configure Nginx (or similar) to proxy requests to the Streamlit ports:

```nginx
location / {
    proxy_pass http://127.0.0.1:8501;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
}
```

WebSocket support (`Upgrade` / `Connection` headers) is required for Streamlit.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

## License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/) - Web application framework
- [OpenAI](https://openai.com/) - GPT-4o-mini API for AI Q&A
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Folium](https://folium.readthedocs.io/) - Interactive maps
- [World Bank](https://data.worldbank.org/) - Open data platform
- [REST Countries](https://restcountries.com/) - Country metadata API

---

*Disclaimer: The data presented in this application is for informational purposes only. While efforts are made to ensure accuracy and currency, no guarantees are provided regarding the completeness or reliability of the information. Users are advised to verify data from official sources.*
