import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb


model = joblib.load('crop_yield_model.pkl')
model_columns = joblib.load('model_columns.pkl')


st.set_page_config(page_title="Crop Yield Predictor", page_icon="🌾")
st.title("🌾 Agricultural Crop Yield Predictor")
st.write("Enter the environmental and farming parameters to predict the yield per hectare.")


col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Location & Environment")
    region = st.selectbox("Region", ['North', 'South', 'East', 'West'])
    weather = st.selectbox("Weather Condition", ['Sunny', 'Rainy', 'Cloudy'])
    temp = st.slider("Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0, step=0.1)
    rainfall = st.slider("Rainfall (mm)", min_value=0.0, max_value=2000.0, value=500.0, step=10.0)

with col2:
    st.subheader("🚜 Farm Parameters")
    soil = st.selectbox("Soil Type", ['Loam', 'Sandy', 'Clay', 'Silt', 'Peaty', 'Chalky'])
    crop = st.selectbox("Crop", ['Barley', 'Cotton', 'Maize', 'Rice', 'Soybean', 'Wheat'])
    days = st.number_input("Days to Harvest", min_value=60, max_value=200, value=120)
    fertilizer = st.checkbox("Used Fertilizer?")
    irrigation = st.checkbox("Used Irrigation?")


if st.button("Predict Crop Yield 🚀"):
    
    input_data = {
        'Region': region, 'Soil_Type': soil, 'Crop': crop,
        'Rainfall_mm': rainfall, 'Temperature_Celsius': temp,
        'Fertilizer_Used': int(fertilizer), 'Irrigation_Used': int(irrigation),
        'Weather_Condition': weather, 'Days_to_Harvest': days
    }
    
    
    input_df = pd.DataFrame([input_data])
    
    input_processed = pd.get_dummies(input_df, drop_first=True)
    
    input_processed = input_processed.reindex(columns=model_columns, fill_value=0)
    
    prediction = model.predict(input_processed)[0]
    
    st.success(f"### 🎉 Predicted Yield: {prediction:.2f} tons per hectare")