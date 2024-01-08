import sys
from src.Concrete_strength_prediction.components.model_training import ModelTrainer
from src.Concrete_strength_prediction.config.configuration import ConfigurationManager
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class ModelTrainerPipeline:
    def __init__(self) -> None:
        """
        Initialize the ModelTrainerPipeline.
        """
        pass

    def main(self):
        """
        Main method to execute the model training pipeline.
        """
        configuration_manager_object = ConfigurationManager()
        get_model_trainer_config_object = configuration_manager_object.get_model_trainer_config()
        model_trainer_object = ModelTrainer(get_model_trainer_config_object)
        model_trainer_object._model_training()

STAGE_NAME = "Model Training"
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
