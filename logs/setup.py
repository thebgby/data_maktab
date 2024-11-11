import logging
import os

# Create and configure logger
logger = logging.getLogger("ETL_Logger")
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'etl_process.log'), mode='a')
console_handler = logging.StreamHandler()

# Define format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
