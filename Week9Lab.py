# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
import time
channel = 3
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 
      
channel = GPIO.wait_for_edge(channel, GPIO.RISING, timeout=5000)
try:
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(6, GPIO.IN)
 GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
"""
start = int(time.time())
iTime = start
while(iTime < start + 10):
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(6, GPIO.IN)
 GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
 #channel = GPIO.wait_for_edge(channel, GPIO.RISING, timeout=5000)
 iTime = int(time.time())
 """
"""
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
 
    message = raw_input('\nPress any key to exit.\n')
"""
finally:
    GPIO.cleanup()
 
#GPIO.cleanup()
print("Goodbye!")
