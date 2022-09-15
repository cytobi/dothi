import sqlite3 as sl
import time

import os
from dotenv import load_dotenv

load_dotenv()

con = sl.connect(os.getenv("DBPATH"))
print("Connected to Database")

currentTime = time.time()
sql = 'INSERT INTO DATA (time, temperature, humidity) values(?, ?, ?)' #test query
data = [
    (currentTime, 23, 65),
    (1153453456, 26, 43),
    (1567524567, 31, 54)
] #test data
with con:
    con.executemany(sql, data) #execute multiple statements at once
print("Inserted Data")

print("temp<=26")
with con:
    data = con.execute("SELECT * FROM DATA WHERE temperature <= 26") #select relevant entries
    for row in data:
        print(row) #print every tuple found

print("hum>=54")
with con:
    data = con.execute("SELECT * FROM DATA WHERE humidity >= 54") #select relevant entries
    for row in data:
        print(row) #print every tuple found
print("Queried the table")