from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import InputData, PreditctPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = InputData(
            age=request.form.get('age'),
            children=request.form.get('children'),
            bmi=request.form.get('bmi'),
            sex=request.form.get('sex'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')
        )
        
        data_df = data.get_data_as_dataFrame()
        print(data_df)
        
        predict_pipeline = PreditctPipeline()
        predictions = predict_pipeline.predict(data_df)
        return render_template('home.html', results=round(predictions[0], 2))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)
