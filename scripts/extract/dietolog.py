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

    # dietolog_students
    dstudents_sheets = sheets_conn.get_worksheet(0)
    dstudents_data = dstudents_sheets.get_values("A1:E")

    columns = [
        "num",
        "sana",
        "ism_familyasi",
        "sinfi",
        "dieta_turi"
    ]

    df = pd.DataFrame(dstudents_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 3]

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce", format="%d.%m.%Y")
    # print(df.shape)
    final_data["dietolog_students"] = df

    #menu_school
    menu_school = sheets_conn.get_worksheet(1)
    menu_school_data = menu_school.get_values("A1:E")

    columns = [
        "num",
        "sana",
        "kun",
        "vaqt",
        "ovqat_turi"
    ]
    df = pd.DataFrame(menu_school_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 4]

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce")

    final_data["menu_school"] = df

    return final_data

