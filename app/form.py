from flask import request, jsonify
from run import app
import pandas as pd
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

def form():
    """
    Handles the form data and converts it to the csv file
    """
    try:
        age = request.form.get('age')
        sex = request.form.get('sex')
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoker = request.form.get('smoker')
        region = request.form.get('region')
        
        if(not age and sex and bmi and children and smoker and region):
            return jsonify({"Error" : "All fields are required"}), 400
        
        data = {
            "age": [age],
            "sex": [sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker],
            "region": [region]
        }
        
        df = pd.DateFrame(data)
        
        path = os.makedirs(UPLOAD_FOLDER, "predict.csv")
        df.to_csv(path, index = False)
        
        return jsonify({
            "message" : "Form data successfully processed",
            "path" : path
        }), 200
        
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {str(e)}"}), 500
        