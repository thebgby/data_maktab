import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from config import db_conn
from pandas import DataFrame as Df
from sqlalchemy import  text

def load_data(data: Df):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""
        CREATE TABLE IF NOT EXISTS avtobus_sheet (
            num text,
            student text,
            parents text,
            phone1 text,
            phone2 text,
            class text,
            destination text,
            station text,
            time text,
            teacher text,
            sheet_name text
            );
            
        TRUNCATE TABLE avtobus_sheet
        """))
        c.commit()

    data.to_sql("avtobus_sheet", conn, if_exists="append", index=False)
