import sqlite3 as sl

import os
from dotenv import load_dotenv

load_dotenv()

con = sl.connect(os.getenv("DBPATH"))
print("Connected to Database")

with con:
    con.execute("DELETE FROM DATA") #delete all
print("Cleared Table")