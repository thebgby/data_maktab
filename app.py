import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import *
from scripts.load import *
from config import *
from logs import logger


# dietolog data etl
dietolog_data = None
try:
    dietolog_data = dietolog_extract(dietolog)
    # print(type(psixolog_test_data))
    logger.info(f"[dietolog] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [dietolog] data: {e}")

if  dietolog_data:
    try:
        dietolog_load(dietolog_data)
        logger.info(f"[dietolog] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [dietolog] data: {e}")
