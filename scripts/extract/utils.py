import pandas as pd
import numpy as np
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

from config import gs_connection

worksheets = [
    {
        "name": "psixolog_test",
        "url": "https://docs.google.com/spreadsheets/d/1YfQ8AI0fWw0OYOtBEe-vpBqTzz9aPnDwN3lhFGfiBso/edit?usp=sharing",
        "sheets": [
            {
                "id": 0,
                "table_name": "psixolog_test_class",
                "values": "B1:G",
                "thresh": 4,
                "columns": [
                    "date",
                    "name",
                    "class",
                    "teacher",
                    "test_name",
                    "result"
                ],
                "date_columns": ["date"]
            },
            {
                "id": 1,
                "table_name": "psixolog_test_muloqot",
                "values": "B1:D",
                # "thresh": 4,
                "columns": [
                    "date",
                    "name",
                    "mijoz_turi"
                ],
                "date_columns": ["date"]
            }
        ]
    },

]


worksheet = worksheets[0]
print(worksheet)


def data_as_df(w_data, columns):
    df = pd.DataFrame(w_data[1:], columns=columns)
    df = df.map(lambda x: np.nan if str(x).strip() == '' else x)
    df = df.dropna(how='all')

def extract_from_sheet(info: dict):
    sheets_url = info['url']
    sheets_conn = gs_connection(sheets_url)
    final_data = {}

    for worksheet in info["sheets"]:
        worksheet_data = sheets_conn.get_worksheet(worksheet['id']).get_values(worksheet['values'])
        
        


