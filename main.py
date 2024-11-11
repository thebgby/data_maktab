import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import pnl_extract, maktab_royxat_extract
from scripts.load import pnl_load, maktab_royxat_load
from config import pnl, maktab_royxat
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

# maktab royxat list (months)  etl
maktab_royxat_months_data = None
try:
    maktab_royxat_months_data = maktab_royxat_extract(maktab_royxat)
    logger.info(f"[maktab royxat] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [maktab royxat] data: {e}")

if maktab_royxat_months_data:
    try:
        maktab_royxat_load(maktab_royxat_months_data)
        logger.info(f"[maktab royxat] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [maktab royxat] data: {e}")
