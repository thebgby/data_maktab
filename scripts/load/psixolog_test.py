import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from typing import Dict
from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text


def load_data(data: Dict[str, df]):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""
        create table if not exists psixolog_test_class (
        id serial primary key,
        date date,
        name text,
        class text,
        teacher text,
        test_name text,
        result text,
        extra_result text
    );
    
    truncate table psixolog_test_class;
    
    create table if not exists psixolog_test_muloqot (
        id serial primary key,
        date date,
        name text,
        mijoz_turi text
    );
    
    truncate table psixolog_test_muloqot;
        """))
        c.commit()
    for table_name, df in data.items():
        # print(df.shape)
        df.to_sql(table_name, conn, if_exists="append", index=False)
