import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import time
import pandas as pd
from config import gs_connection
from logs import logger
from config import maktab_royxat


def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    final_data = {}
    for sheet_name, worksheet in info.items():
        if isinstance(worksheet, list):
            if sheet_name == 'maktab_royxat_months':
                combined_df = pd.DataFrame()
                for sheets_index in worksheet:
                    worksheet_conn = sheets_conn.get_worksheet(sheets_index)
                    sheets_data = worksheet_conn.get_values("B3:L")
                    df = pd.DataFrame(sheets_data)
                    #data cleaning
                    df = df.map(lambda x: x if str(x).strip() != '' else None)
                    df = df[df.isna().sum(axis=1) < 7] # if row has more that 7 null column

                    for i in [5, 6, 8, 10]:
                        df[i] = df[i].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False).str.replace(" ", "", regex=False)
                        df[i] = df[i].fillna(0).astype(int)

                    df[4] = df[4].str.replace(",", ".", regex=False)
                    df[4] = pd.to_datetime(df[4], dayfirst=True, errors="coerce")
                    df[11] = worksheet_conn.title
                    combined_df = pd.concat([combined_df, df], ignore_index=True)

                combined_df.rename(columns={
                    0: 'fish',
                    1: 'sinfi',
                    2: 'tili',
                    3: 'telefon',
                    4: 'sana',
                    5: 'chegirma',
                    6: 'tushum',
                    7: 'kirim_order',
                    8: 'tushum_2',
                    9: 'qarzi',
                    10: 'ortiqcha',
                    11: 'worksheet_name'
                }, inplace=True)
                final_data[sheet_name] = combined_df
            elif sheet_name == 'maktab_royxat_uqituvchilar_oyligi':
                sheet_index = worksheet[0]
                sheets_data = sheets_conn.get_worksheet(sheet_index).get_values("B2:D")
                df = pd.DataFrame(sheets_data)

                # data cleaning
                df = df.map(lambda x: x if str(x).strip() != '' else None)
                df = df.dropna(how='all')

                # type converting
                df[1] = df[1].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False).str.replace(" ", "", regex=False)
                df[1] = df[1].astype(float) # for salary

                df.rename(columns={
                    0: 'full_name',
                    1: 'xisoblangan',
                    2: 'oyi'
                }, inplace=True)
                final_data[sheet_name] = df
            elif sheet_name == 'maktab_royxat_shaxzod_uchun':
                sheet_index = worksheet[0]
                sheets_data = sheets_conn.get_worksheet(sheet_index).get_values("B6:D")

                df = pd.DataFrame(sheets_data)

                # data cleaning
                df = df.map(lambda x: x if str(x).strip() != '' else None)
                df = df.dropna(how='all')
                df = df[df.isna().sum(axis=1) < 2].iloc[:-2]

                # type converting
                df[1] = df[1].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False).str.replace(" ", "", regex=False)
                df[1] = df[1].astype(float) # for salary
                df.rename(columns={
                    0: 'description',
                    1: 'summa',
                    2: 'muddati'
                }, inplace=True)
                final_data[sheet_name] = df
                            


    return final_data
            


    

    

# extract_data(maktab_royxat)
