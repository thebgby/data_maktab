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

# psixolog data etl
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

# nps etl
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


# tugaraklar reytingi etl
tugaraklar_reytingi_data = None
try:
    tugaraklar_reytingi_data = tugaraklar_reytingi_extract(tugaraklar_reytingi)
    logger.info(f"[tugaraklar_reytingi_data] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [tugaraklar_reytingi_data] data: {e}")

if  not tugaraklar_reytingi_data.empty:
    try:
        tugaraklar_reytingi_load(tugaraklar_reytingi_data)
        logger.info(f"[tugaraklar_reytingi_data] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [tugaraklar_reytingi_data] data: {e}")

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

# new pochemuchka
n_pochemuchka_data = None
try:
    n_pochemuchka_data = n_pochemuchka_extract(new_pochemuchka)
    logger.info(f"[n_pochemuchka] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [n_pochemuchka] data: {e}")

if n_pochemuchka_data:
    try:
        n_pochemuchka_load(n_pochemuchka_data)
        logger.info(f"[n_pochemuchka] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [n_pochemuchka] data: {e}")


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

# new kutubxona
shifokor_data = None
try:
    shifokor_data = shifokor_qabul_extract(shifokor_kundalik_qabul)
    logger.info(f"[shifokor qabul] data successfully extracted")
except Exception as e:
    logger.error(f"error while extracting [shifokor_qabul] data: {e}")

if not shifokor_data.empty:
    try:
        shifokor_qabul_load(shifokor_data)
        logger.info(f"[shifokor_qabul] data successfully loaded")
    except Exception as e:
        logger.error(f"error while loading [shifokor_qabul] data: {e}")