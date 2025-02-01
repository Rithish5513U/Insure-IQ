from flask import Flask, request, jsonify
import os
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Trainer

train_path = os.path.join('artifacts', "train.csv")
validation_path = os.path.join('artifacts', "validation_data.csv")
model_path = os.path.join('artifacts', 'model.pkl')

# @app.route('/train', methods = ['GET'])
def train():
    data_transformation = DataTransformation()
    train_data, test_data, preprocessor_path = data_transformation.data_transform(train_path, validation_path)
    
    model = Trainer()
    score = model.train(train_data, test_data)
    
    return jsonify({"Best score": score})
    