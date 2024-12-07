import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import db_conn
from pandas import DataFrame as df
from sqlalchemy import text


def load_data(data: df):
    conn = db_conn()
    with conn.connect() as c:
        c.execute(text("""create table if not exists nps (
                            id serial primary key,
                            sana date,
                            jami_guruh_ishtirokchilari int,
                            ovoz_berganlar int,
                            tanqidchilar int,
                            neytrallar int,
                            targibotchilar int,
                            sheet_name text
                        );
                        
                        truncate table nps;"""))
        c.commit()
    data.to_sql("nps", conn, if_exists="append", index=False)
