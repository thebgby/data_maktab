import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import *
from scripts.load import *
from config import *
from logs import logger

# pnl etl
# pnl_data = None
# try:
#     pnl_data = pnl_extract(pnl)
#     logger.info(f"PNL data successfully extracted")
# except Exception as e:
#     logger.error(f"error while extracting PNL data: {e}")

# if not pnl_data.empty:
#     try:
#         pnl_load(pnl_data)
#         logger.info(f"PNL data successfully loaded")
#     except Exception as e:
#         logger.error(f"error while loading PNL data: {e}")

# # maktab royxat list (months)  etl
# maktab_royxat_data = None
# try:
#     maktab_royxat_data = maktab_royxat_extract(maktab_royxat)
#     logger.info(f"[maktab royxat] data successfully extracted")
# except Exception as e:
#     logger.error(f"error while extracting [maktab royxat] data: {e}")

# if maktab_royxat_data:
#     try:
#         maktab_royxat_load(maktab_royxat_data)
#         logger.info(f"[maktab royxat] data successfully loaded")
#     except Exception as e:
#         logger.error(f"error while loading [maktab royxat] data: {e}")

# # maktab kassa data etl
# maktab_kassa_data = None
# try:
#     maktab_kassa_data = maktab_kassa_extract(maktab_kassa)
#     logger.info(f"[maktab kassa] data successfully extracted")
# except Exception as e:
#     logger.error(f"error while extracting [maktab kassa] data: {e}")

# if maktab_kassa_data:
#     try:
#         maktab_kassa_load(maktab_kassa_data)
#         logger.info(f"[maktab kassa] data successfully loaded")
#     except Exception as e:
#         logger.error(f"error while loading [maktab kassa] data: {e}")

# stipendiya data etl
stipendiya_data = None
try:
    stipendiya_data = stipendiya_extract(stipendiya)
    logger.info(f"[stipendiya] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [stipendiya] data: {e}")

if not stipendiya_data.empty:
    try:
        stipendiya_load(stipendiya_data)
        logger.info(f"[stipendiya] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [stipendiya] data: {e}")

# maktab_xodimlar data etl
m_xodimlar_data = None
try:
    m_xodimlar_data = maktab_xodimlar_extract(maktab_xodimlar)
    logger.info(f"[maktab xodimlar] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [maktab xodimlar] data: {e}")

if  m_xodimlar_data:
    try:
        maktab_xodimlar_load(m_xodimlar_data)
        logger.info(f"[maktab xodimlar] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [maktab xodimlar] data: {e}")


# maktab_xodimlar data etl
pochemuchkadb_data = None
try:
    pochemuchkadb_data = pochemuchkadb_extract(pochemuchkadb)
    logger.info(f"[pochemuchkadb] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [pochemuchkadb] data: {e}")

if  pochemuchkadb_data:
    try:
        pochemuchkadb_load(pochemuchkadb_data)
        logger.info(f"[pochemuchkadb] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [pochemuchkadb] data: {e}")


# dars jadvali data etl
darsjadval_data = None
try:
    darsjadval_data = darsjadvali_extract(dars_jadvali)
    logger.info(f"[dars jadvali] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [dars jadvali] data: {e}")

if  not darsjadval_data.empty:
    try:
        darsjadvali_load(darsjadval_data)
        logger.info(f"[dars jadvali] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [dars jadvali] data: {e}")

# dars jadvali data etl
psixolog_test_data = None
try:
    psixolog_test_data = psixolog_test_extract(psixolog_test)
    # print(type(psixolog_test_data))
    logger.info(f"[psixolog test] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [psixolog test] data: {e}")

if  psixolog_test_data:
    try:
        psixolog_test_load(psixolog_test_data)
        logger.info(f"[psixolog test] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [psixolog test] data: {e}")

# kutubxona data etl
kutubxona_data = None
try:
    kutubxona_data = kutubxona_extract(kutubxona)
    # print(type(psixolog_test_data))
    logger.info(f"[kutubxona] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [kutubxona] data: {e}")

if  kutubxona_data:
    try:
        kutubxona_load(kutubxona_data)
        logger.info(f"[kutubxona] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [kutubxona] data: {e}")