import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import InputData, PreditctPipeline

st.title("Medical Cost Prediction")

st.header("Enter the Details Below")

age = st.number_input("Age", min_value=0, max_value=100, value=25)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=0.0, format="%.1f")
sex = st.selectbox("Sex", options=["male", "female"])
smoker = st.selectbox("Smoker", options=["yes", "no"])
region = st.selectbox("Region", options=["northeast", "northwest", "southeast", "southwest"])

# Button to trigger prediction
if st.button("Predict"):
    # Prepare the input data
    data = InputData(
        age=age,
        children=children,
        bmi=bmi,
        sex=sex,
        smoker=smoker,
        region=region,
    )
    
    # Convert input data to DataFrame
    data_df = data.get_data_as_dataFrame()
    st.subheader("Input Data")
    st.write(data_df)

    # Make prediction
    try:
        predict_pipeline = PreditctPipeline()
        predictions = predict_pipeline.predict(data_df)
        st.subheader("Prediction Result")
        st.success(f"Predicted Medical Cost: ${round(predictions[0], 2)}")
    except Exception as e:
        st.error(f"Error occurred during prediction: {e}")
