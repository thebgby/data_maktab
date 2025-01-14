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

    # baza
    baza = sheets_conn.get_worksheet(0)
    baza_data = baza.get_values("A1:J")

    columns = [
        "id",
        "date",
        "studentid",
        "yoshi",
        "class",
        "muammosi",
        "sabab",
        "qilingan_ish",
        "metod",
        "ozgarish"
    ]

    df = pd.DataFrame(baza_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    # df = df[df.isna().sum(axis=1) < 4]

    df["date"] = df["date"].str.replace(",", ".", regex=False)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

    df["yoshi"] = (
            df["yoshi"].astype(str)  
            .str.replace(r'\s+', '', regex=True)  
            .str.replace(r'\.', '', regex=True)  
            .str.replace(r',', '.', regex=True)  
            .replace('', np.nan) 
            .astype(float) 
        )
    # print(df.shape)
    final_data["psbaza_baza"] = df

    #student
    student = sheets_conn.get_worksheet(1)
    student_data = student.get_values("A1:E")

    columns = [
        "studentid",
        "name",
        "yoshi",
        "sinfid",
        "sinfrahbari"
    ]
    # print(muloqot_data)
    df = pd.DataFrame(student_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df["yoshi"] = (
            df["yoshi"].astype(str)  
            .str.replace(r'\s+', '', regex=True)  
            .str.replace(r'\.', '', regex=True)  
            .str.replace(r',', '.', regex=True)  
            .replace('', np.nan) 
            .astype(float) 
        )

    final_data["psbaza_student"] = df
    #sinf
    sinf = sheets_conn.get_worksheet(2)
    sinf_data = sinf.get_values("A1:B")

    columns = [
        "sinfid",
        "name"
    ]
    # print(muloqot_data)
    df = pd.DataFrame(sinf_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    final_data["psbaza_sinf"] = df


    return final_data

