from flask import request, jsonify
from src.pipeline.prediction_pipeline import PreditctPipeline
import os
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# @app.route('/predict', methods=['GET'])
def predict():
    """
    Endpoint to predict using the uploaded CSV file.
    """
    try:
        file_name = request.args.get('file_name')
        
        if not file_name:
            return jsonify({"Error" : "No file name provided"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        
        if not os.path.exists(file_path):
            return jsonify({"Error": "File Not Found"}), 404

        input_data = pd.read_csv(file_path)

        pipeline = PreditctPipeline()

        predictions = pipeline.predict(features=input_data)

        os.remove(file_path)

        return jsonify({
            "message": "Prediction successful",
            "predictions": predictions.tolist()
        }), 200

    except Exception as e:
        return jsonify({"Error": f"An error occurred: {str(e)}"}), 500
