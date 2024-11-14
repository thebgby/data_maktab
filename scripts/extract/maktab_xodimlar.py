import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # for importing modules

import pandas as pd
from config import gs_connection
# from logs import logger
import time

def extract_data(info: dict):
    sheets_url = info["url"]
    sheets_conn = gs_connection(sheets_url)
    final_data = {}