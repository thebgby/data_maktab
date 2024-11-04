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
        CREATE TABLE IF NOT EXISTS pnl_2024 (
            id serial primary key,
            sana date,
            xarajat_mazmuni text,
            summa decimal,
            manba text,
            bolim text,
            sheet text  );
            
        TRUNCATE TABLE pnl_2024
        """))
        c.commit()

    data.to_sql("pnl_2024", conn, if_exists="append", index=False)
