import RPi.GPIO as GPIO
import datetime
import time

channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

f = open("data5.csv","w")
meta_data = ["CPM","Time Tags"]
import csv
f = open("data5.csv","w",newline='')
writer = csv.writer(f)
writer.writerow(meta_data)

startTime=int(time.time())
iTime=startTime
count = 0
list_of_times = []
originalStart = int(time.time())

while iTime < (originalStart + 13):
 temp = GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 1000)
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
 if iTime > (startTime + 3):
  data = [str(count),str(list_of_times)]
  writer.writerow(data)
  count = 0
  list_of_times = []
  startTime = int(time.time())
 
print("Total Counts:" + str(count))
f.close()
