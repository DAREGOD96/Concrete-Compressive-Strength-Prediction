import sys
from src.Concrete_strength_prediction.components.data_ingestion import DataIngestion
from src.Concrete_strength_prediction.config.configuration import ConfigurationManager
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class DataIngestionPipeline:
    def __init__(self) -> None:
        """
        Initialize the DataIngestionPipeline.
        """
        pass

    def main(self):
        """
        Main method to execute the data ingestion pipeline.
        """
        # Initialize the ConfigurationManager
        configuration_manager_object = ConfigurationManager()

        # Get the DataIngestionConfig using the ConfigurationManager
        get_data_ingestion_config_object = configuration_manager_object.get_data_ingestion_config()

        # Initialize DataIngestion with the DataIngestionConfig
        data_ingestion_config = DataIngestion(get_data_ingestion_config_object)

        # Initiate the data ingestion process
        data_ingestion_config.initiate_data_ingestion()

STAGE_NAME = "Data ingestion pipeline"

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Create an instance of DataIngestionPipeline and run the main method
        obj = DataIngestionPipeline()
        obj.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log exceptions and raise a CustomException
        logging.exception(e)
        raise CustomException(e, sys)
