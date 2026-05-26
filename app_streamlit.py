import streamlit as st

st.set_page_config(page_title="Flight Delay Predictor", page_icon="✈️", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #eef2ff, #f8fbff);
}

.title {
    font-size: 52px;
    font-weight: 800;
    color: #1f2937;
}

.subtitle {
    font-size: 20px;
    color: #6b7280;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.75);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(31,38,135,0.1);
    backdrop-filter: blur(8px);
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #4338ca, #6d28d9);
}

.result-success {
    background: #dcfce7;
    padding: 20px;
    border-radius: 15px;
    color: #166534;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

.result-danger {
    background: #fee2e2;
    padding: 20px;
    border-radius: 15px;
    color: #991b1b;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">✈️ Flight Delay Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict whether your flight will be delayed</div>', unsafe_allow_html=True)

# ---------- FORM ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Year", 2020, 2030, 2024)
        month = st.selectbox("Month", list(range(1,13)))

    with col2:
        day = st.number_input("Day", 1, 31, 1)
        day_of_week = st.selectbox(
            "Day of Week",
            ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]
        )

    predict = st.button("🚀 Predict Flight Status")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RESULT ----------
if predict:

    # Dummy prediction
    delayed = False

    if delayed:
        st.markdown(
            '<div class="result-danger">⚠️ Flight WILL be delayed</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-success">✅ Flight will NOT be delayed</div>',
            unsafe_allow_html=True
        )