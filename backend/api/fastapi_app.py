# backend/api/fastapi_app.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# Load models and columns
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
random_forest_model = joblib.load(os.path.join(MODEL_DIR, "random_forest_model.pkl"))
logistic_model = joblib.load(os.path.join(MODEL_DIR, "logistic_model.pkl"))
columns_used = joblib.load(os.path.join(MODEL_DIR, "columns_used.pkl"))

# Define request body structure
class CustomerInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Churn prediction API is live."}

@app.post("/predict")
def predict_churn(customer: CustomerInput, model: str = "random_forest"):
    input_data = customer.dict()
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=columns_used, fill_value=0)

    try:
        if model == "logistic":
            prediction = logistic_model.predict(df)
        else:
            prediction = random_forest_model.predict(df)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
