import gspread

def gs_connection(sheets_url, cred='/home/roma/Documents/data/config/key.json'):
    try:
        sheet = gspread.service_account(cred)
        sheet = sheet.open_by_url(sheets_url)
        return sheet
    except Exception as e:
        print(f"error while conencting google sheets on {sheets_url} sheets")
        return None