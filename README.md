# Booklet, a country insights dashboard

Welcome to the **Country Insights Dashboard**, a comprehensive Streamlit application that provides detailed information about various countries. This dashboard offers insightful visualizations and factual data to help users explore country-specific information across various domains.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Interactive Dashboard**: Navigate through different sections such as Environment, Labor Force, Population, Education, Connectivity, and Economy.
- **Group Selector**: Choose from various country groups like LDCs, LLDCs, SIDS, EU, OECD, BRICS, G7, G20, and G77 to explore specific data.
- **Detailed Country Profiles**: Access comprehensive information including climate, economic indicators, population statistics, and more.
- **AI-Powered Q&A**: Utilize OpenAI's GPT-4 to ask specific questions about selected countries and receive detailed, factual responses.
- **Data Visualizations**: View interactive charts and maps generated using Streamlit, Pandas, and Folium.
- **Random Quotes**: Enjoy motivational quotes related to global perspectives displayed in the sidebar.
- **Responsive Design**: Custom CSS ensures a user-friendly and aesthetically pleasing interface.

## Demo

![Dashboard Screenshot](./screenshots/dashboard.png)

*Figure: Sample view of the Country Insights Dashboard showcasing the Environment section for a selected country.*

## Installation

### Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tomasgonz/booklet.git
   cd country-insights-dashboard
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables

The application uses environment variables to manage sensitive information like API keys. Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Configuration File

Ensure a `config.yaml` file exists in the root directory to manage application settings. Below is a sample configuration:

```yaml
app:
  show_group_selector: true
```

Adjust the settings as needed to enable or disable features.

## Usage

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

Once the server starts, open your web browser and navigate to the URL provided in the terminal (typically `http://localhost:8501`).

### Navigating the Dashboard

1. **Group Selector**: Use the sidebar to select a group of countries (e.g., EU, BRICS).
2. **Country Selection**: Choose a specific country from the list to view detailed information.
3. **Sections**: Utilize the floating menu on the right to jump to different sections like Environment, Labor Force, etc.
4. **AI Q&A**: Enter your questions about the selected country in the provided input box to receive AI-generated responses.

## Project Structure

```
country-insights-dashboard/
├── app.py
├── config.yaml
├── .env
├── requirements.txt
├── indicators/
│   └── indicators.py
├── groups/
│   └── groups.py
├── country_facts/
│   └── country_facts.py
├── quotes/
│   └── quotes.py
├── maps/
│   └── maps.py
├── cache/
│   └── maps/
├── screenshots/
│   └── dashboard.png
├── README.md
└── LICENSE
```

- **app.py**: Main Streamlit application script.
- **config.yaml**: Configuration file for app settings.
- **.env**: Environment variables file (ensure this is excluded from version control).
- **indicators/**, **groups/**, **country_facts/**, **quotes/**, **maps/**: Modules handling different data sources and functionalities.
- **cache/**: Directory for cached data and maps.
- **screenshots/**: Sample screenshots of the application.
- **requirements.txt**: Python dependencies.
- **README.md**: Project documentation.
- **LICENSE**: License information.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your message here"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure that your contributions adhere to the project's coding standards and include relevant tests.

## License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web application framework.
- [OpenAI](https://openai.com/) for providing the GPT-4 API.
- [Pandas](https://pandas.pydata.org/) and [Folium](https://folium.readthedocs.io/) for data manipulation and mapping.
- All data sources used in this project are credited appropriately within the application.

---

*Disclaimer: The data presented in this application is for informational purposes only. While efforts are made to ensure accuracy and currency, no guarantees are provided regarding the completeness or reliability of the information. Users are advised to verify data from official sources.*
