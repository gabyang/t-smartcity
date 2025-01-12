# t-smartcity

## Project Description
**t-smartcity** is an intelligent application designed to empower urban planners by transforming raw data into actionable insights. By assuming the presence of an existing data pipeline, our solution streamlines data interaction and visualization to solve critical challenges in urban planning, such as data fragmentation, outdated plans, and lack of stakeholder engagement. 

### Key Features:
- **Insights Snapshot**: Provides real-time updates on evolving datasets.
- **Geospatial Visualization**: Displays land use, meteorological, and spatial relationships through interactive maps.
- **Comparative Analysis**: Facilitates benchmarking by comparing datasets across countries for case studies.
- **Synthetic Data Generation**: Simulates scenarios for planning and decision-making.

---

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
Set Up a Virtual Environment (optional but recommended) and install requirements:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run the web application with `streamlit`
```bash
streamlit run smart_planner_app.py
```

---

## Usage Guide
### How to Test or Use the Solution
<!-- 1. **Upload Your Dataset**:
   - Instructions for uploading or accessing sample datasets.
2. **Explore Features**:
   - Walkthrough of key features like insights snapshot, geospatial visualization, and synthetic data generation.
3. **Export Results**:
   - Guide on exporting visualizations and reports for stakeholders. -->

### Examples:
<!-- - Example scenarios or datasets for testing the application. -->

<!-- ---

## Deployment Instructions (if applicable)
### Steps to Deploy:
1. **Prepare the Environment**:
   - Ensure all prerequisites are installed.
2. **Build and Deploy**:
   - Detailed deployment steps for cloud or local environments.
3. **Post-Deployment Verification**:
   - Checklist for verifying the application is working as expected. -->

---
## Contributors
- **Pairor Tarin**  
  - Role: Developed the map visualization features, gathered CSV and GeoJSON data, studied and implemented GeoPandas, and worked on displaying spatial data.
  
- **William Jacob**  
  - Role: Debugged synthetic data issues, fixed errors in data generation, and created `main.py` for OpenAI integration.

- **Bryan**  
  - Role: [Specify Bryan's role and contributions here.]

- **Benjamin**  
  - Role: Conducted research on data lakes and assisted in gathering GeoJSON files.

- **Gabriel**  
  - Role: Worked on data synthesization and generation processes.

---

## Additional Notes
### Limitations:
- The cost of API keys adds financial constraints to the application's scalability.
- IBM Watson integration was attempted but faced issues, preventing its successful implementation.
- Currently, the data is limited to Singapore, which restricts its applicability to other regions.
- Some data is hardcoded, reducing flexibility and adaptability.

### Future Improvements:
- Expand data coverage to include other countries and regions.
- Enhance the agent's capabilities to be more specialized and context-aware with the data it processes.
- Resolve issues with Watson integration and explore other robust AI services for additional functionality.
- Transition from hardcoded data to a more dynamic and scalable data pipeline.


## YouTube Link
[Watch the Demo](https://youtu.be/your-video-link)

<!-- ### Video Structure:
1. **Introduction**:
   - Briefly introduce the team and the problem being solved.
2. **Demonstration**:
   - Showcase the working solution, highlighting key features and functionality.

----->




   