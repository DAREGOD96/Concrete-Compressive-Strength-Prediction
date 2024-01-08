import sys
from pathlib import Path
from src.Concrete_strength_prediction.config.configuration import ConfigurationManager
from src.Concrete_strength_prediction.components.data_transformation import DataTransformation
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class DataTransformationPipeline:
    def __init__(self) -> None:
        """
        Constructor for DataTransformationPipeline class.
        """
        pass

    def main(self):
        """
        Main method for the data transformation pipeline.

        Reads the status from the data validation process and initiates
        the data transformation process if the validation is successful.

        Raises:
        - Exception: If the data schema is not valid.
        """
        with open(Path("artifacts/data_validation/status.txt"), "r") as f:
            status = f.read().split(" ")[-1]
        
        if status == "True":
            configuration_manager_object = ConfigurationManager()
            get_data_transformation_config_object = configuration_manager_object.get_data_transformation_config()
            data_transformation_object = DataTransformation(get_data_transformation_config_object)
            data_transformation_object.train_test_splitting()
        else:
            raise Exception("Your data schema is not valid")

STAGE_NAME = "Data transformation"
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
