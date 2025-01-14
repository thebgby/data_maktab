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
        CREATE TABLE IF NOT EXISTS printer_sheet (
            num int,
            sana date,
            printerchi text,
            mijoz_turi text,
            sinf text,
            qogoz_turi text,
            soni int,
            izoh text
        );       

        TRUNCATE TABLE printer_sheet ;
        """))
        c.commit()
    data.to_sql('printer_sheet', conn, if_exists="append", index=False)
