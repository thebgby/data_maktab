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
                       CREATE TABLE IF NOT EXISTS dietolog_students (
                        id serial primary key,
                        num int,
                        sana date,
                        ism_familyasi text,
                        sinfi text,
                        dieta_turi text
                    );

                    TRUNCATE TABLE dietolog_students;

    
                        CREATE TABLE IF NOT EXISTS menu_school (
                        id serial primary key,
                        num int,
                        sana date,
                        kun text,
                        vaqt text,
                        ovqat_turi text
                    );

                    TRUNCATE TABLE menu_school;
        """))
        c.commit()
    for table_name, df in data.items():
        # print(df.shape)
        # print(table_name)
        df.to_sql(table_name, conn, if_exists="append", index=False)
