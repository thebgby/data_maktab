import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text


def load_data(data: df):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""create table if not exists tugaraklar_reytingi (
                        id serial primary key,
                        num int,
                        date date,
                        subject text,
                        name text,
                        group_name text,
                        defect text,
                        advantages text,
                        score int,
                        note text
                        );
                        
                        truncate table tugaraklar_reytingi;
                        """))
        c.commit()
    data.to_sql("tugaraklar_reytingi", conn, if_exists="append", index=False)
