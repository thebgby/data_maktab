import sys
import os
import time
import pandas as pd
from config import gs_connection, pnl, db_conn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules


def extract_data(info: dict):
    global worksheet
    combined_df = pd.DataFrame()

    for year in info:
        sheets = info[year]
        for sheet in sheets:
            sheets_conn = gs_connection(sheets[sheet]["url"])
            for worksheet_id in sheets[sheet]['default_sheets'] + sheets[sheet]['other_sheets']:
                try:
                    worksheet = sheets_conn.get_worksheet(worksheet_id)

                    # Fetch data from worksheet
                    if worksheet_id in sheets[sheet]['other_sheets']:
                        data = worksheet.get_values("B5:F")
                    else:
                        data = worksheet.get_values("B5:E")

                    # Check if the worksheet is empty
                    if not data or all(not any(cell.strip() for cell in row) for row in data):
                        print(f"Empty sheet:'{worksheet.title}'. in {sheet}")
                        continue

                    # Convert to DataFrame and perform transformations
                    df = pd.DataFrame(data)

                    if worksheet_id in sheets[sheet]['other_sheets']:
                        df[1] = df[1].astype(str) + ' | ' + df[2].astype(str)
                        df = df.drop(columns=[2])
                        df = df.rename(columns={3: 2, 4: 3})

                    # Data cleaning and transformation
                    df = df.map(lambda x: x if str(x).strip() != '' else None)
                    df = df.dropna(how='all')
                    df[2] = df[2].str.replace("\xa0", "", regex=False).str.replace(",", ".", regex=False)
                    df[2] = df[2].astype(float)
                    df[0] = df[0].str.replace(",", ".", regex=False)


                    df[0] = pd.to_datetime(df[0], dayfirst=True, errors="coerce")
                    df[4] = worksheet.title
                    df[5] = sheet
                    combined_df = pd.concat([combined_df, df], ignore_index=True)

                    time.sleep(5)
                except Exception as e:
                    print(f"Error processing worksheet '{worksheet.title}': {e}")

    print(f"Final DataFrame size for PNL extracted: {combined_df.shape}")
    combined_df = combined_df.rename(columns={0: "sana", 1: "xarajat_mazmuni", 2: "summa", 3: "manba", 4: "bolim", 5: "sheet"})
    return combined_df
