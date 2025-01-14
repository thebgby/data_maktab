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
        CREATE TABLE IF NOT EXISTS materialniy_atchot (
            id int,
            kirim text,
            ulchov_birligi text,
            miqdori float,
            sana date,
            narxi float,
            jami float,
            maxsulot_turi text,
            sheet_name text
            );
            
        TRUNCATE TABLE materialniy_atchot
        """))
        c.commit()

    data.to_sql("materialniy_atchot", conn, if_exists="append", index=False)
