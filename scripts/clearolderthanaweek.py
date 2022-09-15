import sqlite3 as sl
import time

import os
from dotenv import load_dotenv

load_dotenv()

con = sl.connect(os.getenv("DBPATH"))
print("Connected to Database")

with con:
    currentUnix = int(time.time())
    aWeekAgoUnix = currentUnix - (7*24*60*60)
    con.execute("DELETE FROM DATA WHERE time<" + str(aWeekAgoUnix)) #terrible but works, delete relevant entries
print("Cleared Table")