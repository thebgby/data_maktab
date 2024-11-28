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
        CREATE TABLE IF NOT EXISTS pochemuchkadb (
			regid text,
			sana date,
			manager_id text,
			manbda text,
			name_mijoz text,
			holati text,
			smen_id text,
			smen_vaqti text,
			qayta_sana text,
			tel1 text,
			tel2 text,
			izoh1 text,
			izoh2 text,
			izoh3 text,
			izoh4 text,
			izoh5 text
		);
                    
        TRUNCATE TABLE pochemuchkadb;  
                       
        CREATE TABLE IF NOT EXISTS pochemuchkadb_managerdb (
            manager_id text,
			manager_name text
        );      
                       
        
        TRUNCATE TABLE  pochemuchkadb_managerdb;  
           
        """))
        c.commit()
    for table_name, df in data.items():
        df.to_sql(table_name, conn, if_exists="append", index=False)
