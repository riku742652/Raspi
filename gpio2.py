#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT)

GPIO.output(24, True)
time.sleep(2)
GPIO.output(24, False)
time.sleep(2)
