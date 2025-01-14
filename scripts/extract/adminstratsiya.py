import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)

    # kundalik qabul
    sheets_data = sheets_conn.get_worksheet(0).get_values("A1:H")

    columns = [
        "num",
        "sana",
        "xarajat_mazmuni",
        "ulchov_birligi",
        "soni",
        "narxi",
        "summasi",
        "xarajat_manbasi"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    # df = df[df.isna().sum(axis=1) < 4]

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce", format="%d.%m.%Y")

    for i in ["num", "soni", "narxi", "summasi"]:
        df[i] = (
            df[i].astype(str)  
            .str.replace(r'\s+', '', regex=True)  
            .str.replace(r'\.', '', regex=True)  
            .str.replace(r',', '.', regex=True)  
            .replace('', np.nan) 
            .astype(float) 
        )

    return df
