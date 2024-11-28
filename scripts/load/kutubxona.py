import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from typing import Dict
from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text
from logs import logger


def load_data(data: Dict[str, df]):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""create table if not exists kutubxona_bookdb (
                            table_id serial primary key,
                            id text,
                            kitob_raqami int,
                            toifa_id text,
                            kitob_nomi text,
                            nashr_yili int,
                            tili text,
                            soni int,
                            summasi int,
                            jami_summa int,
                            izoh text
                        );
                        
                        truncate table kutubxona_bookdb;
                        
                        create table if not exists kutubxona_toifa (
                            id serial primary key,
                            toifa_id text,
                            toifa_nomi text
                        );
                        
                        truncate table kutubxona_toifa;
                        
                        create table if not exists kutubxona_ijaradb (
                            id serial primary key,
                            ijara_id text,
                            olgan_sana date,
                            kitob_nomi text,
                            student_name text,
                            sinfi text,
                            muddati date,
                            holati text
                        );
                        
                        truncate table kutubxona_ijaradb;
                        
                        create table if not exists kutubxona_studentdb (
                            id serial primary key,
                            student_id text,
                            student_name text,
                            sinf_id text
                        );
                        
                        truncate table kutubxona_studentdb;"""))
        c.commit()
    for table_name, df in data.items():
        df.to_sql(table_name, conn, if_exists="append", index=False)
