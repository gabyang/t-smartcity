import pandas as pd
import matplotlib.pyplot as plt

class ComparativeAnalysisAgent:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def plot_comparative_analysis(self, column, countries):
        country_data = self.data[self.data['Country'].isin(countries)]
        country_data.groupby('Country')[column].mean().plot(kind='bar', figsize=(8, 5))
        
        plt.title(f'Comparative Analysis of {column}')
        plt.ylabel(column)
        plt.xlabel('Country')
        plt.show()

# Example usage
agent = ComparativeAnalysisAgent('comparative_data.csv')
agent.plot_comparative_analysis('GDP Growth', ['SG', 'Indonesia', 'China'])