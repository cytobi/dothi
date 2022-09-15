import time
import board
import adafruit_dht
import sqlite3 as sl
import traceback
import sys

import os
from dotenv import load_dotenv

print("Started program")

sensor = adafruit_dht.DHT11(board.D23, use_pulseio=False) #sensor is on gpio 23

load_dotenv() #load the .env file
con = sl.connect(os.getenv("DBPATH")) #connect to database

done = False

currentTimeStr = str(time.ctime(time.time()))
currentTime = int(time.time())
print("Current Time: " + currentTimeStr)

while not done: #retry getting value until fatal error or successful
    try:
        #print the values
        temperature = int(sensor.temperature)
        humidity = int(sensor.humidity)
        print("Temp: " + str(temperature) + " °C, Humidity: " + str(humidity) + "%")
        done = True
 
    except RuntimeError as error:
        #errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue

try:
    sql = 'INSERT INTO DATA (time, temperature, humidity) values(?, ?, ?)' #prepare query
    data = [
        (currentTime, temperature, humidity)
    ] #arrange data
    with con:
        con.executemany(sql, data) #insert data
    print("Inserted values into Database")
except sl.Error as er: #print error (to log) if one occurs
    print('SQLite error: %s' % (' '.join(er.args)))
    print("Exception class is: ", er.__class__)
    print('SQLite traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
except: #all other weird errors
    print("Database Error")
con.close() #clos database connection