 k8s-failure-prediction
AI model for predicting failures in kubernetes clusters
 Kubernetes Failure Prediction using Machine Learning

 Overview
This project predicts Kubernetes failures based on real-time resource usage metrics.  
It uses *Machine Learning (Isolation Forest)* and provides predictions via a *FastAPI REST API*.

 📂 Project Structure
 k8s-failure-prediction/ 📁 src/ # Source code (FastAPI, ML model) 📁 models/ # Trained model (model.pkl) 📁 data/ # Dataset (k8s_metrics.csv) 📁 docs/ # Documentation (API guide, setup) 📁 presentation/ # Slides  📄 requirements.txt # Dependencies 📄 README.md # Project Overview

Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/YOUR_USERNAME/k8s-failure-prediction.git
cd k8s-failure-prediction 

Step 2: Create a Virtual Environment
python -m venv k8s-env
k8s-env\Scripts\activate  # Windows
source k8s-env/bin/activate  # Mac/Linux

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the FastAPI Server
python src/k8s_failure_prediction.py

Step 5: Test the API
Open: http://127.0.0.1:8000/docs

Test the /predict/ endpoint.