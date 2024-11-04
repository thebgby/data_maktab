import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import pnl_extract
from scripts.load import pnl_load
from config import pnl
from logs import logger

# pnl etl
pnl_data = None
try:
    pnl_data = pnl_extract(pnl)
    logger.info(f"PNL data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting PNL data: {e}")

if not pnl_data.empty:
    try:
        pnl_load(pnl_data)
        logger.info(f"PNL data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading PNL data: {e}")
