import streamlit as st
import pandas as pd
import joblib

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="centered"
)

# ======================================
# LOAD MODEL
# ======================================

model = joblib.load("flight_delay_model.pkl")

# ======================================
# TITLE
# ======================================

st.title("✈️ Flight Delay Prediction App")

st.markdown("""
Predict whether a flight will be delayed or not
using Machine Learning.
""")

# ======================================
# SIDEBAR
# ======================================

st.sidebar.header("About Project")

st.sidebar.info("""
Machine Learning Project using:
- Python
- Streamlit
- Pandas
- Scikit-learn
""")

# ======================================
# INPUT SECTION
# ======================================

st.header("Enter Flight Details")

col1, col2 = st.columns(2)

with col1:

    year = st.number_input(
        "Year",
        min_value=2000,
        max_value=2100,
        value=2024
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1
    )

with col2:

    day_of_month = st.number_input(
        "Day of Month",
        min_value=1,
        max_value=31,
        value=1
    )

    day_of_week = st.number_input(
        "Day of Week (1=Mon, 7=Sun)",
        min_value=1,
        max_value=7,
        value=1
    )

# ======================================
# PREDICTION BUTTON
# ======================================

if st.button("Predict Flight Delay"):

    # Create dataframe

    input_data = pd.DataFrame([{
        "year": year,
        "month": month,
        "day_of_month": day_of_month,
        "day_of_week": day_of_week
    }])

    # Show entered data

    st.subheader("Entered Flight Details")

    st.dataframe(input_data)

    # Prediction

    result = model.predict(input_data)[0]

    # ======================================
    # OUTPUT
    # ======================================

    st.subheader("Prediction Result")

    if result == 1:
        st.error("✈️ Flight WILL BE DELAYED")
    else:
        st.success("✈️ Flight will NOT be delayed")

    # ======================================
    # PROBABILITY
    # ======================================

    try:

        probability = model.predict_proba(input_data)[0][1]

        st.write(
            f"Delay Probability: {probability * 100:.2f}%"
        )

    except:

        st.info("Probability score not available.")

# ======================================
# FOOTER
# ======================================

st.markdown("---")

st.caption("Developed using Streamlit and Machine Learning")