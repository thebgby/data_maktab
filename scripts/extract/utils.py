import pandas as pd
import numpy as np
import sys
import os
from worksheets import worksheets

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import gs_connection


def column_to_date(column): # convert column to date
    column = column.str.replace(",", ".", regex=False)
    return pd.to_datetime(column, dayfirst=True, errors="coerce", format="%d.%m.%Y")


def column_to_numeric(column): # convert column to numeric
    cleaned = (
        column.astype(str)  
        .str.replace(r'\s+', '', regex=True)  
        .str.replace(r'\.', '', regex=True)  
        .str.replace(r',', '.', regex=True)  
        .replace('', np.nan) 
        .astype(float) 
    ) 
    return cleaned

def data_as_df(w_data, worksheet): # sheets to df
    df = pd.DataFrame(w_data[1:], columns=worksheet["columns"])
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')
    if worksheet.get("thresh"):
        df = df[df.isna().sum(axis=1) < worksheet["thresh"]]

    if worksheet.get("date_columns"):
        for column in worksheet["date_columns"]:
            df[column] = column_to_date(df[column])

    if worksheet.get("numeric_columns"):
        for column in worksheet["numeric_columns"]:
            df[column] = column_to_numeric(df[column])

    return df

def extract_from_sheet(info: dict): #extract data
    sheets_url = info['url']
    sheets_conn = gs_connection(sheets_url)
    final_data = {}

    for worksheet in info["sheets"]:
        worksheet_data = sheets_conn.get_worksheet(worksheet['id']).get_values(worksheet['values'])
        df_data = data_as_df(worksheet_data, worksheet)
        final_data[worksheet["table_name"]] = df_data
    
    return final_data

def sql_ddl_dml(worksheet: dict, df: pd.DataFrame, conn):
    table_name = worksheet["table_name"]
    columns = worksheet["columns"]
    date_columns = worksheet["date_columns"] if worksheet.get("date_columns") else []
    numeric_columns = worksheet["numeric_columns"] if worksheet.get("numeric_columns") else {}
    query = f"create table {table_name} ("
    for column in columns:
        column_type = "text"
        if column in date_columns:
            column_type = "date"
        elif column in numeric_columns:
            column_type = "int" if numeric_columns[column] else "float"
        query += f"{column} {column_type}, "
    
    query = query.rstrip(", ") + (f");\ntruncate table {table_name};")
    df.to_sql(table_name, conn, if_exists="append", index=False)
    return query

    

# for sheet in worksheets:
#     for worksheet in sheet["sheets"]:
#         print(sql_func(worksheet))
        
        


