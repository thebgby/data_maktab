import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import *
from scripts.load import *
from config import *
from logs import logger

# new kutubxona
n_kutubxona_data = None
try:
    n_kutubxona_data = n_kutubxona_extract(new_kutubxona)
    logger.info(f"[n_kutubxona] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [n_kutubxona] data: {e}")

if n_kutubxona_data:
    try:
        n_kutubxona_load(n_kutubxona_data)
        logger.info(f"[n_kutubxona] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [n_kutubxona] data: {e}")