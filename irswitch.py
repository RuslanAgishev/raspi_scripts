import RPi.GPIO as GPIO
import time
import sys

pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

if sys.argv[1]=="big":
    GPIO.output(pin, 1)
else:
    GPIO.output(pin, 0)
