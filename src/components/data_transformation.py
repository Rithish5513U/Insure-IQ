import sys
import os
import numpy as np
import pandas as pd 
from dataclasses import dataclass

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_object(self):
        try:
            numerical_features = ['age', 'bmi', 'children']
            categorical_features = ['sex', 'smoker', 'region']

            num_pipeline = Pipeline(
                steps = [
                    ("Imputer", SimpleImputer(strategy="median")),
                    ("Scaler", StandardScaler(with_mean=False))
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("Imputer", SimpleImputer(strategy="most_frequent")),
                    ("OneHotEncoder", OneHotEncoder()),
                    ("Scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info("Object creation for cleaning done...")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_features),
                    ("cat_pipeline", cat_pipeline, categorical_features)
                ],
                remainder="passthrough"
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def data_transform(self, train_path, valid_path):
        try:
            train_df = pd.read_csv(train_path)
            valid_df = pd.read_csv(valid_path)

            logging.info("Loaded train and test dataset")
            logging.info("Obtaining preprocessor object")

            obj = self.get_object()

            target_column_name = 'charges'

            x_train = train_df.drop(columns=[target_column_name], axis=1)
            y_train = train_df[target_column_name]

            x_test = valid_df.drop(columns=[target_column_name], axis=1)
            y_test = valid_df[target_column_name]

            logging.info("Applying preprocessor object on training and testing dataframe")

            train_features = obj.fit_transform(x_train)
            test_features = obj.transform(x_test)

            train_data = np.c_[train_features, np.array(y_train)]
            test_data = np.c_[test_features, np.array(y_test)]

            save_object(
                file_path = self.config.preprocessor_path,
                obj = obj
            )

            logging.info("Saved Preprocessing object successfully")

            return (
                train_data,
                test_data,
                self.config.preprocessor_path
            )

        except Exception as e:
            raise CustomException(e,sys)