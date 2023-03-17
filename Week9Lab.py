import RPi.GPIO as GPIO
import datetime
import time

channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

startTime=int(time.time())
iTime=startTime
count = 0
list_of_times = []
list_of_cpm = []
while iTime < (startTime + 5):
 temp = GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 5000)
 if temp is None:
  print("Timeout")
 else:
  count = count + 1
  #print(str(datetime.datetime.now()))
 #GPIO.wait_for_edge(channel, GPIO.FALLING)
 #counts = counts + 1
 #print(str(datetime.datetime.now()))
 list_of_times.append(str(datetime.datetime.now()))
 #time.sleep(0.001)
 iTime = int(time.time())
 if iTime > (start + 60):
  list_of_cpm.append(count)
  count = 0
  start = int(time.time())
 
print("Total Counts:" + str(count))
