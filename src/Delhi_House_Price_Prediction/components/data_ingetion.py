import os
import sys
import pandas as pd
from src.logs.logger import logging
from src.Delhi_House_Price_Prediction.exceptions import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifact',"train_data.csv")
    test_data_path = os.path.join('artifact',"test_data.csv")
    raw_data_path = os.path.join('artifact',"raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def data_ingestion_start(self):
        try:
            logging.info("Data Reading started.")
            data = pd.read_csv("Data\delhi_house.csv")
            logging.info("Data reading completed and data dir creating Started.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info("Data dir creation completed and raw data conveting Started.")
            data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("raw data creation completed and splitting data started.")
            from sklearn.model_selection import train_test_split
            train_data,test_data = train_test_split(data,test_size=0.25,random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
    
            logging.info("Data spliting completed.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )    
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    DataIngestion().data_ingestion_start()