import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D23, use_pulseio=False)
done = False

while not done:
    try:
        #print the values
        temperature = sensor.temperature
        humidity = sensor.humidity
        print("Temp: " + str(temperature) + " °C, Humidity: " + str(humidity) + "%")
        done = True
 
    except RuntimeError as error:
        #errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue