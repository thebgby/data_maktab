import gspread
from logs import logger
import os

def gs_connection(sheets_url, cred=os.path.join(os.path.dirname(__file__), 'key.json')):
    try:
        sheet = gspread.service_account(cred)
        sheet = sheet.open_by_url(sheets_url)
        return sheet
    except Exception as e:
        logger.error(f"error gspread connection: {e}")
        return None