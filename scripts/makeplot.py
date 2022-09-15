print("Importing Libraries")

import sqlite3 as sl
import matplotlib.pyplot as plt
import time

import os
from dotenv import load_dotenv

#specify these
sameScale = True #should the two graphs be on the same scale, affects colors and grid
limitYAx = False #should the y-axis display a specified range
yAxLimits = [[0,100],[0,40],[20,80]] #[total, temps, hums]
onlyLastTwoDays = True #should only the last two days be shown on the plot or all

#code
print("Started Program")

load_dotenv()

con = sl.connect(os.getenv("DBPATH"))
print("Connected to Database")

if onlyLastTwoDays:
    currentUnix = int(time.time())
    twoDaysAgoUnix = currentUnix - 172800 #172800 seconds = 2 days
    data = con.execute("SELECT * FROM DATA WHERE time>=" + str(twoDaysAgoUnix)) #terrible but works
else:
    with con:
        data = con.execute("SELECT * FROM DATA") #get relevant entries


unixtimes = [] #list of unix times
times = [] #list of readable times
temps = [] #list of temperatures
hums = []  #list of humidities

#put data into lists for each value
for row in data:
    a, b, c = row #unpack tuple 
    
    #append each value to correct list
    unixtimes.append(a)
    temps.append(b)
    hums.append(c)
print("Parsed response")

#convert unix time to readable time
for entry in unixtimes:
    res = time.localtime(entry) #time struct of relevant time
    if onlyLastTwoDays: #if only last two days are shown we can leave out some of the timestamp
        times.append(time.strftime("%a, %H:%M", res)) #seconds are irrelevant, only 10 min intervals, so always ~ :00
    else:
        times.append(time.strftime("%d.%m.%y, %H:%M", res))
print("Converted Time")


#create graph
ax1 = plt.gca() #get axis
if not sameScale: #when on seperate scales, only temperature for now
    print("Displaying graphs on seperate scales")
    if limitYAx:
        print("Limiting y-axis")
        ax1.set_ylim(yAxLimits[1]) #limit y-axis for first scale
    plt.ylabel("Temperature in °C", color = "darkorange") #label scale in color
    line1 = ax1.plot(times, temps, label = "temperature", color = "darkorange") #plot temperature
else:
    print("Displaying graphs on the same scale")
    if limitYAx:
        print("Limiting y-axis")
        ax1.set_ylim(yAxLimits[0])
    plt.ylabel("°C respectively %")
    ax1.plot(times, temps, label = "temperature") #plot temperature
    ax1.plot(times, hums, label = "humidity") #plot humidity
    ax1.legend() #create legend
    ax1.yaxis.grid() #create grid

#modify ticks
for i, tick in enumerate(ax1.xaxis.get_ticklabels()): #every tick on xaxis, determined by temp scale if seperate (doesn't make a difference because same times)
    if i % 8 != 0: #every 8th not -> every 8th is visible
        tick.set_visible(False) #make invisible
plt.xticks(rotation = 90) #rotate ticks on x axis

if not sameScale: #when on seperate scales, second part with humidity
    ax2 = ax1.twinx() #make twin object for humidity
    if limitYAx:
        ax2.set_ylim(yAxLimits[2]) #limit y-axis for second scale
    plt.ylabel("Humidity in %", color = "deepskyblue") #label scale in color
    line2 = ax2.plot(times, hums, label = "humidity", color = "deepskyblue") #plot humidity


#always/standard stuff
#name axis
plt.xlabel("time")

#title graph
plt.title("Temperature and Humidity Graph")

#specify size
fig = plt.gcf()
fig.set_size_inches(10, 5)

#print to file
plt.savefig(os.getenv(RESULTPATH), bbox_inches='tight', dpi=100)

print("Created Graph")