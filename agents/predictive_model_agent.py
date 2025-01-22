import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import logging
import joblib

class PredictiveModelAgent:
    def __init__(self, data_path, model_save_path="predictive_model.pkl"):
        """
        Initialize the predictive model agent.
        
        Args:
            data_path (str): Path to the dataset.
            model_save_path (str): Path to save the trained model.
        """
        self.data_path = data_path
        self.model_save_path = model_save_path
        self.data = pd.read_csv(data_path)
        self.model = None
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def preprocess_data(self, feature_columns, target_column):
        """
        Split the data into training and test sets.
        """
        logging.info("Preprocessing data for model training...")
        X = self.data[feature_columns]
        y = self.data[target_column]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, feature_columns, target_column, hyperparameter_tuning=False):
        """
        Train a Random Forest model with optional hyperparameter tuning.
        """
        X_train, X_test, y_train, y_test = self.preprocess_data(feature_columns, target_column)
        logging.info("Training the Random Forest Regressor...")

        if hyperparameter_tuning:
            logging.info("Performing hyperparameter tuning...")
            param_grid = {
                "n_estimators": [50, 100, 200],
                "max_depth": [None, 10, 20],
                "min_samples_split": [2, 5, 10]
            }
            grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=3)
            grid_search.fit(X_train, y_train)
            self.model = grid_search.best_estimator_
        else:
            self.model = RandomForestRegressor(random_state=42)
            self.model.fit(X_train, y_train)

        # Save the model
        joblib.dump(self.model, self.model_save_path)
        logging.info(f"Model saved to {self.model_save_path}")

        # Evaluate the model
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        logging.info(f"Model Evaluation - MSE: {mse}, R^2: {r2}")
        return {"mse": mse, "r2": r2}

    def predict(self, input_data):
        """
        Predict outcomes using the trained model.
        """
        if self.model is None:
            logging.error("Model not trained. Please train the model before predicting.")
            return None
        return self.model.predict(input_data)

# Example usage
if __name__ == "__main__":
    agent = AdvancedPredictiveModelAgent("synthetic_data.csv")
    results = agent.train_model(feature_columns=["Year"], target_column="Population", hyperparameter_tuning=True)
    print("Training Results:", results)