import os
import sys
import pickle
import dill

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, Y_train, X_test, Y_test, models, params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            
            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, Y_train)
            print(param)
            
            best_model = gs.best_estimator_
            best_model_params = gs.best_params_
            
            best_model.set_params(**best_model_params)
            best_model.fit(X_train, Y_train)
            
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)
            
            model_train_score = r2_score(Y_train, y_train_pred)
            model_test_score = r2_score(Y_test, y_test_pred)
            
            report[list(models.keys())[i]] = model_test_score
            
        return report
    
    except Exception as e:
        raise CustomException(e, sys)