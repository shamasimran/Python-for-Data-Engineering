"""
11_logging_and_monitoring.py

This script demonstrates how to use Python's built-in logging module for:
- Logging messages of different severity levels
- Creating a custom logger
- Writing logs to both console and file
- Rotating log files automatically
- Simulating a simple ETL process with logging

In data engineering, logging is essential for:
- Tracking ETL pipeline execution
- Monitoring errors and performance
- Troubleshooting production issues
"""

import logging
from logging.handlers import RotatingFileHandler
import time


# STEP 1: Configure the logger
logger = logging.getLogger("etl_logger")
logger.setLevel(logging.DEBUG)  # Capture all levels: DEBUG -> CRITICAL


# STEP 2: Create log formatters and handlers
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Console Handler → prints logs to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Only show INFO and above in console
console_handler.setFormatter(formatter)

# File Handler → saves logs to file (rotating handler keeps file size small)
file_handler = RotatingFileHandler(
    "etl_process.log", maxBytes=1024 * 5, backupCount=3  # 5KB max, keep 3 old logs
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# STEP 3: Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# STEP 4: Example - Simple ETL Process Simulation
def extract_data():
    """Simulate data extraction from a source."""
    logger.info("Starting data extraction...")
    time.sleep(1)
    data = ["John", "Sara", "Ali", "Fatima"]
    logger.debug(f"Extracted raw data: {data}")
    return data


def transform_data(data):
    """Simulate data transformation."""
    logger.info("Transforming data...")
    time.sleep(1)
    try:
        transformed = [name.upper() for name in data]
        logger.debug(f"Transformed data: {transformed}")
        return transformed
    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        raise


def load_data(data):
    """Simulate data loading into a target system."""
    logger.info("Loading data to target...")
    time.sleep(1)
    logger.info(f"Successfully loaded {len(data)} records.")


def etl_pipeline():
    """Run a mock ETL pipeline."""
    logger.info("===== ETL Pipeline Started =====")
    try:
        raw_data = extract_data()
        transformed_data = transform_data(raw_data)
        load_data(transformed_data)
        logger.info("===== ETL Pipeline Completed Successfully =====")
    except Exception as e:
        logger.critical(f"ETL pipeline failed: {e}", exc_info=True)


# STEP 5: Run the ETL pipeline
if __name__ == "__main__":
    etl_pipeline()
