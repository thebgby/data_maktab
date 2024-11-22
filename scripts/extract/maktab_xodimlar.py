import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection, maktab_xodimlar
from logs import logger
import time

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    final_data = {}

    # XODIMLAR SHEETS
    time.sleep(5)
    try:
        xodimlar_sheet = sheets_conn.get_worksheet(0)
        xodimlar_sheet_data = xodimlar_sheet.get_values("B1:P")
        columns = [
            "id",
            "full_name",
            "birth_date",
            "malumoti",
            "jinsi",
            "departament_name",
            "role",
            "type",
            "tajribasi",
            "work_type",
            "working_hours",
            "start_date",
            "status",
            "end_date",
            "izoh"
        ]

        df = pd.DataFrame(xodimlar_sheet_data[1:], columns=columns)
        df = df.map(lambda x: np.nan if str(x).strip() == '' else x)  
        df = df.dropna(how='all')
        
        df["birth_date"] = df["birth_date"].str.replace(",", ".", regex=False)
        df["birth_date"] = pd.to_datetime(df["birth_date"], dayfirst=True, errors="coerce")

        df["start_date"] = df["start_date"].str.replace(",", ".", regex=False)
        df["start_date"] = pd.to_datetime(df["start_date"], format="%d.%m.%y", errors="coerce")

        df["end_date"] = df["end_date"].str.replace(",", ".", regex=False)
        df["end_date"] = pd.to_datetime(df["end_date"], format="%d.%m.%y", errors="coerce")

        final_data["maktab_xodimlar"] = df
    except Exception as e:
        logger.error(f"maktab_xodimlar | {e}")
    time.sleep(5)
    # TEACHERS SHEETS
    try:
        teachers_sheet = sheets_conn.get_worksheet(1)
        teachers_sheet_data = teachers_sheet.get_values("B1:S")
        columns = [
            "id",
            "full_name",
            "birth_date",
            "jinsi",
            "subject",
            "type",
            "subject_teacher",
            "support",
            "mbr",
            "tugarak",
            "sinf_rahbar",
            "toifasi",
            "tajribasi",
            "work_type",
            "start_date",
            "status",
            "end_date",
            "izoh"
        ]
        df = pd.DataFrame(teachers_sheet_data[1:], columns=columns)
        df = df.map(lambda x: np.nan if str(x).strip() == '' else x)  
        df = df.dropna(how='all')

        df["birth_date"] = df["birth_date"].str.replace(",", ".", regex=False)
        df["birth_date"] = pd.to_datetime(df["birth_date"], dayfirst=True, errors="coerce")


        df["start_date"] = df["start_date"].str.replace(",", ".", regex=False)
        df["start_date"] = pd.to_datetime(df["start_date"], dayfirst=True, errors="coerce")
        
        try:
            df["end_date"] = df["end_date"].str.replace(",", ".", regex=False)
            df["end_date"] = pd.to_datetime(df["end_date"], dayfirst=True, errors="coerce")
        except:
            pass

        final_data["maktab_xodimlar_teachers"] = df
    except Exception as e:
        logger.error(f"maktab_xodimlar_teachers | {e}")
    return final_data
    # print(df)
# extract_data(maktab_xodimlar)