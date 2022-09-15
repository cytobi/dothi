import sqlite3 as sl

import os
from dotenv import load_dotenv

load_dotenv()

con = sl.connect(os.getenv("DBPATH"))
print("Connected to Database")

print("Data:")
with con:
    data = con.execute("SELECT * FROM DATA") #get everything
    for row in data:
        print(row) #print all tuples