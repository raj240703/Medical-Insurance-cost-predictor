import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# -------------------------
# 🎨 Page Configuration
# -------------------------
st.set_page_config(
    page_title="💰 Insurance Charges Predictor",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------
# 🌈 Custom CSS Styling
# -------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #e0f7fa, #f1f8e9);
        color: #1a1a1a;
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #005f73;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# ⚙️ Load Model (Replace with your model path)
# -------------------------
model = joblib.load("insurance_model.pkl")  # ensure this file exists in same folder

# -------------------------
# 🧾 Sidebar Inputs
# -------------------------
st.sidebar.header("🧍‍♂️ Enter User Details")

age = st.sidebar.slider("Age", 18, 65, 30)
bmi = st.sidebar.slider("BMI (Body Mass Index)", 15.0, 45.0, 25.0)
smoker = st.sidebar.radio("Are you a smoker?", ["No", "Yes"])

# Convert to model input
smoker_yes = 1 if smoker == "Yes" else 0

input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "smoker_yes": [smoker_yes]
})

# -------------------------
# 💡 Prediction
# -------------------------
if st.sidebar.button("🔮 Predict Charges"):
    prediction = model.predict(input_data)[0]
    st.markdown(f"""
        <div style='text-align:center;'>
            <h2>🩺 Estimated Insurance Charges:</h2>
            <h1 style='color:#0077b6;'>${prediction:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<h4 style='text-align:center;'>Enter details on the left and click Predict!</h4>", unsafe_allow_html=True)

# -------------------------
# 📊 Visualizations Section
# -------------------------
st.markdown("## 📈 Insights and Visualization")

# Example random data (optional)
data = pd.DataFrame({
    "age": np.random.randint(18, 65, 100),
    "bmi": np.random.uniform(15, 45, 100),
    "charges": np.random.uniform(2000, 50000, 100)
})

col1, col2 = st.columns(2)

with col1:
    fig1 = px.scatter(
        data, x="age", y="charges",
        color_discrete_sequence=["#0077b6"],
        title="Age vs Charges"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(
        data, x="bmi", y="charges",
        color_discrete_sequence=["#00b4d8"],
        title="BMI vs Charges"
    )
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# 💬 Footer
# -------------------------
st.markdown("""
---
**Built with ❤️ using Streamlit**  
Developer: *Your Name*
""")
