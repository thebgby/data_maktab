import sys
import os
import numpy as np
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection

def clean_and_convert(value):
    if pd.isnull(value):  # If the value is already NaN, return NaN
        return np.nan
    try:
        # Remove all non-numeric characters except for dots and commas
        clean_value = re.sub(r'[^\d.,]', '', str(value))
        # Replace commas with dots (to handle decimal conversion)
        clean_value = clean_value.replace(',', '.')
        return float(clean_value)  # Attempt conversion to float
    except ValueError:
        return np.nan

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)

    sheets_data = sheets_conn.get_worksheet(0).get_values("A1:H")

    columns = [
        "num",
        "sana",
        "printerchi",
        "mijoz_turi",
        "sinf",
        "qogoz_turi",
        "soni",
        "izoh"
    ]

    df = pd.DataFrame(sheets_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    df = df[df.isna().sum(axis=1) < 6]

    df["sana"] = df["sana"].str.replace(",", ".", regex=False)
    df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce", format="%d.%m.%Y")

    for i in ["soni"]:
            df[i] = (
                df[i].astype(str)  # Ensure all values are strings
                .str.replace(r'\s+', '', regex=True)  # Remove whitespace
                .apply(clean_and_convert)  # Clean and convert each value
            )
    # print(df)
    return df
