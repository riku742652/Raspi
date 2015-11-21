#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDPIN = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.output(LEDPIN, True)
time.sleep(2)
GPIO.output(LEDPIN, False)
time.sleep(2)
GPIO.cleanup()
