import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)

try:
	while True:
		print GPIO.input(24)
		sleep(1)

except KeyboardInterrupt:
	pass

GPIO.cleanup()

