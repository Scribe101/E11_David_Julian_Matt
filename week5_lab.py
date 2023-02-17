import sys
import random
import time

start_time = int(time.time())
itime = start_time
run_time = 10
if len(sys.argv) > 1:
  run_time = int(sys.argv[1])


while itime < start_time + run_time:
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
  time.sleep(1)
