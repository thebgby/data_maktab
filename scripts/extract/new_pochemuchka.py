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

    #  rating students
    p_sheet = sheets_conn.get_worksheet(0)
    p_sheet_data = p_sheet.get_values("A1:V")
    columns = [
        "no",
        "name",
        "group"
        "month_1",
        "note_1",
        "month_2",
        "note_2",
        "month_3",
        "note_3",
        "month_4",
        "note_4",
        "month_5",
        "note_5",
        "month_6",
        "note_6",
        "month_7",
        "note_7",
        "month_8",
        "note_8",
        "month_9",
        "note_9",
        "month_10",
        "note_10",
    ]

    df = pd.DataFrame(p_sheet_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')

    df = df[df.isna().sum(axis=1) < 21]
    month_columns = [col for col in df.columns if col.startswith("month_")]
    df[month_columns] = df[month_columns].apply(
        lambda x: x.astype(str).str.replace('%', '', regex=False).replace('nan', '0').astype(float)
    )

    final_data["p_rating_students"] = df
    # print(df)

    # contact parents
    m_sheet = sheets_conn.get_worksheet(1)
    m_sheet_data = m_sheet.get_values("A1:V")
    columns = [
        "no",
        "name",
        "month_1",
        "response_1",
        "month_2",
        "response_2",
        "month_3",
        "response_3",
        "month_4",
        "response_4",
        "month_5",
        "response_5",
        "month_6",
        "response_6",
        "month_7",
        "response_7",
        "month_8",
        "response_8",
        "month_9",
        "response_9",
        "month_10",
        "response_10",
    ]

    df_m = pd.DataFrame(m_sheet_data[1:], columns=columns)
    df_m = df_m.map(lambda x: np.nan if str(x).strip() == '' else x)
    df_m = df_m.dropna(how='all')
    # print(df_m)
    # print(df_m.isnull().sum(axis=1))
    df_m = df_m[df_m.isna().sum(axis=1) < 21]
    final_data["contact_parents_pochemuchka"] = df_m

    return final_data