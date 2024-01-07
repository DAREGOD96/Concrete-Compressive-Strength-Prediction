import pandas as pd
import sys
from src.Concrete_strength_prediction.entity.config_entity import DataValidationConfig
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        """
        Initialize DataValidation with a configuration.

        Parameters:
        - config (DataValidationConfig): Configuration for data validation.
        """
        self.config = config

    def data_validation_config_initiated(self):
        """
        Perform data validation based on the provided configuration.

        Reads the raw data, compares columns with the specified schema,
        and writes the validation status to the designated file.

        Returns:
        - bool: Validation status (True if successful, False otherwise).
        """
        try:
            validation_status = None

            df = pd.read_csv(self.config.raw_data_path)
            logging.info("Reading the dataset is successfull")
            all_columns = list(df.columns)
            all_schema = self.config.schema

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    logging.info(f"Validation failed for column: {col}")
                else:
                    validation_status = True
                    logging.info(f"Validation successful for column: {col}")

            # Write the validation status to the designated file
            with open(self.config.validation_status, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logging.info("Data validation completed successfully.")

            return validation_status

        except CustomException as e:
            logging.info(e)
            raise CustomException(e, sys)
