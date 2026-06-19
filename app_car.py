import streamlit as st
import numpy as np
import pickle

# 1. Page Configuration Setup
st.set_page_config(
    page_title="Automotive AI Valuation Hub",
    page_icon="🚗",
    layout="centered"
)

# 2. Premium Automotive Theme (Corrected CSS Graphic Injection)
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                          url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
    }
    
    /* Input Fields Styling */
    .stNumberInput div div input {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #fbbf24 !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 8px;
        font-weight: bold;
    }

    /* Clean Dropdown Box Style - Fixes the unreadable text overlap */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(30, 41, 59, 0.9) !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 8px;
    }
    
    /* Dropdown Selected Text Color and Alignment */
    .stSelectbox div[data-baseweb="select"] div {
        color: #fbbf24 !important;
        font-weight: bold !important;
    }
    
    /* Style for dropdown options container popover list */
    ul[role="listbox"] {
        background-color: #1e293b !important;
    }
    
    /* Style for individual items inside dropdown list */
    ul[role="listbox"] li {
        color: #fbbf24 !important;
        background-color: transparent !important;
    }
    ul[role="listbox"] li:hover {
        background-color: #334155 !important;
    }

    label p {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #d97706 0%, #b45309 100%);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 14px 20px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 6px 20px rgba(180, 83, 94, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 15px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%);
        box-shadow: 0 0 25px #f59e0b;
        color: #0f172a;
    }
    .valuation-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        background-color: rgba(30, 41, 59, 0.8);
        border: 2px solid #fbbf24;
        color: #fbbf24;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 Automotive Market AI Valuation Engine")
st.markdown("### Automated Predictive Appraiser using Linear Regression")
st.write("Provide the required vehicle specifications and metric history profile below.")
st.markdown("---")

# 3. Load Saved Model Artifact
try:
    with open('car_price_model.pkl', 'rb') as f_model:
        model = pickle.load(f_model)
except FileNotFoundError:
    st.error("🚨 File Loss Error: 'car_price_model.pkl' could not be found. Please save your model from the notebook first.")
    st.stop()

st.markdown("#### Vehicle Specifications Profile")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Manufacture", min_value=2000, max_value=2026, value=2014, step=1)
    present_price = st.number_input("Original Showroom Price (Present_Price in Lakhs)", min_value=0.1, max_value=100.0, value=5.59, format="%.2f")
    kms_driven = st.number_input("Total Distance Odometer (Kms_Driven)", min_value=100, max_value=500000, value=27000, step=500)
    owner = st.selectbox("Number of Previous Owners (Owner)", options=[0, 1, 3])

with col2:
    fuel_type = st.selectbox("Fuel Infrastructure Variant (Fuel_Type)", options=["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Distribution Retail Channel (Seller_Type)", options=["Dealer", "Individual"])
    transmission = st.selectbox("Powertrain Transmission (Transmission)", options=["Manual", "Automatic"])

# 4. Input Label Mapping Architecture
fuel_mapping = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_mapping = {"Dealer": 0, "Individual": 1}
transmission_mapping = {"Manual": 0, "Automatic": 1}

fuel_encoded = fuel_mapping[fuel_type]
seller_encoded = seller_mapping[seller_type]
transmission_encoded = transmission_mapping[transmission]

# 5. Valuation Execution Matrix
if st.button("CALCULATE MARKET ESTIMATE"):
    features = [year, present_price, kms_driven, fuel_encoded, seller_encoded, transmission_encoded, owner]
    input_array = np.asarray(features).reshape(1, -1)
    prediction = model.predict(input_array)
    estimated_price = prediction[0]
    
    if estimated_price < 0:
        st.markdown(
            f'<div class="valuation-box" style="border-color: #ef4444; color: #ef4444;">'
            f'⚠️ APPRECIATION EVALUATION MARGIN BLANK:<br>'
            f'<span style="font-size: 22px; color: #ffffff;">Vehicle metrics indicate negligible remaining baseline residual value.</span>'
            f'</div>', 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="valuation-box">'
            f'🏷️ ESTIMATED VEHICLE VALUATION:<br>'
            f'<span style="font-size: 36px; color: #ffffff;">{estimated_price:.2f} Lakhs</span>'
            f'</div>', 
            unsafe_allow_html=True
        )
