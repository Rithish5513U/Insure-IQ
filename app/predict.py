from flask import request, jsonify
from src.pipeline.prediction_pipeline import PreditctPipeline
import pandas as pd

REQUIRED_COLUMNS = ['age','sex','bmi','children','smoker','region']

def predict():
    """
    Endpoint to predict using the uploaded CSV file.
    """
    try:
        if 'pred_file' not in request.files:
            return jsonify({"Error": "No file uploaded"}), 400

        file = request.files['pred_file']

        if file.filename == '':
            return jsonify({"Error": "No file selected"}), 400

        if not file.filename.endswith('.csv'):
            return jsonify({"Error": "Only CSV files are allowed"}), 400

        input_data = pd.read_csv(file)
        
        missing_columns = [col for col in REQUIRED_COLUMNS if col not in input_data.columns]
        if missing_columns:
            return jsonify({
                "Error": "Required columns are missing",
                "Missing columns": missing_columns,
            }), 400
            
        input_data = input_data[REQUIRED_COLUMNS]

        if input_data.empty:
            return jsonify({"Error": "Uploaded file is empty"}), 400

        pipeline = PreditctPipeline()
        predictions, features = pipeline.predict(features=input_data)

        return jsonify({
            "message": "Prediction successful",
            "input_params": features.to_dict(),
            "predictions": predictions.tolist()
        }), 200

    except Exception as e:
        return jsonify({"Error": f"An error occurred: {str(e)}"}), 500
