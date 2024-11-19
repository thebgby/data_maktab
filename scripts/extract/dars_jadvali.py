import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection, dars_jadvali
from logs import logger
import time

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)

    #  DARS JADVALI EXTRACT
    sheet_data = sheets_conn.get_worksheet(0)
    sheet_data = sheet_data.get_values("B2:H")
    columns = [
        "day",
        "class",
        "time",
        "lesson",
        "teacher",
        "xona",
        "type"
    ]

    df = pd.DataFrame(sheet_data, columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)  
    df = df.dropna(how='all')
    # print(df)
    return df

# extract_data(dars_jadvali)