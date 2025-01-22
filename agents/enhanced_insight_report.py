import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class InsightReportAgent:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def generate_insight_report(self, column):
        stats = self.data[column].describe()
        print("Descriptive Statistics:")
        print(stats)
        
        plt.figure(figsize=(8, 5))
        sns.histplot(self.data[column], kde=True, bins=30, color='blue')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
        
        return stats


agent = InsightReportAgent('synthetic_data.csv')
stats = agent.generate_insight_report('Population')
print(stats)