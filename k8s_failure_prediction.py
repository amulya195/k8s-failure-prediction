import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from fastapi import FastAPI
import uvicorn

# Check if model.pkl exists
MODEL_PATH = "models/model.pkl"
if os.path.exists(MODEL_PATH):
    print("Loading existing model...")
    model = joblib.load(MODEL_PATH)
else:
    print("Training new model...")
    # Step 1: Simulating Kubernetes Metrics Data
    def generate_k8s_metrics(num_samples=1000):
        np.random.seed(42)
        data = {
            "timestamp": pd.date_range(start="2024-01-01", periods=num_samples, freq="H"),
            "cpu_usage": np.random.normal(50, 10, num_samples),
            "memory_usage": np.random.normal(60, 15, num_samples),
            "disk_io": np.random.normal(30, 5, num_samples),
            "network_io": np.random.normal(20, 3, num_samples),
            "pod_status": np.random.choice([0, 1], num_samples, p=[0.95, 0.05])  # 1 means failure
        }
        df = pd.DataFrame(data)
        return df

    data = generate_k8s_metrics()

    # Step 2: Preprocessing & Feature Engineering
    def preprocess_data(df):
        df = df.drop(columns=["timestamp"])  # Drop timestamp for model simplicity
        return df

    data_processed = preprocess_data(data)
    X = data_processed.drop(columns=["pod_status"])
    y = data_processed["pod_status"]

    # Step 3: Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: Model Training (Anomaly Detection using Isolation Forest)
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X_train)
    
    # Save trained model
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved to models/model.pkl")

# Step 6: Deploying the Model via FastAPI
app = FastAPI()

@app.post("/predict/")
def predict_failure(cpu_usage: float, memory_usage: float, disk_io: float, network_io: float):
    input_data = np.array([[cpu_usage, memory_usage, disk_io, network_io]])
    prediction = model.predict(input_data)
    return {"failure": bool(prediction[0] == -1)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)