import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np

# ----- PAGE CONFIG & STYLES -----
st.set_page_config(
    page_title="Smart City Planner Insights App",
    page_icon="🌆",
    layout="wide"
)

# Inject a bit of CSS to style metric cards, titles, etc.
st.markdown(
    """
    <style>
    .stContainer {
        background-color: #F9F9F9;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #fff;
        border-radius: 6px;
        padding: 10px 15px;
        text-align: center;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    /* Sidebar style tweaks */
    section[data-testid="stSidebar"] {
        background-color: #F0F4F8;
    }
    section[data-testid="stSidebar"] .css-1d391kg {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Exploratory Data Insights", "Map Visualization", "Comparative Analysis"]
    )

    st.sidebar.markdown("---")
    st.sidebar.write("**User:** John Doe")
    st.sidebar.write("**Version:** 0.0.1")
    if st.sidebar.button("Logout"):
        st.sidebar.write("You have logged out.")

    st.title("Smart City Insights App")
    st.markdown(
        """
        Welcome to the **Smart City Insights** application, an intelligent generative AI advisor 
        designed to help you explore multimodal datasets for **demographic, transportation, economic, environment, and social** factors.
        """
    )

    if selected_page == "Dashboard":
        dashboard_page()

    elif selected_page == "Exploratory Data Insights":
        query_ai_agent_page()

    elif selected_page == "Map Visualization":
        map_visualization_page()

    elif selected_page == "Comparative Analysis":
        comparative_analysis_page()


def dashboard_page():
    st.markdown("### Key Stats")
    col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)
    with col_m1:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.metric(label="Documents", value="10.5K", delta="↑125")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_m2:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.metric(label="Annotations", value="510", delta="↓2")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_m3:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.metric(label="Accuracy", value="87.9%", delta="↑0.1%")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_m4:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.metric(label="Training Time", value="1.5 hours", delta="↑10 mins")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_m5:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.metric(label="Processing Time", value="3 seconds", delta="↓0.1s")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")    


    st.subheader("Overview")
    st.write(
        """
        **Becoming a smart city is vital** for attracting business, residents, tourists, and talent. 
        This application helps city leaders and planners create a roadmap using AI-driven insights 
        based on **demographic, transportation, economic, environment**, and **social** data.
        """
    )

    with st.container():
        st.markdown("### Data Extraction")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        st.line_chart(chart_data)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Model Training")
            bar_data = pd.DataFrame(
                np.random.randn(20, 2),
                columns=['Train', 'Validation']
            )
            st.bar_chart(bar_data)

        with col2:
            st.markdown("### Data Annotation")
            area_data = pd.DataFrame(
                np.random.randn(20, 2),
                columns=['Label1', 'Label2']
            )
            st.area_chart(area_data)

    st.info("Navigate using the sidebar to explore other features.")


def query_ai_agent_page():
    st.subheader("Ask the Smart Agent")
    st.write(
        """
        Input your query related to **demographic, transportation, economic, environment, or social** issues, 
        and let the agent automatically collect and consolidate information from the vector database.
        """
    )
    user_query = st.text_input(
        "What would you like to find out?",
        value="What are the key transportation challenges the city is facing?"
    )
    
    if st.button("Get Insight Report"):
        st.markdown("### Insight Report")
        # Placeholder text
        st.write("Here is where your AI-generated insight report would appear.")
        # Optionally display some “calls” or “steps” if you want to mimic an agent’s chain-of-thought (in a user-friendly format).


def map_visualization_page():
    st.subheader("Map Visualization")
    st.write(
        """
        Below is an interactive map (for demonstration) of Singapore. 
        Select different **filters** to visualize them on the map.
        """
    )
    filter_option = st.selectbox(
        "Select a filter to visualize:",
        ["Population Density", "Median Income", "CO2 Emissions"]
    )

    try:
        gdf = gpd.read_file("data/new_gdf.geojson")
        st.write(f"**Displaying {filter_option} on the map:**")
        # If you just want to show the map with pinned centroids
        st.map(gdf.set_geometry("geometry").centroid)
    except Exception as e:
        st.warning(
            f"Could not load or display GeoData. Check your file path or data format.\n\nError: {e}"
        )


def comparative_analysis_page():
    st.subheader("Comparative Analysis")
    st.write(
        """
        Wondering how other cities or countries tackle similar problems? 
        Ask the agent to pull **external data or case studies** from the web.
        """
    )

    compare_query = st.text_input(
        "For example: 'How do cities like Tokyo address demographic aging?'",
        value="How do cities like Tokyo address demographic aging?"
    )
    
    if st.button("Compare with Other Countries"):
        st.markdown("### Comparative Analysis Results")
        st.write("[Placeholder for AI-generated comparative analysis]")


if __name__ == "__main__":
    main()
