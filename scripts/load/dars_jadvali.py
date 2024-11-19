import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from config import db_conn
import pandas as pd
from sqlalchemy import text

def load_data(data: pd.DataFrame):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""
        CREATE TABLE IF NOT EXISTS dars_jadvali (
            id serial primary key,
            day text,
            class text,
            time text,
            lesson text,
            teacher text,
            xona text,
            type text
        );       

        TRUNCATE TABLE dars_jadvali ;
        """))
        c.commit()
    data.to_sql('dars_jadvali', conn, if_exists="append", index=False)
