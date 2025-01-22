import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import logging
import pandas as pd

class AdvancedVisualizationTools:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    @staticmethod
    def plot_trend(data, x_column, y_column, title="Trend Analysis", save_path=None):
        """
        Plot a trend line with markers.
        """
        logging.info("Plotting trend analysis...")
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x=x_column, y=y_column, marker="o")
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        if save_path:
            plt.savefig(save_path)
            logging.info(f"Plot saved to {save_path}")
        plt.show()

    @staticmethod
    def plot_comparative_bar(data, category_column, value_column, title="Comparative Bar Chart", save_path=None):
        """
        Plot a bar chart for comparative analysis.
        """
        logging.info("Plotting comparative bar chart...")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x=category_column, y=value_column)
        plt.title(title)
        plt.xlabel(category_column)
        plt.ylabel(value_column)
        if save_path:
            plt.savefig(save_path)
            logging.info(f"Plot saved to {save_path}")
        plt.show()

    @staticmethod
    def plot_map(geojson_file, column=None, cmap="viridis", title="Geospatial Visualization"):
        """
        Plot a geospatial visualization.
        """
        logging.info("Plotting geospatial visualization...")
        gdf = gpd.read_file(geojson_file)
        gdf.plot(column=column, cmap=cmap, legend=True, figsize=(12, 8))
        plt.title(title)
        plt.show()

# Example usage
if __name__ == "__main__":
    trend_data = pd.DataFrame({
        "Year": [2010, 2015, 2020, 2025],
        "Population": [500000, 600000, 700000, 800000]
    })
    AdvancedVisualizationTools.plot_trend(trend_data, "Year", "Population")

    bar_data = pd.DataFrame({
        "Country": ["Country A", "Country B", "Country C"],
        "GDP Growth": [2.5, 3.0, 4.5]
    })
    AdvancedVisualizationTools.plot_comparative_bar(bar_data, "Country", "GDP Growth")

    AdvancedVisualizationTools.plot_map("data/SupermarketsGEOJSON.geojson", title="Supermarkets Distribution")