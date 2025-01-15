import numpy as np
import pandas as pd
import streamlit as st

from src.pipeline.prediction_pipeline import InputData, PreditctPipeline

st.title("Medical Cost Prediction")

st.sidebar.header("Input features")
age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
children = st.sidebar.number_input("Children", min_value=0, max_value=10, value=0)
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0, format="%.1f")
sex = st.sidebar.selectbox("Sex", options=["male", "female"])
smoker = st.sidebar.selectbox("Smoker", options=["yes", "no"])
region = st.sidebar.selectbox("Region", options=["northeast", "northwest", "southeast", "southwest"])

if st.sidebar.button("Predict"):
    # Prepare the input data
    data = InputData(
        age=age,
        children=children,
        bmi=bmi,
        sex=sex,
        smoker=smoker,
        region=region,
    )
    
    data_df = data.get_data_as_dataFrame()
    st.write("Input Data:", data_df)

    # Load the prediction pipeline and make a prediction
    try:
        predict_pipeline = PreditctPipeline()
        predictions = predict_pipeline.predict(data_df)
        st.success(f"Predicted Medical Cost: ${round(predictions[0], 2)}")
    except Exception as e:
        st.error(f"Error occurred during prediction: {e}")