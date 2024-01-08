import pandas as pd
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from src.Concrete_strength_prediction.entity.config_entity import DataValidationConfig
from src.Concrete_strength_prediction.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.Concrete_strength_prediction.utils.common import save_object

class ModelTrainer:
    def __init__(self, config: DataValidationConfig):
        """
        Initialize the ModelTrainer.

        Args:
        - config (DataValidationConfig): Configuration object for model training.
        """
        self.config = config

    def evaluate_model(self, X_train, y_train, X_test, y_test, models, param):
        """
        Evaluate multiple models on the given data.

        Args:
        - X_train: Training features.
        - y_train: Training labels.
        - X_test: Testing features.
        - y_test: Testing labels.
        - models: Dictionary of models to evaluate.
        - param: Dictionary of hyperparameter search spaces for each model.

        Returns:
        - List[Dict]: List of dictionaries containing model information, score, and best parameters.
        """
        model_scores = []
        for model_name, model in models.items():
            gs = GridSearchCV(model, param[model_name], cv=3)
            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            model_scores.append({
                'model_name': model_name,
                'score': test_model_score,
                'best_params': gs.best_params_
            })

        for score_info in model_scores:
            logging.info(f"Model: {score_info['model_name']}, R2 Score: {score_info['score']}, Best Params: {score_info['best_params']}")

        return model_scores

    def _model_training(self):
        """
        Train and evaluate models based on the provided configuration.
        """
        train_data_path = self.config.train_data
        test_data_path = self.config.test_data
        train_df = pd.read_csv(train_data_path)
        test_df = pd.read_csv(test_data_path)

        target_column = "concrete_compressive_strength"

        X_train = train_df.drop(columns=[target_column], axis=1)
        y_train = train_df[target_column]

        X_test = test_df.drop(columns=[target_column], axis=1)
        y_test = test_df[target_column]

        models = {
            "AdaBoostRegressor": AdaBoostRegressor(),
            "GradientBoostingRegressor": GradientBoostingRegressor(),
            "RandomForestRegressor": RandomForestRegressor(),
            "LinearRegression": LinearRegression(),
            "KNeighborsRegressor": KNeighborsRegressor(),
            "DecisionTreeRegressor": DecisionTreeRegressor(),
            "XGBRegressor": XGBRegressor(),
            "CatBoostRegressor": CatBoostRegressor()
        }

        param = dict(self.config.params)
        model_scores = self.evaluate_model(X_train, y_train, X_test, y_test, models, param)

        best_model_info = max(model_scores, key=lambda x: x['score'])
        best_model_name = best_model_info['model_name']
        best_model_score = best_model_info['score']
        best_model_params = best_model_info['best_params']

        logging.info(f"Best performing model is {best_model_name} with a score of {best_model_score} and best parameters: {best_model_params}")

        # Save the best-performing model
        save_object(file_path=self.config.best_model_path, obj=models[best_model_name])

        # Make predictions using the best model
        predicted = models[best_model_name].predict(X_test)
        r2_square = r2_score(y_test, predicted)

        # Log the last R2 Score
        logging.info(f"Last R2 Score: {r2_square}")

        return r2_square
