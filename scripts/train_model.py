# scripts/train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

def load_data(file_path):
    """Load the dataset."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess data and split into features and target."""
    X = df[['engagement_score', 'experience_score']]
    y = df['satisfaction_score']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and return predictions and MSE."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return y_pred, mse

def log_model(model, X_train, y_pred, mse, X_test):
    """Log the model, metrics, and signature with MLflow."""
    signature = infer_signature(X_train, y_pred)
    input_example = X_test.iloc[:5]
    
    with mlflow.start_run():
        mlflow.log_param("model_type", "Linear Regression")
        mlflow.log_param("test_size", 0.2)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model", signature=signature, input_example=input_example)
    
def main():
    # Load and preprocess the data
    df = load_data('notebooks/user_satisfaction_scores.csv')
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    y_pred, mse = evaluate_model(model, X_test, y_test)
    
    # Log the model and metrics
    log_model(model, X_train, y_pred, mse, X_test)

if __name__ == "__main__":
    main()
