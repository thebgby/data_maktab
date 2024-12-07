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

    #  POCHEMUCHKADB EXTRACT
    p_sheet = sheets_conn.get_worksheet(0)
    p_sheet_data = p_sheet.get_values("A1:P")
    columns = [
        "regid",
        "sana",
        "manager_id",
        "manbda",
        "name_mijoz",
        "holati",
        "smen_id",
        "smen_vaqti",
        "qayta_sana",
        "tel1",
        "tel2",
        "izoh1",
        "izoh2",
        "izoh3",
        "izoh4",
        "izoh5"
    ]

    df = pd.DataFrame(p_sheet_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)  
    df = df.dropna(how='all')

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce")

    df["qayta_sana"] = df["qayta_sana"].str.replace(",", ".", regex=False)
    df["qayta_sana"] = pd.to_datetime(df["qayta_sana"], dayfirst=True, errors="coerce")
    final_data["pochemuchkadb"] = df
    # print(df)

    # MENEGER DB
    m_sheet = sheets_conn.get_worksheet(1)
    m_sheet_data = m_sheet.get_values("A1:B")
    columns = [
        "manager_id",
        "manager_name"
    ]

    df_m = pd.DataFrame(m_sheet_data[1:], columns=columns)

    final_data["pochemuchkadb_managerdb"] = df_m

    return final_data