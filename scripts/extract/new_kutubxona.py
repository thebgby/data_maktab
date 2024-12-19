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

    # yetishmaydigan kitoblar
    worksheet = sheets_conn.get_worksheet(0)
    sheets_data = worksheet.get_values("A1:F")

    columns = [
        "no",
        "kitob_nomi",
        "turi",
        "sinf",
        "tili",
        "kerakli_miqdor"
    ]

    df = pd.DataFrame(sheets_data[1:] ,columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 5]

    final_data["n_kutubxona_yetishmaydigan_kitoblar"] = df

    # sinflar kesimida
    worksheet = sheets_conn.get_worksheet(1)
    sheets_data = worksheet.get_values("A1:H")

    columns = [
        "num",
        "kitob_nomi",
        "sinf",
        "turi",
        "tili",
        "oquvchi_soni",
        "jami_kitob",
        "berilgan_soni"
    ]

    df = pd.DataFrame(sheets_data[1:] ,columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 7]

    final_data["n_kutubxona_sinflar_kesimida"] = df

    # ijaradagi kitoblar
    worksheet = sheets_conn.get_worksheet(2)
    sheets_data = worksheet.get_values("A1:I")

    columns = [
        "num",
        "kitob_nomi",
        "sinf",
        "turi",
        "tili",
        "soni",
        "manba",
        "qaytarib_berilgan_soni",
        "status"
    ]

    df = pd.DataFrame(sheets_data[1:] ,columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 8]

    final_data["n_kutubxona_ijaradagi_kitoblar"] = df

    # pechat qilinganlar
    worksheet = sheets_conn.get_worksheet(3)
    sheets_data = worksheet.get_values("A1:F")

    columns = [
        "num",
        "kitob_nomi",
        "sinf",
        "turi",
        "tili",
        "soni"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 5]

    final_data["n_kutubxona_pechat_qilinganlar"] = df

    # berilgan konstovar
    worksheet = sheets_conn.get_worksheet(4)
    sheets_data = worksheet.get_values("A1:E")

    columns = [
        "num",
        "sana",
        "nomi",
        "soni",
        "oluvchi"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 4]

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce")

    final_data["n_kutubxona_berilgan_konstovar"] = df

    # kerak konstovar
    worksheet = sheets_conn.get_worksheet(5)
    sheets_data = worksheet.get_values("A1:F")

    columns = [
        "num",
        "nomi",
        "narxi",
        "soni",
        "summasi",
        "status"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 5]

    final_data["n_kutubxona_kerakli_konstovar"] = df

    return final_data



