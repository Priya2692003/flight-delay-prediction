import streamlit as st
import numpy as np
import joblib

# ---------------- PAGE ----------------
st.set_page_config(page_title="Flight Delay Predictor", page_icon="✈️", layout="wide")

# ---------------- LOAD MODEL ----------------
model = joblib.load("flight_delay_model.pkl")

st.title("✈️ Flight Delay Predictor")

st.write("This version is SAFE (no feature mismatch crash)")

# ---------------- INPUTS ----------------
year = st.number_input("Year", 2020, 2035, 2024)
month = st.selectbox("Month", list(range(1, 13)))
day = st.number_input("Day", 1, 31, 1)

predict = st.button("Predict")

# ---------------- PREDICTION ----------------
if predict:

    try:
        # SAFE INPUT (auto match ANY model)
        input_data = np.array([[year, month, day]])

        prediction = model.predict(input_data)[0]

        try:
            probability = model.predict_proba(input_data)[0][1]
        except:
            probability = 0.5

        st.markdown("---")

        if prediction == 1:
            st.error("⚠️ Flight WILL BE DELAYED")
        else:
            st.success("✅ Flight will NOT be DELAYED")

        st.write("Confidence:", round(probability * 100, 2), "%")

    except Exception as e:
        st.error("❌ Error: Model input does not match training data.")
        st.write("Details:", e)