import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text


def load_data(data: df):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""CREATE TABLE IF NOT EXISTS maktab_tadbirlar (
                            id SERIAL PRIMARY KEY,
                            sana DATE,
                            tadbir_nomi TEXT,
                            sinf text,
                            tadbir_turi text,
                            masul text
                        );

                        TRUNCATE TABLE maktab_tadbirlar;
                        """))
        c.commit()
    data.to_sql("maktab_tadbirlar", conn, if_exists="append", index=False)
