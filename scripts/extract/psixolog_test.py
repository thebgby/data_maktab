import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    final_data = {}

    # class test
    class_test = sheets_conn.get_worksheet(0)
    class_test_data = class_test.get_values("B1:G")

    columns = [
        "date",
        "name",
        "class",
        "teacher",
        "test_name",
        "result"
    ]

    df = pd.DataFrame(class_test_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 4]

    df["date"] = df["date"].str.replace(",", ".", regex=False)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    # print(df.shape)
    final_data["psixolog_test_class"] = df

    #muloqot
    muloqot = sheets_conn.get_worksheet(1)
    # print(muloqot.title)
    muloqot_data = muloqot.get_values("B1:D")

    columns = [
        "date",
        "name",
        "mijoz_turi"
    ]
    # print(muloqot_data)
    df = pd.DataFrame(muloqot_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    # print(df)
    df["date"] = df["date"].str.replace(",", ".", regex=False)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    # print(df)
    final_data["psixolog_test_muloqot"] = df

    return final_data

