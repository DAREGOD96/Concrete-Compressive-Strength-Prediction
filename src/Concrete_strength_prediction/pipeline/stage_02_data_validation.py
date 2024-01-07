import sys
from src.Concrete_strength_prediction.components.data_validation import DataValidation
from src.Concrete_strength_prediction.config.configuration import ConfigurationManager
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class DataValidationPipeline:
    def __init__(self) -> None:
        """
        Initialize the DataValidationPipeline.
        """
        pass

    def main(self):
        """
        Main method to execute the data validation pipeline stage.

        1. Initializes the ConfigurationManager.
        2. Retrieves the DataValidationConfig using the ConfigurationManager.
        3. Initializes DataValidation with the DataValidationConfig.
        4. Initiates the data validation process.

        """
        configuration_manager_object = ConfigurationManager()
        get_validation_data_config_object = configuration_manager_object.get_data_validation_config()
        data_validation_config = DataValidation(get_validation_data_config_object)
        data_validation_config.data_validation_config_initiated()

STAGE_NAME = "Data Validation"
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
