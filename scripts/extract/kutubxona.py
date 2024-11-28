import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection
from logs import logger
import time

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    final_data = {}

    # bookdb
    bookdb_sheet = sheets_conn.get_worksheet(0)
    bookdb_data = bookdb_sheet.get_values("A1:J")

    columns = [
        "id",
        "kitob_raqami",
        "toifa_id",
        "kitob_nomi",
        "nashr_yili",
        "tili",
        "soni",
        "summasi",
        "jami_summa",
        "izoh"
    ]

    bookdb_df = pd.DataFrame(bookdb_data[1:] ,columns=columns)
    bookdb_df = bookdb_df.map(lambda x: np.nan if str(x).strip() == '' else x)
    bookdb_df = bookdb_df.dropna(how='all')

    final_data["kutubxona_bookdb"] = bookdb_df

    # toifa
    toifa_sheet = sheets_conn.get_worksheet(1)
    toifa_data = toifa_sheet.get_values("A1:B")

    columns = [
        "toifa_id",
        "toifa_nomi"
    ]

    toifa_df = pd.DataFrame(toifa_data[1:] ,columns=columns)
    toifa_df = toifa_df.map(lambda x: np.nan if str(x).strip() == '' else x)
    toifa_df = toifa_df.dropna(how='all')

    final_data["kutubxona_toifa"] = toifa_df

    # ijara db
    ijara_sheet = sheets_conn.get_worksheet(2)
    ijara_data = ijara_sheet.get_values("A1:G")

    columns = [
        "ijara_id",
        "olgan_sana",
        "kitob_nomi",
        "student_name",
        "sinfi",
        "muddati",
        "holati"
    ]

    ijara_df = pd.DataFrame(ijara_data[1:] ,columns=columns)
    ijara_df = ijara_df.map(lambda x: np.nan if str(x).strip() == '' else x)
    ijara_df = ijara_df.dropna(how='all')

    ijara_df["olgan_sana"] = ijara_df["olgan_sana"].str.replace(",", ".", regex=False)
    ijara_df["olgan_sana"] = pd.to_datetime(ijara_df["olgan_sana"], dayfirst=True, errors="coerce", format="%d.%m.%Y")

    ijara_df["muddati"] = ijara_df["muddati"].str.replace(",", ".", regex=False)
    ijara_df["muddati"] = pd.to_datetime(ijara_df["muddati"], dayfirst=True, errors="coerce", format="%d.%m.%Y")

    final_data["kutubxona_ijaradb"] = ijara_df

    # student db
    student_sheet = sheets_conn.get_worksheet(3)
    student_data = student_sheet.get_values("A1:C")

    columns = [
        "student_id",
        "student_name",
        "sinf_id"
    ]
    student_df = pd.DataFrame(student_data[1:] ,columns=columns)
    student_df = student_df.map(lambda x: np.nan if str(x).strip() == '' else x)
    student_df = student_df.dropna(how='all')

    final_data["kutubxona_studentdb"] = student_df

    return final_data



