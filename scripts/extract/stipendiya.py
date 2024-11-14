import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection
# from logs import logger
import time

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    combined_df = pd.DataFrame()
    for sheets_index in range(len(sheets_conn.worksheets())):
        worksheet_conn = sheets_conn.get_worksheet(sheets_index)
        sheets_data = worksheet_conn.get_values("A2:T")
        df = pd.DataFrame(sheets_data)
        df = df.map(lambda x: np.nan if str(x).strip() == '' else x)  
        df = df.dropna(how='all')
        df = df.dropna(thresh=3)

        values_to_remove = ["Стипендия ответы", "Класс"]
        df = df[~df.iloc[:, 0].str.strip().isin(values_to_remove)]
        combined_df = pd.concat([combined_df, df], ignore_index=True)
        time.sleep(5)
    
    combined_df.columns = [
        "class_name", "full_name", "october", "october_scholarship",
        "november", "november_scholarship", "december", "december_scholarship",
        "january", "january_scholarship", "february", "february_scholarship",
        "march", "march_scholarship", "april", "april_scholarship",
        "may", "may_scholarship", "june", "june_scholarship"
    ]

    return combined_df

# extract_data(stipendiya)