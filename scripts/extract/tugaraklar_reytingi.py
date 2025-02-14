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

    #  TUGARAKLAR REYTINGI EXTRACT
    sheets_data = sheets_conn.get_worksheet(0).get_values("A1:I")

    columns = [
        "num",
        "date",
        "subject",
        "name",
        "group_name",
        "defect",
        "advantages",
        "score",
        "note"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 4]

    df["date"] = df["date"].str.replace(",", ".", regex=False)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce", format="%d.%m.%Y")
    # print(df)
    return df
