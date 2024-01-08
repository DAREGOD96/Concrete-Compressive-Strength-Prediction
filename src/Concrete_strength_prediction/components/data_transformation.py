import pandas as pd
import os
import numpy as np
import sys
from src.Concrete_strength_prediction.utils.common import save_object
from src.Concrete_strength_prediction.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        """
        Constructor for DataTransformation class.

        Parameters:
        - config (DataTransformationConfig): An instance of DataTransformationConfig containing
          configuration parameters for data transformation.
        """
        self.config = config

    def get_data_transformer_object(self):
        """
        Get the ColumnTransformer object for numerical column preprocessing.

        Returns:
        - ColumnTransformer: Preprocessing pipeline for numerical columns.
        """
        all_schema = list(self.config.columns_name)
        numerical_columns = all_schema[:-1]
        
        numerical_pipeline = Pipeline(
            steps=[
                ("scaler", MinMaxScaler())
            ]
        )
        
        preprocessor = ColumnTransformer(
            transformers=[
                ("num_pipeline", numerical_pipeline, numerical_columns)
            ]
        )
        
        return preprocessor

    def train_test_splitting(self):
        """
        Perform data transformation, train-test splitting, and save transformed datasets.

        Raises:
        - CustomException: If an error occurs during data transformation.
        """
        df = pd.read_csv(self.config.raw_data_path)
        target_column = "concrete_compressive_strength"

        X = df.drop(columns=[target_column], axis=1)
        y = df[target_column]

        logging.info("Splited data into training and test sets")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        logging.info(X_train.shape)
        logging.info(X_test.shape)

        preprocessor_object = self.get_data_transformer_object()

        X_train_arr = preprocessor_object.fit_transform(X_train)
        X_test_arr = preprocessor_object.transform(X_test)

        logging.info("Preprocessing of the numerical columns is done!")

        train_data = np.c_[X_train_arr, np.array(y_train)]
        test_data = np.c_[X_test_arr, np.array(y_test)]

        column_names = list(self.config.columns_name)
        train_df = pd.DataFrame(data=train_data, columns=column_names)
        test_df = pd.DataFrame(data=test_data, columns=column_names)

        train_df.to_csv(os.path.join(self.config.train_data), index=False)
        test_df.to_csv(os.path.join(self.config.test_data), index=False)

        logging.info("X_train, X_test, y_train, y_test are added together")

        save_object(
            file_path=self.config.preprocessor,
            obj=preprocessor_object
        )

        logging.info("Data transformation is done!")

