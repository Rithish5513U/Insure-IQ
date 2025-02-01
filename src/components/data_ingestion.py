import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Trainer

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw_data.csv")
    validation_data_path: str = os.path.join('artifacts','validation_data.csv')
    
class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
        
    def ingest(self, file_path = 'notebook/data/insurance.csv'):
        logging.info("Data ingestion started...")
        try:
            df = pd.read_csv(file_path)
            
            logging.info('Reading complete...')
            
            df.drop_duplicates(inplace=True)
            
            os.makedirs(os.path.dirname(self.config.train_data_path),exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False, header=True)
            
            logging.info('Train test split...')
            train_set, remaining_set = train_test_split(df, train_size=0.7, random_state=42)
            valid_set, test_set = train_test_split(remaining_set, test_size=0.15, random_state=42)
            
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            valid_set.to_csv(self.config.validation_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            
            logging.info("Data Ingestion complete...")
            
            return (
                self.config.train_data_path,
                self.config.validation_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    di = DataIngestion()
    train_path, validation_path = di.ingest()
    
    # Data Transformation
    dt = DataTransformation()
    train_arr, val_arr, _ = dt.data_transform(train_path, validation_path)
    
    # Model Training
    model_trainer = Trainer()
    r2_score = model_trainer.train(train_arr, val_arr)
    print(r2_score)

