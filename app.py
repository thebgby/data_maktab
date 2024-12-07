import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import *
from scripts.load import *
from config import *
from logs import logger


# dars jadvali data etl
nps_data = None
try:
    nps_data = nps_extract(nps)
    logger.info(f"[nps] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [nps] data: {e}")

if  not nps_data.empty:
    try:
        nps_load(nps_data)
        logger.info(f"[nps] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [nps] data: {e}")
