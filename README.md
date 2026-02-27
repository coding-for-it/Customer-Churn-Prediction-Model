# 📉 Customer Churn Prediction

A machine learning solution to predict if a customer is likely to churn based on behavior and account features.

## 🚀 Tech Stack
- Python
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Docker
  
## 📁 Project Directory Structure
```bash
Customer-Churn-Prediction/
├── data/                  # Raw and processed datasets
│   └── customer_churn.csv
│
├── notebooks/             # Jupyter notebooks for EDA and model pipeline
│   └── churn_pipeline.ipynb
│
├── backend/               # Model and utility scripts
│   ├── model_utils.py
│   └── __init__.py
│
├── database/              # MySQL integration
│   ├── mysql_utils.py
│   └── mysql_setup.sql
│
├── frontend/              # Streamlit web app
│   └── app.py
│
├── .gitignore             # Ignore unnecessary files and folders
├── README.md              # Project overview and instructions
└── requirements.txt       # Python dependencies
```

## 📊 Data Source

The dataset contains features like:

- Customer tenure
- Contract type
- Monthly charges
- Total charges
- Internet service
- Payment method
- Gender, Senior citizen, etc.

---

## 🧠 Model Details

- **Model Used**: Random Forest Classifier
- **Why Random Forest**: Handles both numerical and categorical features well, reduces overfitting, and provides feature importance for interpretability.
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score, Confusion Matrix.

---

## 🧪 How to Run Locally

1. Clone the Repository
```bash
git clone https://github.com/coding-for-it/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```
2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the App
```bash
streamlit run frontend/app.py
```
5. Run the FastAPI server
```bash
uvicorn backend.api.fastapi_app:app --reload
```
