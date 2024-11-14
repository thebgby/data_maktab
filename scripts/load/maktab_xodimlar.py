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
        CREATE TABLE IF NOT EXISTS maktab_xodimlar (
            id text,
            full_name text,
            birth_date date,
            malumoti text,
            jinsi text,
            departament_name text,
            role text,
            type text,
            tajribasi text,
            work_type text,
            working_hours int,
            start_date date,
            status text,
            end_date date,
            izoh text
        );
                    
        TRUNCATE TABLE maktab_xodimlar;  
                       
        CREATE TABLE IF NOT EXISTS maktab_xodimlar_teachers (
            id text,
            full_name text,
            birth_date date,
            jinsi text,
            subject text,
            type text,
            subject_teacher text,
            support text,
            mbr text,
            tugarak text,
            sinf_rahbar text,
            toifasi text,
            tajribasi text, 
            work_type text, 
            start_date date,
            status text,
            end_date date,
            izoh text
        );      

        TRUNCATE TABLE  maktab_xodimlar_teachers;               
        """))
        c.commit()
    for table_name, df in data.items():
        df.to_sql(table_name, conn, if_exists="append", index=False)