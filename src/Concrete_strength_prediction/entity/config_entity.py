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