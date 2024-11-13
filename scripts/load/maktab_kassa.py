import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from typing import Dict
from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text
from logs import logger

def load_data(data: Dict[str, df]):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""
        CREATE TABLE IF NOT EXISTS maktab_kassa_months (
            id serial primary key,
            fio text,
            sinfi text,
            tili text,
            sinfi_2 text,
            sana date,
            num_column int,
            tolov_turi text,
            summa int,
            worksheet_name text
        );
            
        TRUNCATE TABLE maktab_kassa_months;
                       
        CREATE TABLE IF NOT EXISTS maktab_kassa_gazel_tulovi (
            id serial primary key,
            fio text,
            sinfi text,
            telefon text,
            sana date,
            chek_raqami int,
            tolov_turi text,
            summa int
        );
                       
        TRUNCATE TABLE maktab_kassa_gazel_tulovi;

        CREATE TABLE IF NOT EXISTS maktab_kassa_qaytarilgan_tulovlar (
            id serial primary key,
            fio text,
            sinfi text,
            tili text,
            telefon text,
            sana date,
            order_column text,
            tolov_turi text,
            summa int
        );

            
        TRUNCATE TABLE maktab_kassa_qaytarilgan_tulovlar;
                   
        """))
        c.commit()
    for table_name, df_data in data.items():
        df_data.to_sql(table_name, conn, if_exists="append", index=False)
        logger.info(f"{table_name} loaded")
