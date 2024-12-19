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
        c.execute(text("""CREATE TABLE IF NOT EXISTS n_kutubxona_yetishmaydigan_kitoblar (
                    id serial primary key ,
                    no int,
                    kitob_nomi text,
                    turi text,
                    sinf text,
                    tili text,
                    kerakli_miqdor int
                );
                
                TRUNCATE TABLE n_kutubxona_yetishmaydigan_kitoblar;
                
                CREATE TABLE IF NOT EXISTS n_kutubxona_sinflar_kesimida (
                    id serial primary key,
                    num int,
                    kitob_nomi text,
                    sinf text,
                    turi text,
                    tili text,
                    oquvchi_soni int,
                    jami_kitob int,
                    berilgan_soni int
                );
                
                TRUNCATE TABLE n_kutubxona_sinflar_kesimida;
                
                CREATE TABLE IF NOT EXISTS n_kutubxona_ijaradagi_kitoblar (
                    id serial primary key ,
                    num int,
                    kitob_nomi text,
                    sinf text,
                    turi text,
                    tili text,
                    soni int,
                    manba text,
                    qaytarib_berilgan_soni int,
                    status text
                );
                
                TRUNCATE TABLE n_kutubxona_ijaradagi_kitoblar;
                
                CREATE TABLE IF NOT EXISTS n_kutubxona_pechat_qilinganlar (
                    id serial primary key ,
                    num int,
                    kitob_nomi text,
                    sinf text,
                    turi text,
                    tili text,
                    soni int
                );
                
                TRUNCATE TABLE n_kutubxona_pechat_qilinganlar;
                
                CREATE TABLE IF NOT EXISTS n_kutubxona_berilgan_konstovar (
                    id serial primary key,
                    num int,
                    sana date,
                    nomi text,
                    soni text,
                    oluvchi text
                );
                
                TRUNCATE TABLE n_kutubxona_berilgan_konstovar;
                
                CREATE TABLE IF NOT EXISTS n_kutubxona_kerakli_konstovar (
                    id serial primary key ,
                    num int,
                    nomi text,
                    narxi int,
                    soni text,
                    summasi int,
                    status text
                );
                
                TRUNCATE TABLE n_kutubxona_kerakli_konstovar;"""))
        c.commit()
    for table_name, df in data.items():
        df.to_sql(table_name, conn, if_exists="append", index=False)
