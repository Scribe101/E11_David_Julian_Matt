import RPi.GPIO as GPIO
import datetime
import time

channel = 3 # or maybe 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

i = 0
while i < 10:
 GPIO.wait_for_edge(channel, GPIO.FALLING)
 # timeout
 print(str(datetime.datetime.now()))
 i = i + 1
 time.sleep(0.001)
