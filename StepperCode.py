import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
a1 = 17
a2 = 27
b1 = 23
b2 = 22
GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)
def pair_on(pin):
    GPIO.output(pin, GPIO.HIGH)
def pair_off(pin):
    GPIO.output(pin, GPIO.LOW)  
def read(l1):
    if l1[0] == 1:
        pair_on(a1)
    else:
        pair_off(a1)
    if l1[1] == 1:
        pair_on(b1)
    else:
        pair_off(b1)
    if l1[2] == 1:
        pair_on(a2)
    else:
        pair_off(a2)
    if l1[3] ==1:
        pair_on(b2)
    else:
        pair_off(b2)
def full_step_clockwise(n,time = 0.05):
    read([1,1,0,0])
    sleep(time)
    i = 1
    while i <= n:
        if i%4 == 0:
            read([0,1,1,0])
            sleep(time)
        if i%4 == 1:
            read([0,0,1,1])
            sleep(time)
        if i%4 == 2:
            read([1,0,0,1])
            sleep(time)
        if i%4 == 3:
            read([1,1,0,0])
            sleep(time)
        i+=1
def full_step_anticlockwise(n, time = 0.05):
    read([1,1,0,0])
    sleep(.05)
    i = 1
    while i <= n:
        if i%4 == 3:
            read([0,1,1,0])
            sleep(time)
        if i%4 == 2:
            read([0,0,1,1])
            sleep(time)
        if i%4 == 1:
            read([1,0,0,1])
            sleep(time)
        if i%4 == 0:
            read([1,1,0,0])
            sleep(time)
        i+=1
def half_step_clockwise(n, time = 0.05):
    read([1,0,0,0])
    sleep(0.05)
    i=1
    while i <= n:
        if i%8 ==0:
            read([1,1,0,0])
            sleep(time)
        if i%8 == 1:
            read([0,1,0,0])
        if i%8 == 2:
            read([0,1,1,0])
            sleep(time)
        if i%8 == 3:
            read([0,0,1,0])
            sleep(time)
        if i%8 == 4:
            read([0,0,1,1])
            sleep(time)
        if i%8 == 5:
            read([0,0,0,1])
            sleep(time)
        if i%8 ==6:
            read([1,0,0,1])
            sleep(time)
        if i%8 == 7:
            read([1,0,0,0])
            sleep(time)
        i+=1
def half_step_anticlockwise(n, time = 0.05):
    read([1,0,0,0])
    sleep(time)
    i=1
    while i <= n:
        if i%8 ==7:
            read([1,1,0,0])
            sleep(time)
        if i%8 == 6:
            read([0,1,0,0])
            sleep(time)
        if i%8 == 5:
            read([0,1,1,0])
            sleep(time)
        if i%8 == 4:
            read([0,0,1,0])
            sleep(time)
        if i%8 == 3:
            read([0,0,1,1])
            sleep(time)
        if i%8 == 2:
            read([0,0,0,1])
            sleep(time)
        if i%8 ==1:
            read([1,0,0,1])
            sleep(time)
        if i%8 == 0:
            read([1,0,0,0])
            sleep(time)
        i+=1

def bottom_stop():
    pair_off(a1)
    pair_off(a2)
    pair_off(b1)
    pair_off(b2)
#full_step_clockwise(150, 0.01)
#full_step_anticlockwise(400, 0.005)
#half_step_clockwise(400, 0.008)
#half_step_anticlockwise(400, 0.005)

#GPIO.cleanup()
