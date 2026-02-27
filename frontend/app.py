import streamlit as st
from backend.model_utils import predict_churn

st.title("🔮 Customer Churn Prediction App")

st.markdown("Enter customer details to predict whether they are likely to churn.")

# Input form
input_data = {
    "gender": st.selectbox("Gender", ["Male", "Female"]),
    "tenure": st.slider("Tenure (months)", 0, 72),
    "MonthlyCharges": st.number_input("Monthly Charges", min_value=0.0),
    "Contract": st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"]),
    "InternetService": st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"]),
    "PaymentMethod": st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
}

model_choice = st.radio("Choose Model", ["Random Forest", "Logistic Regression"])

if st.button("Predict"):
    try:
        model_name = "random_forest" if model_choice == "Random Forest" else "logistic"
        result = predict_churn(input_data, model_name=model_name)

        if result == 1:
            st.error("⚠️ Customer is likely to churn.")
        else:
            st.success("✅ Customer is not likely to churn.")
    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")
