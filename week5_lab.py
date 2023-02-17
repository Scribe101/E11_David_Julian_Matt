"""
import adafruit_bme680

import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
"""
import sys
import random
import time

i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

##################################################

"""
reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)
"""

start_time = int(time.time())
itime = start_time
run_time = 10
if len(sys.argv) > 1:
  run_time = int(sys.argv[1])
  
  
f = open("data2.csv","w")
meta_data = ["Time","PM 1.0","PM2.5","PM10","Temperature","Gas","Humidity","Pressure","Altitude"]
import csv
f = open("data2.csv","w",newline='')
writer = csv.writer(f)
writer.writerow(meta_data)

continuing = True
while continuing:
  """
  try:
    aqdata = pm25.read()
  except RuntimeError:
    print("Unable to read from sensor, retrying...")
    continue
    """
  print()
  itime = time.time()
  print("Time: "+str(itime))
  print("Concentration Units (standard)")
  print("---------------------------------------")
  print(
    "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
    % (random.random(), random.random(), random.random())
  )
  print("Concentration Units (environmental)")
  print("---------------------------------------")
  print(
    "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
    % (random.random(), random.random(), random.random())
  )
  print("---------------------------------------")
  print("Particles > 0.3um / 0.1L air:", random.random())
  print("Particles > 0.5um / 0.1L air:", random.random())
  print("Particles > 1.0um / 0.1L air:", random.random())
  print("Particles > 2.5um / 0.1L air:", random.random())
  print("Particles > 5.0um / 0.1L air:", random.random())
  print("Particles > 10 um / 0.1L air:", random.random())
  print("---------------------------------------")
  
  #############################################
  print("Time: ", time.time(), "\nTemperature: %0.1f C" % bme680.temperature, "  Gas: %d ohm" % bme680.gas, "  Humidity: %0.1f %%" % bme680.relative_humidity, "  Pressure: %0.3f hPa" % bme680.pressure, "  Altitude = %0.2f meters" % bme680.altitude)
  time.sleep(1)
  
  #data = [itime,aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude]
  data = [itime, random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]
  writer.writerow(data)
  if itime > start_time + run_time:
    continuing = False
    f.close()
