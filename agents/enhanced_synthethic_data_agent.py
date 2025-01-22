import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class SyntheticDataAgent:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def predict_future_trends(self, feature_column, target_column):
        X = self.data[[feature_column]]
        y = self.data[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        future = pd.DataFrame({feature_column: range(max(X[feature_column])+1, max(X[feature_column])+6)})
        future['prediction'] = model.predict(future)
        
        plt.figure(figsize=(8, 5))
        plt.scatter(X, y, label="Actual Data")
        plt.plot(future[feature_column], future['prediction'], color='red', label="Prediction")
        plt.xlabel(feature_column)
        plt.ylabel(target_column)
        plt.title("Future Trend Prediction")
        plt.legend()
        plt.show()
        
        return future

agent = SyntheticDataAgent('synthetic_data.csv')
future_trends = agent.predict_future_trends('Year', 'Population')
print(future_trends)