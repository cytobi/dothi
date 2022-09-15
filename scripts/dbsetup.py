import sqlite3 as sl

import os
from dotenv import load_dotenv

load_dotenv()

con = sl.connect(os.getenv("DBPATH"))
print("Connected to Database")

#create table with tuples: (time, temperature, humidity)
#time is unix timestamp, might break in 2038
with con:
    con.execute("""
        CREATE TABLE DATA (
            time INTEGER NOT NULL PRIMARY KEY,
            temperature INTEGER,
            humidity INTEGER
        );
    """)
print("Created Table")