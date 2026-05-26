import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Flight Delay Predictor",
    page_icon="✈️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("flight_delay_model.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(to right, #eef2ff, #f8fbff);
}

.title {
    font-size: 50px;
    font-weight: 900;
    text-align: center;
    color: #1e1b4b;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    font-size: 18px;
    padding: 12px;
    border-radius: 12px;
}

.stButton>button:hover {
    transform: scale(1.03);
}

.success-box {
    padding: 20px;
    border-radius: 15px;
    background: #dcfce7;
    color: #166534;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}

.fail-box {
    padding: 20px;
    border-radius: 15px;
    background: #fee2e2;
    color: #991b1b;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>✈️ Flight Delay Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered flight delay prediction system</div>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Settings")
show_chart = st.sidebar.checkbox("Show Charts", True)

# ---------------- INPUT UI ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        airline = st.selectbox("Airline", ["IndiGo", "Air India", "SpiceJet", "Vistara"])
        source = st.selectbox("Departure Airport", ["DEL", "BOM", "BLR", "HYD", "MAA"])
        month = st.selectbox("Month", list(range(1, 13)))
        departure_time = st.time_input("Departure Time")

    with col2:
        destination = st.selectbox("Arrival Airport", ["DEL", "BOM", "BLR", "HYD", "MAA"])
        year = st.number_input("Year", 2024, 2035, 2025)
        day = st.number_input("Day", 1, 31, 1)
        day_of_week = st.selectbox(
            "Day of Week",
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        )

    predict = st.button("🚀 Predict Flight Delay")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ENCODING ----------------
airline_map = {"IndiGo":0,"Air India":1,"SpiceJet":2,"Vistara":3}

airport_map = {"DEL":0,"BOM":1,"BLR":2,"HYD":3,"MAA":4}

day_map = {
    "Monday":0,"Tuesday":1,"Wednesday":2,
    "Thursday":3,"Friday":4,"Saturday":5,"Sunday":6
}

dep_hour = departure_time.hour

# ---------------- INPUT ARRAY (FIXED) ----------------
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

# ---------------- PREDICTION ----------------
if predict:

    prediction = model.predict(input_data)[0]

    try:
        probability = model.predict_proba(input_data)[0][1]
    except:
        probability = 0.5

    st.markdown("---")

    if prediction == 1:
        st.markdown("<div class='fail-box'>⚠️ Flight WILL BE DELAYED</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='success-box'>✅ Flight WILL NOT BE DELAYED</div>", unsafe_allow_html=True)

    st.write("Confidence:", round(probability*100, 2), "%")

    # ---------------- CHART ----------------
    if show_chart:
        st.subheader("Prediction Chart")

        fig, ax = plt.subplots()
        ax.pie(
            [probability, 1-probability],
            labels=["Delayed", "On Time"],
            autopct="%1.1f%%",
            colors=["red","green"]
        )
        st.pyplot(fig)
