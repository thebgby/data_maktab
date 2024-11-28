from sqlalchemy import create_engine
from logs import logger

def db_conn():
    try:
        conn = create_engine("postgresql+psycopg2://postgres_admin:admin_kleo345tWER@172.20.1.22/martech_db_main")
        # conn = create_engine("postgresql+psycopg2://roma:password@localhost/data")
        logger.info(f"Database Connection Successful")
        # conn = create_engine("postgresql://neondb_owner:d8wg9sJNtVUo@ep-bitter-smoke-a5zxbrjk.us-east-2.aws.neon.tech/neondb?sslmode=require")
        return conn
    except Exception as e:
        logger.error(f"error pg connection: {e}")
        return None

# db_conn()