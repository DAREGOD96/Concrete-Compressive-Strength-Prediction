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