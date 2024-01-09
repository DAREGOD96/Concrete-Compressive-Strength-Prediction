import os
import sys
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException
from src.Concrete_strength_prediction.utils.common import load_object

class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        """
        Predict the concrete compressive strength using a trained model.

        Args:
            features (array-like or pd.DataFrame): Input features for prediction.

        Returns:
            array-like: Predicted concrete compressive strength.
        """
        try:
            model_path = os.path.join("artifacts", "model_training", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "data_transformation", "preprocessor.pkl")

            load_model = load_object(file_path=model_path)
            load_preprocessor = load_object(file_path=preprocessor_path)

            scaled_features = load_preprocessor.transform(features)
            prediction = load_model.predict(scaled_features)

            logging.info("Prediction successful.")
            return prediction

        except Exception as e:
            logging.error(f"Prediction failed: {e}")
            raise CustomException(e, sys)

        

    