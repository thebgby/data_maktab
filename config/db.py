from sqlalchemy import create_engine

def db_conn():
    try:
        conn = create_engine("postgresql+psycopg2://roma:password@localhost/data")
        return conn
    except Exception as e:
        print(f"error on pg connection {e}")
        return None