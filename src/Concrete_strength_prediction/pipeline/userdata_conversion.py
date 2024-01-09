import pandas as pd
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException

class UserData:
    def __init__(self, cement: float, blast_furnace_slag: float, fly_ash: float,
                 water: float, superplasticizer: float, coarse_aggregate: float,
                 fine_aggregate: float, age: int):
        """
        Class to represent user input data for concrete compressive strength prediction.

        Args:
            cement (float): Amount of cement.
            blast_furnace_slag (float): Amount of blast furnace slag.
            fly_ash (float): Amount of fly ash.
            water (float): Amount of water.
            superplasticizer (float): Amount of superplasticizer.
            coarse_aggregate (float): Amount of coarse aggregate.
            fine_aggregate (float): Amount of fine aggregate.
            age (int): Age of the concrete.

        """
        self.cement = cement
        self.blast_furnace_slag = blast_furnace_slag
        self.fly_ash = fly_ash
        self.water = water
        self.superplasticizer = superplasticizer
        self.coarse_aggregate = coarse_aggregate
        self.fine_aggregate = fine_aggregate
        self.age = age

    def convert_data_into_dataframe(self):
        """
        Convert user input data into a pandas DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing user input data.
        """
        try:
            logging.info("User data received")
            user_data = {
                "cement": [self.cement],
                "blast_furnace_slag": [self.blast_furnace_slag],
                "fly_ash": [self.fly_ash],
                "water": [self.water],
                "superplasticizer": [self.superplasticizer],
                "coarse_aggregate": [self.coarse_aggregate],
                "fine_aggregate": [self.fine_aggregate],
                "age": [self.age]
            }
            logging.info("user data is converted into dataframe fro prediction")
            return pd.DataFrame(user_data)

        except Exception as e:
            logging.error(f"Failed to convert user data into DataFrame: {e}")
            raise CustomException(e)
