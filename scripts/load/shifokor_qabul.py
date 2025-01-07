import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text


def load_data(data: df):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""
                        create table if not exists shifokor_kundalik_qabul (
                            id serial primary key ,
                            sana date,
                            ism_familiya text,
                            sinfi text,
                            shikoyati text,
                            holati text,
                            muolaja text,
                            yechim text
                        );

                        truncate table shifokor_kundalik_qabul;
                        """))
        c.commit()
    data.to_sql("shifokor_kundalik_qabul", conn, if_exists="append", index=False)
