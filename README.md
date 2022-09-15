# dothi
A collection of python scripts for logging and visualizing temperature and humidity trends on a Raspberry Pi using a DHT11. The scripts use python's built in SQLite database for data management and matplotlib to create nice graphs.

## Install

Use [pip](https://pip.pypa.io/en/stable/) to install dependencies:
- dotenv
```bash
python3 -m pip install -U python-dotenv
```
- board
```bash
python3 -m pip install -U board
```
- adafruit_dht
```bash
python3 -m pip install -U adafruit_dht
```
- matplotlib
```bash
python3 -m pip install -U matplotlib
```


## Hardware setup

### Pinout

![pinout of the DHT11](https://cdn.discordapp.com/attachments/712262169819086930/1019937097882279996/unknown.png)

The pinout of the DHT11. GND is ground, NC isn't used, Data will be connected to a GPIO Pin of your choice & VCC should be connected to 3.3V power.

### Circuit

![circuit layout](https://cdn.discordapp.com/attachments/712262169819086930/1019938735103676486/unknown.png)

Connect the DHT11 like this to your Raspberry Pi. I used a 10kΩ resistor. You can connect the Data pin (blue wire) to any GPIO Pin you like. In the picture it is connected to GPIO 4, however the scripts assume the sensor is connected to GPIO 23. You can change this by changing ```board.D23``` to ```board.D4``` wherever you find sensor declarations like:
```python
sensor = adafruit_dht.DHT11(board.D23, use_pulseio=False) #sensor is on gpio 23
```

### GPIO Pins

To find the correct GPIO Pin refer to this picture:

![GPIO Pins](https://cdn.discordapp.com/attachments/712262169819086930/1019937746703372419/unknown.png)

### Alternative sensor

![alternative sensor](https://cdn.discordapp.com/attachments/712262169819086930/1019939213875089428/unknown.png)

You may also have a DHT11 like this. It already includes a 10kΩ resistor, spares the NC and Data is called DOUT here.

## Usage

Create a .env file in the scripts directory (it won't be tracked) and include the following environment variables:
```
DBPATH=absolute-path-to-the-parent-directory-of-dothi/dothi/database/ambient.db
RESULTPATH=absolute-path-to-the-parent-directory-of-dothi/dothi/results/graph.png
```
The paths should be absolute, so that you can call the scripts from crontabs.

Now you're ready to manually or automatically call the scripts and start logging and visualizing ambient temperature and humidity.

## Contributors
- [cytobi](https://github.com/cytobi)

## License

[MIT](https://choosealicense.com/licenses/mit/)
