import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import time
import pandas as pd
from config import gs_connection
from logs import logger
from config import maktab_kassa

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    final_data = {}
    for sheet_name, worksheet in info.items():
        if isinstance(worksheet, list):
            if sheet_name == 'maktab_kassa_months':
                combined_df = pd.DataFrame()
                for sheets_index in worksheet:
                    worksheet_conn = sheets_conn.get_worksheet(sheets_index)
                    sheets_data = worksheet_conn.get_values("B2:I")
                    df = pd.DataFrame(sheets_data)
                    #data cleaning
                    df = df.map(lambda x: x if str(x).strip() != '' else None)
                    df = df[df.isna().sum(axis=1) < 5] # if row has more that 7 null column

                    for i in [5, 7]:
                        df[i] = df[i].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False).str.replace(" ", "", regex=False)
                        df[i] = df[i].fillna(0).astype(float)

                    df[4] = df[4].str.replace(",", ".", regex=False)
                    df[4] = pd.to_datetime(df[4], dayfirst=True, errors="coerce")
                    df[8] = worksheet_conn.title
                    combined_df = pd.concat([combined_df, df], ignore_index=True)

                combined_df.rename(columns={
                    0: 'fio',
                    1: 'sinfi',
                    2: 'tili',
                    3: 'sinfi_2',
                    4: 'sana',
                    5: 'num_column',
                    6: 'tolov_turi',
                    7: 'summa',
                    8: 'worksheet_name'
                }, inplace=True)
                final_data[sheet_name] = combined_df

            elif sheet_name == 'maktab_kassa_gazel_tulovi':
                sheet_index = worksheet[0]
                worksheet_conn = sheets_conn.get_worksheet(sheet_index)
                sheets_data = worksheet_conn.get_values("B2:H")
                df = pd.DataFrame(sheets_data)
                # print(df.head(30))
                # data cleaning
                df = df.map(lambda x: x if str(x).strip() != '' else None)
                df = df[df.isna().sum(axis=1) < 5] # if row has more that 5 null column

                # type converting
                for i in (4, 6):
                    df[i] = df[i].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False).str.replace(" ", "", regex=False)
                    df[i] = df[i].astype(float) # for int columns

                df[3] = df[3].str.replace(",", ".", regex=False)
                df[3] = pd.to_datetime(df[3], dayfirst=True, errors="coerce")

                df.rename(columns={
                    0: 'fio',
                    1: 'sinfi',
                    2: 'telefon',
                    3: 'sana',
                    4: 'chek_raqami',
                    5: 'tolov_turi',
                    6: 'summa'
                }, inplace=True)
                # print(df.shape)
                final_data[sheet_name] = df
            elif sheet_name == 'maktab_kassa_qaytarilgan_tulovlar':
                sheet_index = worksheet[0]
                worksheet_conn = sheets_conn.get_worksheet(sheet_index)
                sheets_data = worksheet_conn.get_values("B1:I")

                df = pd.DataFrame(sheets_data)

                # data cleaning
                df = df.map(lambda x: x if str(x).strip() != '' else None)
                df = df.dropna(how='all')
                # df = df[df.isna().sum(axis=1) < 2]

                # type converting
                df[7] = df[7].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False).str.replace(" ", "", regex=False)
                df[7] = pd.to_numeric(df[7], errors='coerce').fillna(0)
                df[7] = df[7].astype(float) # for salary

                df[4] = df[4].str.replace(",", ".", regex=False)
                df[4] = pd.to_datetime(df[4], dayfirst=True, errors="coerce")

                df.rename(columns={
                    0: 'fio',
                    1: 'sinfi',
                    2: 'tili',
                    3: 'telefon',
                    4: 'sana',
                    5: 'order_column',
                    6: 'tolov_turi',
                    7: 'summa'
                }, inplace=True)
                final_data[sheet_name] = df
                # print(df)
                            


    return final_data

# extract_data(maktab_kassa)