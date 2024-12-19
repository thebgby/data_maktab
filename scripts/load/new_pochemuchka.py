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
        c.execute(text("""CREATE TABLE if not exists p_rating_students (
                            id serial primary key,
                            no int,
                            name text,
                            month_1 int,
                            note_1 text,
                            month_2 int,
                            note_2 text,
                            month_3 int,
                            note_3 text,
                            month_4 int,
                            note_4 text,
                            month_5 int,
                            note_5 text,
                            month_6 int,
                            note_6 text,
                            month_7 int,
                            note_7 text,
                            month_8 int,
                            note_8 text,
                            month_9 int,
                            note_9 text,
                            month_10 int,
                            note_10 text
                        );
                        
                        TRUNCATE TABLE p_rating_students;
                        
                        CREATE TABLE if not exists contact_parents_pochemuchka (
                            no int,
                            name text,
                            month_1 text,
                            response_1 text,
                            month_2 text,
                            response_2 text,
                            month_3 text,
                            response_3 text,
                            month_4 text,
                            response_4 text,
                            month_5 text,
                            response_5 text,
                            month_6 text,
                            response_6 text,
                            month_7 text,
                            response_7 text,
                            month_8 text,
                            response_8 text,
                            month_9 text,
                            response_9 text,
                            month_10 text,
                            response_10 text
                        );
                        
                        TRUNCATE TABLE contact_parents_pochemuchka;
                        """))
        c.commit()
    for table_name, df in data.items():
        df.to_sql(table_name, conn, if_exists="append", index=False)
