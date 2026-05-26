import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="centered"
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("flight_delay_model.pkl")

# =========================
# TITLE
# =========================
st.title("✈️ Flight Delay Prediction App")

st.markdown("Predict whether a flight will be delayed or not")

# =========================
# INPUT
# =========================
st.header("Enter Flight Details")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", 2000, 2100, 2024)
    month = st.number_input("Month", 1, 12, 1)

with col2:
    day_of_month = st.number_input("Day", 1, 31, 1)
    day_of_week = st.number_input("Day of Week", 1, 7, 1)

# =========================
# PREDICTION
# =========================
if st.button("Predict"):

    input_data = pd.DataFrame([[
        year, month, day_of_month, day_of_week
    ]], columns=["year", "month", "day_of_month", "day_of_week"])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("✈️ Flight WILL BE DELAYED")
    else:
        st.success("✈️ Flight will NOT be delayed")