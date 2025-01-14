import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text


def load_data(data: df):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""create table if not exists adminstratsiya_xarajatlar (
                            id serial primary key ,
                            num int,
                            sana date,
                            xarajat_mazmuni text,
                            ulchov_birligi text,
                            soni float,
                            narxi float,
                            summasi int,
                            xarajat_manbasi text
                        );

                        truncate table adminstratsiya_xarajatlar;
                        """))
        c.commit()
    data.to_sql("adminstratsiya_xarajatlar", conn, if_exists="append", index=False)
