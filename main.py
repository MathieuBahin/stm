################################################################################
# ex3
#
################################################################################

import streams
import task as ts
import DTH as dth

# create a serial port with default parameters
streams.serial()

def display(number, delay):
    print(DHT_temp,DHT_hum)
    sleep(delay)

# create the various threads using the same function but passing different parameters        
ts.initTask()
thread(ts.task1,1,500)
thread(ts.task2,2,600)
thread(ts.task3,3,1300)
thread(ts.task4,4,800)

thread(dth.DTH_task, 5, 2500) #time must be more than 2000
thread(display, 6, 1000)
   
