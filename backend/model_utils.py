import joblib
import pandas as pd
import os

# Define model directory
MODEL_DIR = "backend/models"

# Load trained models and feature column list
try:
    random_forest_model = joblib.load(os.path.join(MODEL_DIR, "random_forest_model.pkl"))
    logistic_model = joblib.load(os.path.join(MODEL_DIR, "logistic_model.pkl"))
    columns_used = joblib.load(os.path.join(MODEL_DIR, "columns_used.pkl"))
except Exception as e:
    raise RuntimeError("❌ Model files could not be loaded. Check file paths.") from e


def predict_churn(input_data, model_name="random_forest"):
    """
    Predicts customer churn using the specified model.
    
    Parameters:
        input_data (dict): Input customer data as key-value pairs
        model_name (str): 'random_forest' or 'logistic'

    Returns:
        int: 0 (Not Churned) or 1 (Churned)
    """
    model = random_forest_model if model_name == "random_forest" else logistic_model

    # Convert input to DataFrame and ensure column order matches training
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=columns_used, fill_value=0)

    try:
        prediction = model.predict(df)
        return int(prediction[0])
    except Exception as e:
        raise ValueError("❌ Prediction failed. Please check input format.") from e
