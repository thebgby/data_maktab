import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # for importing modules

from scripts.extract import extract_data
from scripts.load import load_data
from config import pnl

pnl_data = extract_data(pnl)
load_data(pnl_data)