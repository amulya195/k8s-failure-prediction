import joblib
import numpy as np

# Load the trained model
model = joblib.load("models/model.pkl")

def predict_failure(cpu_usage, memory_usage, disk_io, network_io):
    input_data = np.array([[cpu_usage, memory_usage, disk_io, network_io]])
    prediction = model.predict(input_data)
    return {"failure": bool(prediction[0] == -1)}

# Example usage
if _name_ == "_main_":
    sample_input = {"cpu_usage": 80, "memory_usage": 90, "disk_io": 50, "network_io": 30}
    print(predict_failure(**sample_input))