import time
import os
#--------------- main routine ---------------
while 1:
    try:
        os.system('/home/pi/aquestalkpi/AquesTalkPi "good" | aplay')
#        wait_min = random.randint(2, 10)
    except:
        wait_min = 1

#    time.sleep(60 * wait_min)