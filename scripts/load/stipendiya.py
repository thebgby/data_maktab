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
        CREATE TABLE IF NOT EXISTS scholarships (
            id serial primary key,
            class_name TEXT,
            full_name TEXT,
            october TEXT,
            october_scholarship TEXT,
            november TEXT,
            november_scholarship TEXT,
            december TEXT,
            december_scholarship TEXT,
            january TEXT,
            january_scholarship TEXT,
            february TEXT,
            february_scholarship TEXT,
            march TEXT,
            march_scholarship TEXT,
            april TEXT,
            april_scholarship TEXT,
            may TEXT,
            may_scholarship TEXT,
            june TEXT,
            june_scholarship TEXT
        );
            
        TRUNCATE TABLE scholarships;  
        """))
        c.commit()
    data.to_sql("scholarships", conn, if_exists="append", index=False)