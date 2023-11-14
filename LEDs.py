import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
x=.03

def pattern1():
    for i in range (1,10):
        GPIO.output(17, GPIO.HIGH)
        sleep(x)
        GPIO.output(17, GPIO.LOW)
        sleep(x)
