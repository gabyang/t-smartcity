# t-smartcity

## Project Description

**t-smartcity** is an intelligent application designed to empower urban planners by transforming raw data into actionable insights. By assuming the presence of an existing data pipeline, our solution streamlines data interaction and visualization to solve critical challenges in urban planning, such as data fragmentation, outdated plans, and lack of stakeholder engagement.

---

## Problem Statement

Urban planners face several challenges that hinder effective decision-making:

1. **Resource Constraints**:
   - Limited manpower and budgets restrict the ability to analyze large datasets.

2. **Fragmented Data and Long Lead Times**:
   - Collecting, cleaning, and analyzing data often takes months, delaying actionable plans.

3. **Fear and Uncertainty**:
   - Rapid technological advancements and external pressures (e.g., geopolitical, economic) create uncertainty in planning.

4. **Stakeholder Alignment**:
   - Gaining buy-in from multiple stakeholders requires consistent and clear communication, often lacking in current workflows.

## Solution Features

t-smartcity tackles these challenges with the following robust features:

### 1. **Exploratory Data Insights**
- Provides real-time insights into key urban metrics, reducing dependency on external consultants.
- Automates synchronization and onboarding processes to save time and resources.

### 2. **Predictive Modeling**
- Uses synthetic data generation to forecast future scenarios, enabling proactive decision-making.
- Machine learning models predict trends and anticipate stakeholder needs.

### 3. **Comparative Country Analysis**
- Benchmarks city performance against global standards using cross-country datasets.
- Offers dynamic visualizations to highlight actionable insights from comparative studies.

### 4. **Geospatial Visualization**
- Interactive maps display land use, meteorological patterns, and urban layouts.
- Supports IoT data integration for real-time analytics and advanced scenario planning.

### 5. **Data Privacy and Compliance**
- Anonymizes sensitive data to ensure compliance with privacy regulations.
- Implements explainable AI techniques to mitigate bias and build trust.

### 6. **Agent Framework**
- Modular AI agents handle diverse tasks such as comparative analysis, report generation, and scenario planning.
- Each agent is designed to specialize in specific urban planning problems, enhancing system flexibility.

---

## Architecture and Scalability

### System Architecture
The application sits at the intersection of **data engineering** and **data analysis**, leveraging the following layers:
- **Data Layer**: Processes and stores structured and unstructured data (e.g., GeoJSON, CSV).
- **AI/ML Layer**: Includes agents for prediction, clustering, and scenario simulation.
- **Visualization Layer**: Generates interactive dashboards and geospatial maps.

### Scalability
- **Small Cities**:
  - Start with basic roadmaps and land-use visualizations.
- **Large Cities**:
  - Integrate IoT data, real-time analytics, and advanced predictive capabilities.
- **Future Work**:
  - Incorporate qualitative data from surveys, focus groups, and mental maps.
  - Expand to support domain-specific large language models (LLMs) and computer vision agents.

---

## Setup Instructions

### Prerequisites

- **Python**: Version 3.12 or higher.
- **Required Python Libraries**:
  - `streamlit`
  - `geopandas`
  - `pandas`
  - `numpy`
  - `plotly`
  - `openai`
  - `python-dotenv`

### Steps to Run Locally

1. **Clone the Repository**:

```bash
git clone https://github.com/gabyang/t-smartcity.git
cd t-smartcity
```

2. **Set Up a Virtual Environment (optional but recommended) and install requirements**:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Ask the team for the `.env` file**:
   Request the team for the `.env` file containing the API keys and other sensitive information.
   You can also create your own `.env` file with the following structure:

```bash
OPENAI_API_KEY="your_openai_api_key"
SERP_API_KEY="your_serp_api_key"
```

4. **Run the web application with `streamlit`**:

```bash
streamlit run smart_planner_app.py
```

---

## Usage Guide

### Features Demonstration
1. **Data Insights**:
   - Run exploratory tools for understanding trends and anomalies in datasets.
2. **Predictive Modeling**:
   - Use the predictive agent to forecast future scenarios and evaluate stakeholder needs.
3. **Geospatial Visualization**:
   - Visualize urban layouts and land use with GeoJSON integrations.
4. **Comparative Analysis**:
   - Benchmark cities using advanced analysis and visualizations.

### How to Test or Use the Solution

For a clear demonstration of the application's features, watch the demonstration video linked below. The video showcases the application's functionality, including insights snapshot, geospatial visualization, and synthetic data generation. Most of testing can be done through the application's interface with stub prompts.

---

## Contributors

- **Gabriel Yang**:
  - Managed the project, contributed business insights, and led data synthesization efforts.
- **Bryan Castorius Halim**:
  - Developed the project structure and contributed to synthetic data generation.
- **William Jacob**:
  - Debugged synthetic data issues and integrated AI agents into various modules.
- **Pairor Tarin**:
  - Created map visualizations and implemented GeoPandas-based features.
- **Benjamin**:
  - Conducted research on data lakes and assisted in demonstration video creation.
---

## Additional Notes

### Limitations:

- The cost of API keys adds financial constraints to the application's scalability.
- IBM Watson integration was attempted but faced issues, preventing its successful implementation.
- Currently, the data is limited to Singapore, which restricts its applicability to other regions.
- Most of the data is hardcoded, reducing flexibility and adaptability.
- The application's interface is basic and lacks advanced features for user interaction.

## Future Improvements

- **Expanded Data Coverage**:
  - Include data from multiple countries and regions for broader applicability.
- **Advanced AI Agents**:
  - Integrate domain-specific large language models and computer vision capabilities.
- **Enhanced Interface**:
  - Develop a more user-friendly and interactive dashboard for urban planners.
- **Scalable Data Pipeline**:
  - Transition from hardcoded data to a dynamic and scalable infrastructure.
- **Watson AI Integration**:
  - Revisit IBM Watson integration to expand the application’s AI capabilities.


## YouTube Link

[Watch the Demo](https://youtu.be/wTnNsgIQbqI)

<!-- ### Video Structure:
1. **Introduction**:
   - Briefly introduce the team and the problem being solved.
2. **Demonstration**:
   - Showcase the working solution, highlighting key features and functionality.

----->
