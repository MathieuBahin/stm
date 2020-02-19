################################################################################
# ex3
#
################################################################################

import streams
import task as ts

# create a serial port with default parameters
streams.serial()



# create the various threads using the same function but passing different parameters        
ts.initTask()
thread(ts.task1,1,500)
thread(ts.task2,2,600)
thread(ts.task3,3,1300)
thread(ts.task4,4,800)

   
