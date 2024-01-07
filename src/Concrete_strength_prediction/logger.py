import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

# Create 'logs' directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Find the latest subdirectory number
latest_subdir_number = 0
for entry in os.listdir(log_dir):
    if entry.startswith("running logs"):
        try:
            number = int(entry.split()[-1])
            latest_subdir_number = max(latest_subdir_number, number)
        except ValueError:
            pass

# Increment the subdirectory number
latest_subdir_number += 1
subdir_name = f"running logs {latest_subdir_number}"

# Create the full path for the new log directory and log file
log_subdir_path = os.path.join(log_dir, subdir_name)
filepath = os.path.join(log_subdir_path, "logs.log")

# Create the necessary directories
os.makedirs(log_subdir_path, exist_ok=True)

logging.basicConfig(
    format=logging_str,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

"""
Configures logging for the script with the following settings:
- Log messages are formatted with a specific pattern.
- Logs are stored in a 'logs' directory.
- Each run creates a subdirectory named 'running logs N', where N is the latest subdirectory number.
- Log entries are written to both a file ('logs.log') and the standard output.

"""
