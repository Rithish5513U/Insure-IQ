from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from src.components.data_ingestion import DataIngestion
from run import app
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/upload', methods = ['POST'])
def upload():
    """
    Endpoint to upload the csv file for data ingestion
    """
    if 'file' not in request.files:
        return jsonify({"Error": "No file has been inserted"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"Error": "No name for the inserted file"}), 400
    
    if file and file.filename.endswith('.csv'):
        try:
            file_name = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            file.save(file_path)
            
            data_ingestion = DataIngestion()
            train_path, validation_path = data_ingestion.ingest(file_path)
            
            return jsonify({
                "message" : "Successfully ingested data",
                "train_data_path" : train_path,
                "validation_data_path" : validation_path
            }), 200
            
        except Exception as e:
            return jsonify({"Error": f"An error occurred: {str(e)}"}), 500
    else:
        return jsonify({"Error": "Only csv files are allowed"})
