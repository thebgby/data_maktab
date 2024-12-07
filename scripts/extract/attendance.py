import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection, attendance

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)

    # class test
    worksheet = sheets_conn.get_worksheet(0)
    data = worksheet.get_values("A1:T")
    df = pd.DataFrame(data[1:])
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    #combine columns
    columns_to_combine = [col for col in df.columns if col not in [0, 1]]
    df['Combined'] = df[columns_to_combine].apply(lambda row: row.dropna().iloc[0] if not row.dropna().empty else np.nan, axis=1)
    df = df[[0, 1, 'Combined']]

    df.columns = ['Timestamp', 'Group', 'Combined Data']
    print(df)

extract_data(attendance)