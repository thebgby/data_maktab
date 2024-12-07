import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection
import  numpy as np


def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    combined_df = pd.DataFrame()

    for i in [0, 1]:
        worksheet = sheets_conn.get_worksheet(i)
        worksheet_data = worksheet.get_values("A1:F")
        columns = [
            "sana",
            "jami_guruh_ishtirokchilari",
            "ovoz_berganlar",
            "tanqidchilar",
            "neytrallar",
            "targibotchilar"
        ]

        df = pd.DataFrame(worksheet_data[1:], columns=columns)
        df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
        df = df.dropna(how='all')

        df["sana"] = df["sana"].str.replace(",", ".", regex=False)
        df["sana"] = pd.to_datetime(df["sana"], dayfirst=True, errors="coerce")
        df["sheet_name"] = worksheet.title

        combined_df = pd.concat([combined_df, df])
    return combined_df