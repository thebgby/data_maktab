import gspread
from logs import logger

def gs_connection(sheets_url, cred='/home/roma/Documents/data/config/key.json'):
    try:
        sheet = gspread.service_account(cred)
        sheet = sheet.open_by_url(sheets_url)
        return sheet
    except Exception as e:
        logger.error(f"error gspread connection: {e}")
        return None