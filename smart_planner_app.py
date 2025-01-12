import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.express as px
import geopandas as gpd
from map_column_dict import column_mapping
from agents.synthetic_data_agent import generate_synthetic_data_code
from agents.comparative_analysis_agent import generate_comparative_analysis
from bs4 import BeautifulSoup

# ----- PAGE CONFIG & STYLES -----
st.set_page_config(
    page_title="SMART City Planner Insights App", page_icon="🌆", layout="wide"
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
    unsafe_allow_html=True,
)


def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio(
        "Go to",
        [
            "Dashboard",
            "Exploratory Data Insights",
            "Map Visualization",
            "Comparative Analysis",
            "Synthetic Generation",
        ],
    )

    st.sidebar.markdown("---")
    st.sidebar.write("**User:** John Doe")
    st.sidebar.write("**Version:** 0.0.1")
    if st.sidebar.button("Logout"):
        st.sidebar.write("You have logged out.")

    st.title("Smart City Insights App")
    st.markdown(
        """
        Welcome to the **SMART City Insights** application, an intelligent generative AI advisor 
        designed to help you explore multimodal datasets for **demographic, transportation, economic, environment, social, land use, meteorological and geospatial** factors.

        Please be aware that these insights may occasionally contain inaccuracies.
        It is essential to verify any critical information independently and consult authoritative sources 
        before making decisions based on the generated content. Your diligence in double-checking facts is highly encouraged.
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

    elif selected_page == "Synthetic Generation":
        synthetic_generation_page()


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
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
        st.line_chart(chart_data)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Model Training")
            bar_data = pd.DataFrame(
                np.random.randn(20, 2), columns=["Train", "Validation"]
            )
            st.bar_chart(bar_data)

        with col2:
            st.markdown("### Data Annotation")
            area_data = pd.DataFrame(
                np.random.randn(20, 2), columns=["Label1", "Label2"]
            )
            st.area_chart(area_data)

    st.info("Navigate using the sidebar to explore other features.")


def query_ai_agent_page():
    st.subheader("Ask the Smart Agent")
    st.write(
        """
        Input your query related to **demographic, transportation, economic, environment, or social** issues, 
        and let the agent automatically collect and consolidate old and new information from your prorietary data lakehouse.
        """
    )
    user_query = st.text_input(
        "What would you like to find out?",
        value="What are the key transportation challenges the city is facing?",
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

    # map the name to proper name in st
    mapping_df = pd.DataFrame.from_dict(column_mapping, orient='index')

    # select only the columns that are after Multigenerational housing
    mapping_df = mapping_df.iloc[9:]
    # Create a toggleable section for documentation
    with st.expander("See Column Specifications"):
        st.write(mapping_df)

    try:

        @st.cache_data
        def load_data():
            # Load the GeoDataFrame
            gdf = gpd.read_file("data/gdf.geojson")
            gdf["longitude"] = gdf.geometry.centroid.x
            gdf["latitude"] = gdf.geometry.centroid.y

            # Rename columns based on column_mapping
            # rename_dict = {col: column_mapping[col]['name'] for col in gdf.columns if col in column_mapping}
            # gdf_renamed = gdf.rename(columns=rename_dict, inplace=False)

            return gdf
        
        
        def parse_description(description):
            soup = BeautifulSoup(description, 'html.parser')
            data = {}
            
            # Find all table rows within the table
            for row in soup.find_all('tr'):
                # Find all cells in the row
                cells = row.find_all(['th', 'td'])  # Include both th and td
                if len(cells) == 2:  # Ensure the row has exactly 2 cells
                    key = cells[0].text.strip()  # First cell is the key
                    value = cells[1].text.strip()  # Second cell is the value
                    data[key] = value
            
            return data

        @st.cache_data
        def load_dwellings_data():
            dwellings = gpd.read_file("data/dwellings.geojson")
            # Apply the parsing function to the 'Description' column
            dwellings_data = dwellings['Description'].apply(parse_description)

            # Convert the parsed data to a DataFrame and concatenate with the original GeoDataFrame
            dwellings_df = pd.DataFrame(dwellings_data.tolist())
            dwellings = pd.concat([dwellings, dwellings_df], axis=1)
            dwellings = dwellings.drop(columns=['Description'])
            return dwellings[:10000]

        with st.spinner("Loading data..."):
            gdf = load_data()
            dwellings = load_dwellings_data()
            geojson_data = gdf.__geo_interface__

        numeric_columns = gdf.select_dtypes(include=[np.number]).columns
        numeric_columns = numeric_columns.drop(["longitude", "latitude"])
        filter_option = st.selectbox("Select Filter", numeric_columns, index=0, format_func=lambda x: f"{x}")
        selected_column = filter_option
        selected_column_name = column_mapping[selected_column]["name"]
        selected_column_desc = column_mapping[selected_column]["description"]

        # Map style selection
        map_style = st.sidebar.selectbox(
            "Select Map Style",
            options=["carto-positron", "carto-darkmatter", "open-street-map"],
        )

        # st.markdown(f"Display Name: **{selected_column}**")
        # st.markdown(f"### Data: **{selected_column_name}**")
        st.markdown(
                f"""
                <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                    <h4 style="color: #333;">Description:</h4>
                    <p>{selected_column_desc}</p>
                </div>
                """,
                unsafe_allow_html=True
        )
        fig = px.choropleth_mapbox(
            gdf,
            geojson=geojson_data,
            locations=gdf.index,  # Use index to match geometry
            color=selected_column,
            hover_name="PLN_AREA_N",
            hover_data=[selected_column],
            title=f"{selected_column_name} Heatmap Data by Location",
            mapbox_style=map_style,
            center={
                "lat": gdf.geometry.centroid.y.mean(),
                "lon": gdf.geometry.centroid.x.mean(),
            },
        )

        st.plotly_chart(fig, use_container_width=True)

        # If you just want to show the map with pinned centroids

        fig2 = px.scatter_mapbox(
            gdf,
            lat="latitude",
            lon="longitude",
            size=selected_column,
            color=selected_column,
            hover_name="PLN_AREA_N",
            hover_data=[selected_column],
            title=f"{selected_column_name} Scatter Plot Data by Location",
            mapbox_style=map_style,
        )
        # Display the map
        st.plotly_chart(fig2, use_container_width=True)


        fig3 = px.density_mapbox(
            gdf,
            lat="latitude",
            lon="longitude",
            z=selected_column,
            radius=10,
            hover_name="PLN_AREA_N",
            hover_data=[selected_column],
            title=f"{selected_column_name} Density Plot Data by Location",
            mapbox_style=map_style,
        )
        # Display the map
        st.plotly_chart(fig3, use_container_width=True)

        # fig4 = px.line_mapbox(
        #     gdf,
        #     lat="latitude",
        #     lon="longitude",
        #     color=selected_column,
        #     hover_name="Name",
        #     hover_data=["PLN_AREA_N", "REGION_N"],
        #     title=f"{selected_column_name} Line Plot Data by Location",
        #     mapbox_style=map_style,
        # )

        # st.plotly_chart(fig4, use_container_width=True)


        # Display Custom GeoData from dwellings.geojson
        st.subheader("Miscellaneous Data")
        st.write("##### URA Number of Dwellings")
        fig5 = px.scatter_mapbox(
            dwellings,
            lat=dwellings.geometry.centroid.y,
            lon=dwellings.geometry.centroid.x,
            color="PROP_TYPE",  # Color points based on property type
            hover_data=["PROP_TYPE", "DU"],
            title="URA Number of Dwellings by Location with Property Type",
            mapbox_style="carto-positron",
        )

        st.plotly_chart(fig5, use_container_width=True)
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
        value="How do cities like Tokyo address demographic aging?",
    )

    if st.button("Compare with Other Countries"):
        summary = generate_comparative_analysis(compare_query)
        st.markdown("### Comparative Analysis Results")
        st.write(summary)


def synthetic_generation_page():
    st.subheader("Synthetic Generation")
    st.write(
        """
        Want to create new data points that don't exist in the database? 
        Ask the agent to generate **synthetic data** based on the existing data.
        """
    )

    synthetic_query = st.text_input(
        "For example: 'Generate synthetic data for a new city with demographic data'",
        value="Generate synthetic data for Singapore with demographic data to simulate population growth after a year",
    )

    if st.button("Generate Synthetic Data"):
        csv_data = generate_synthetic_data_code(synthetic_query)
        st.markdown("### Synthetic Data")
        st.download_button(
            label="Download synthetic_data.csv",
            data=csv_data,
            file_name="synthetic_data.csv",
            mime="text/csv"
        )


if __name__ == "__main__":
    main()
