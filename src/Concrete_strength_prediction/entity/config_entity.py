from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion.

    Attributes:
    - root_dir (Path): The root directory for data storage.
    - raw_data_path (Path): The path to the raw data.
    """
    root_dir: Path
    raw_data_path: Path


@dataclass
class DataValidationConfig:
    """
    Configuration class for data validation.

    Attributes:
    - root_dir (Path): The root directory for data validation.
    - raw_data_path (Path): The path to the raw data for validation.
    - validation_status (Path): The path to store the validation status.
    - schema (Dict): The schema dictionary specifying the expected structure of the data.
    """
    root_dir: Path
    raw_data_path: Path
    validation_status: Path
    schema: dict


@dataclass
class DataTransformationConfig:
    """
    Configuration class for data transformation.

    Attributes:
    - root_dir (Path): Root directory for data transformation artifacts.
    - raw_data_path (Path): Path to the raw data file from data ingestion.
    - preprocessor (str): Path to the saved preprocessor (ColumnTransformer) object.
    - train_data (Path): Path to the CSV file storing the training data after transformation.
    - test_data (Path): Path to the CSV file storing the test data after transformation.
    - columns_name (Dict): Dictionary containing column names for data transformation.
    - target_columns_name (Dict): Dictionary containing column names for the target variable.
    """

    root_dir: Path
    raw_data_path: Path
    preprocessor: str
    train_data: Path
    test_data: Path
    columns_name: dict
    target_columns_name: dict