import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from typing import Dict
from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import  text

def load_data(data: Dict[str, df]):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""
        CREATE TABLE IF NOT EXISTS maktab_royxat_months (
            id serial primary key,
            fish text,
            sinfi text,
            tili text,
            telefon text,
            sana date,
            chegirma int,
            tushum int,
            kirim_order text,
            tushum_2 int,
            qarzi text,
            ortiqcha int,
            worksheet_name text
        );
            
        TRUNCATE TABLE maktab_royxat_list;
                       
        CREATE TABLE IF NOT EXISTS maktab_royxat_uqituvchilar_oyligi (
            id serial primary key, 
            full_name text,
            xisoblangan int,
            oyi text
        );
                       
        TRUNCATE TABLE maktab_royxat_uqituvchilar_oyligi;

        CREATE TABLE IF NOT EXISTS maktab_royxat_shaxzod_uchun (
            id serial primary key, 
            description text,
            summa int,
            muddati text
        );
            
        TRUNCATE TABLE maktab_royxat_shaxzod_uchun;
                   
        """))
        c.commit()
    for table_name, df_data in data.items():
        df_data.to_sql(table_name, conn, if_exists="append", index=False)
