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
        create table if not exists psbaza_baza (
            id text,
            date date,
            studentid text,
            yoshi int,
            class text,
            muammosi text,
            sabab text,
            qilingan_ish text,
            metod text,
            ozgarish text
        );

        truncate table psbaza_baza;

        create table if not exists psbaza_student (
            studentid text,
            name text,
            yoshi int,
            sinfid text,
            sinfrahbari text
        );

        truncate table psbaza_student;

        create table if not exists psbaza_sinf (
            sinfid text,
            name text
        );

        truncate table psbaza_sinf;
           
        """))
        c.commit()
    for table_name, df in data.items():
        df.to_sql(table_name, conn, if_exists="append", index=False)
