import sys
import os
import yaml
import pickle
from src.Concrete_strength_prediction.logger import logging
from src.Concrete_strength_prediction.exception import CustomException
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")

@ensure_annotations
def save_object(file_path: str,obj, verbose: bool = True):
    """
    Save a Python object to a file using pickle.

    Parameters:
    - file_path (str): The path to the file where the object will be saved.
    - obj : The Python object to be saved.
    - verbose (bool, optional): If True, log information about the created directory. Default is True.

    Raises:
    - CustomException: If an error occurs during the saving process.

    Note:
    - The function creates the necessary directory structure if it doesn't exist.
    - The object is serialized using pickle and saved to the specified file.
    """
    try:
        dir_name = os.path.dirname(file_path) 
        os.makedirs(dir_name, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {dir_name}")
        with open(file_path, "wb") as f:
            pickle.dump(obj, f)

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    """
    Load and return a Python object from the specified file.

    Parameters:
    - file_path (str): The path to the file containing the serialized object.

    Returns:
    - object: The deserialized Python object.

    Raises:
    - CustomException: If there is an error during the loading process.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
        logging.info(f"loading the pickle file {file_obj} was successfull")
    except Exception as e:
        logging.error(f"Error loading object from file: {file_path}. Error: {e}")
        raise CustomException(e, sys)
