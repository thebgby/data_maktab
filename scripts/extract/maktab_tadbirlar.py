import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection
# from logs import logger
# import time

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)

    #  maktab tadbirlar EXTRACT
    sheets_data = sheets_conn.get_worksheet(0).get_values("B1:F")

    columns = [
        "sana",
        "tadbir_nomi",
        "sinf",
        "tadbir_turi",
        "masul"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 4]

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce", format="%d.%m.%Y")
    # print(df)
    return df
