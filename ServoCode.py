

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)
p=GPIO.PWM(24, 50)
p.start(2)

def serv_ang(deg, t):
  dc=(deg/18)+2
  print(dc)
  p.ChangeDutyCycle(dc)


#GPIO.cleanup()

