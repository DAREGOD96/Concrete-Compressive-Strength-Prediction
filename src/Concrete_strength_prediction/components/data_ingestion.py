import pandas as pd
import sys
from src.Concrete_strength_prediction.entity.config_entity import DataIngestionConfig
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException
from pathlib import Path
class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        """
        Initialize DataIngestion with a configuration.

        Parameters:
        - config (DataIngestionConfig): Configuration for data ingestion.
        """
        self.config = config

    def initiate_data_ingestion(self):
        """
        Initiate the data ingestion process.

        Reads a CSV file, logs information, and saves the raw dataset to a specified path.
        """
        try:
            dataset_url = Path("dataset/cleaned_dataset.csv")
            df = pd.read_csv(dataset_url)
            logging.info("Reading the dataset as a dataframe done!")
            
            # Save the raw dataset to the specified path
            df.to_csv(self.config.raw_data_path, index=False, header=True)
            logging.info("Saving the raw dataset to artifacts/data_ingestion folder")

        except Exception as e:
            logging.error(e)
            # Raise a CustomException with the original exception and sys module
            raise CustomException(e, sys)