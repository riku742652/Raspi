f = open("/sys/class/thermal/thermal_zone0/temp","r")

for t in f:
    print "CPU temp:"+t[:2]+"."+t[2:5] ,

f.close()
