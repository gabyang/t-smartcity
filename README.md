# t-smartcity

## Project Description

**t-smartcity** is an intelligent application designed to empower urban planners by transforming raw data into actionable insights. By assuming the presence of an existing data pipeline, our solution streamlines data interaction and visualization to solve critical challenges in urban planning, such as data fragmentation, outdated plans, and lack of stakeholder engagement.

### Key Features:

- **Insights Snapshot**: Provides real-time updates on evolving datasets.
- **Geospatial Visualization**: Displays land use, meteorological, and spatial relationships through interactive maps.
- **Comparative Analysis**: Facilitates benchmarking by comparing datasets across countries for case studies.
- **Synthetic Data Generation**: Simulates scenarios for planning and decision-making by generating files that can be used for various purposes.

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

### How to Test or Use the Solution

For a clear demonstration of the application's features, watch the demonstration video linked below. The video showcases the application's functionality, including insights snapshot, geospatial visualization, and synthetic data generation. Most of testing can be done through the application's interface with stub prompts.

---

## Contributors

- **Pairor Tarin**

  - Role: Developed the map visualization features, gathered various CSV and GeoJSON data into a combined file, studied and implemented GeoPandas, and worked on displaying spatial data in the map visualization page.

- **William Jacob**

  - Role: Debugged synthetic data issues, fixed errors in data generation, and created `main.py` for OpenAI integration. Researched AI agents and implemented them invarious parts of the application.

- **Bryan Castorius Halim**

  - Role: Contributed majorly to the proposal, created the project structure, and worked on the synthetic data generation process. Contributed to AI agent research and implementation. Refined the data generation process.

- **Benjamin**

  - Role: Conducted research on data lakes and assisted in gathering GeoJSON files. Helped create the demonstration video.

- **Gabrie Yang**
  - Role: Worked on data synthesization and generation processes. Managed the project and gathered business insights for the application include the pain points of urban planners and the potential benefits of the solution. Helped create the demonstration video. Did the initial setup of the project.

---

## Additional Notes

### Limitations:

- The cost of API keys adds financial constraints to the application's scalability.
- IBM Watson integration was attempted but faced issues, preventing its successful implementation.
- Currently, the data is limited to Singapore, which restricts its applicability to other regions.
- Most of the data is hardcoded, reducing flexibility and adaptability.
- The application's interface is basic and lacks advanced features for user interaction.

### Future Improvements:

- Expand data coverage to include other countries and regions.
- Enhance the agent's capabilities to be more specialized and context-aware with the data it processes.
- Resolve issues with Watson integration and explore other robust AI services for additional functionality.
- Transition from hardcoded data to a more dynamic and scalable data pipeline.
- Implement a more user-friendly interface with additional features for urban planners.

## YouTube Link

[Watch the Demo](https://youtu.be/wTnNsgIQbqI)

<!-- ### Video Structure:
1. **Introduction**:
   - Briefly introduce the team and the problem being solved.
2. **Demonstration**:
   - Showcase the working solution, highlighting key features and functionality.

----->
