#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
GPIO.output(22,True)
GPIO.output(23,True)
GPIO.output(24, True)
time.sleep(2)
GPIO.output(24, False)
time.sleep(2)
