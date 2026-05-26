import streamlit as st
import numpy as np
import joblib

# ---------------- PAGE ----------------
st.set_page_config(page_title="Flight Delay Predictor", page_icon="✈️", layout="wide")

# ---------------- LOAD MODEL ----------------
model = joblib.load("flight_delay_model.pkl")

# ---------------- TITLE ----------------
st.title("✈️ Flight Delay Prediction System")

st.write("Enter real flight details below 👇")

# ---------------- USER INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox("Airline", ["IndiGo", "Air India", "SpiceJet", "Vistara"])
    source = st.selectbox("Departure Airport", ["DEL", "BOM", "BLR", "HYD", "MAA"])
    month = st.selectbox("Month", list(range(1, 13)))
    dep_hour = st.slider("Departure Hour", 0, 23, 10)

with col2:
    destination = st.selectbox("Arrival Airport", ["DEL", "BOM", "BLR", "HYD", "MAA"])
    year = st.number_input("Year", 2024, 2035, 2025)
    day = st.number_input("Day", 1, 31, 1)
    day_of_week = st.selectbox(
        "Day of Week",
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    )

# ---------------- ENCODING ----------------
airline_map = {"IndiGo":0, "Air India":1, "SpiceJet":2, "Vistara":3}
airport_map = {"DEL":0, "BOM":1, "BLR":2, "HYD":3, "MAA":4}
day_map = {
    "Monday":0,"Tuesday":1,"Wednesday":2,
    "Thursday":3,"Friday":4,"Saturday":5,"Sunday":6
}

# ---------------- PREDICT BUTTON ----------------
if st.button("🚀 Predict Flight Delay"):

    # REAL USER INPUT USED HERE (NO RANDOM VALUES)
    input_data = np.array([[
        year,
        month,
        day,
        day_map[day_of_week],
        airline_map[airline],
        airport_map[source],
        airport_map[destination],
        dep_hour
    ]])

    prediction = model.predict(input_data)[0]

    try:
        probability = model.predict_proba(input_data)[0][1]
    except:
        probability = 0.5

    st.markdown("---")

    if prediction == 1:
        st.error("⚠️ Flight WILL BE DELAYED")
    else:
        st.success("✅ Flight WILL NOT BE DELAYED")

    st.write("Confidence:", round(probability * 100, 2), "%")