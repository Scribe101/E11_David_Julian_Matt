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



 GPIO.setmode(GPIO.BCM)
 GPIO.setup(6, GPIO.IN)
 
try:
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(6, GPIO.IN)
 channel = GPIO.wait_for_edge(channel, GPIO.FALLING, timeout=5000)
 GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)






finally:
    GPIO.cleanup()
 
#GPIO.cleanup()
print("Goodbye!")
