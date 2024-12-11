import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import *
from scripts.load import *
from config import *
from logs import logger


# maktab tabdirlar etl
maktab_tadbirlar_data = None
try:
    maktab_tadbirlar_data = maktab_tadbirlar_extract(maktab_tadbirlar)
    logger.info(f"[maktab tadbirlar] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [maktab tadbirlar] data: {e}")

if  not maktab_tadbirlar_data.empty:
    try:
        maktab_tadbirlar_load(maktab_tadbirlar_data)
        logger.info(f"[maktab tadbirlar] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [maktab tadbirlar] data: {e}")

