# app.py

import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("credit_fraud.pkl")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction values below to check for fraud.")

# List of features in the dataset
features = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
    'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',
    'normalizedAmount'
]

# Create input sliders for each feature
input_data = []
for feature in features:
    value = st.number_input(f"Enter {feature}", value=0.0, format="%.5f")
    input_data.append(value)

if st.button("Predict"):
    prediction = model.predict([input_data])[0]
    if prediction == 1:
        st.error("⚠️ This transaction is likely **fraudulent**.")
    else:
        st.success("✅ This transaction is **legitimate**.")
