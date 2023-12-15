import RPi.GPIO as GPIO
import time, threading
from random import seed
from random import randint

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RedPin1 = 10
GreenPin1 = 9
BluePin1 = 11

RedPin2 = 5
GreenPin2 = 6
BluePin2 = 20

RedPin3 = 26
GreenPin3 = 16
BluePin3 = 12

RedPin4 = 7
GreenPin4 = 8
BluePin4 = 25




GPIO.setup(RedPin1, GPIO.OUT)
GPIO.setup(GreenPin1, GPIO.OUT)
GPIO.setup(BluePin1, GPIO.OUT)

GPIO.setup(RedPin2, GPIO.OUT)
GPIO.setup(GreenPin2, GPIO.OUT)
GPIO.setup(BluePin2, GPIO.OUT)

GPIO.setup(RedPin3, GPIO.OUT)
GPIO.setup(GreenPin3, GPIO.OUT)
GPIO.setup(BluePin3, GPIO.OUT)

GPIO.setup(RedPin4, GPIO.OUT)
GPIO.setup(GreenPin4, GPIO.OUT)
GPIO.setup(BluePin4, GPIO.OUT)


red1 = GPIO.PWM(RedPin1,500)
green1 = GPIO.PWM(GreenPin1,500)
blue1 = GPIO.PWM(BluePin1,500)

red2 = GPIO.PWM(RedPin2,500)
green2 = GPIO.PWM(GreenPin2, 500)
blue2 = GPIO.PWM(BluePin2,500)

red3 = GPIO.PWM(RedPin3,500)
green3 = GPIO.PWM(GreenPin3, 500)
blue3 = GPIO.PWM(BluePin3,500)

red4 = GPIO.PWM(RedPin4,500)
green4 = GPIO.PWM(GreenPin4, 500)
blue4 = GPIO.PWM(BluePin4,500)

#for rgb pass in a list. [(led1),(led2),(led3),(led4)] each led is a tuple of values.
def light_one(r,g,b):
    red1.start(r)
    green1.start(g)
    blue1.start(b)
def light_two(r,g,b):
    red2.start(r)
    green2.start(g)
    blue2.start(b)
def light_three(r,g,b):
    red3.start(r)
    green3.start(g)
    blue3.start(b)
def light_four(r,g,b):
    red4.start(r)
    green4.start(g)
    blue4.start(b)
def rgb(l,t=1):
    for i in range(0,len(l)):
        x = []
        for j in range (0,4):
            r = (l[i][j][0]/255)*100
            g = (l[i][j][1]/255)*100
            b = (l[i][j][2]/255)*100
            x += [r,g,b]
        threading.Thread(target = light_one(x[0],x[1],x[2])).start()
        threading.Thread(target = light_two(x[3],x[4],x[5])).start()
        threading.Thread(target = light_three(x[6],x[7],x[8])).start()
        threading.Thread(target = light_four(x[9],x[10],x[11])).start()
        if isinstance(t, list):
            time.sleep(t[i])
        else:
            time.sleep(t)
        red1.stop()
        green1.stop()
        blue1.stop()
        red2.stop()
        green2.stop()
        blue2.stop()
        red3.stop()
        green3.stop()
        blue3.stop()
        red4.stop()
        green4.stop()
        blue4.stop()
    pass

def spin(n,t, color_light = 'red'):
    t1 = [0,5,10,15]
    l_spin = []                                                                                                                                                                                                                        
    for i in range (0,n*4):
        if i == 0:
            a = t1[0]
            b = t1[(i+1)%4]
            c = t1[(i+2)%4]
            d = t1[(i+3)%4]
        else:
            a = t1[i%4]
            b = t1[(i+1)%4]
            c = t1[(i+2)%4]
            d = t1[(i+3)%4]
        if color_light == 'red':
            tup_1  = (a,0,0)
            tup_2 = (b,0,0)
            tup_3 = (c,0,0)
            tup_4 = (d,0,0)
        if color_light == 'green':
            tup_1  = (0,a,0)
            tup_2 = (0,b,0)
            tup_3 = (0,c,0)
            tup_4 = (0,d,0)
        if color_light == 'blue':
            tup_1  = (0,0,a)
            tup_2 = (0,0,b)
            tup_3 = (0,0,c)
            tup_4 = (0,0,d)
        l_mid = [tup_1,tup_2,tup_3,tup_4]
        l_spin.append(l_mid)
    rgb(l_spin,t)
    return l_spin
def frand(n,t):
    l = []
    c =  (0,0,0)
    for i in range(0,n):
        x = randint(1,3)#color
        y = randint(1,255)#intensity
        z = randint(1,4)#which led
        if x == 1:
            tup = (y,0,0)
        elif x ==2:
            tup = (0,y,0)
        elif x ==3:
            tup = (0,0,y)
        if z == 1:
            tot = (tup,c,c,c)
        if z ==2:
            tot = (c,tup,c,c)
        if z ==3:
            tot = (c,c,tup,c)
        if z ==4:
            tot = (c,c,c,tup)
        l.append(tot)
        rgb(l,t)
    return l

def randall(n,t):
    l = []
    c =  (0,0,0)
    for i in range(0,n):
        tot = ()
        for i in range(0,4):
            x= randint(1,3)#color
            y = randint(1,255)#intensity
            if x == 1:
                tup = (y,0,0)
            elif x ==2:
                tup = (0,y,0)
            elif x ==3:
                tup = (0,0,y)
            tot += (tup,)
        l.append(tot)
        rgb(l,t)
    return l
#randall(12,1)

def pairs(n,t,l0, y, colorl = 'blue'): #n is length of run, l0 is list of x which is which pair, y is intensity, color is color
    l = []
    print(colorl)
    for i in range(0,n):
        x = l0[i]
        if isinstance(colorl, list):
            color = colorl[i]
        else:
            color = colorl
        if color == 'blue':
            c = y
        else:
            c = 0
        if color == 'green':
            b = y
        else:
            b=0
        if color == 'red':
            a = y
        else:
            a = 0
        if x == 1:
            tup = ((a,b,c),(a,b,c),(0,0,0),(0,0,0))
        if x == 2:
            tup = ((0,0,0),(a,b,c),(a,b,c),(0,0,0))
        if x == 3:
            tup = ((0,0,0),(0,0,0),(a,b,c),(a,b,c))
        if x == 4:
            tup = ((a,b,c),(0,0,0),(0,0,0),(a,b,c))
        if x == 5:
            tup = ((a,b,c),(0,0,0),(a,b,c),(0,0,0))
        if x == 5:
            tup = ((0,0,0),(a,b,c),(0,0,0),(a,b,c))
        l.append(tup)
    print(l)
    rgb(l,t)
    return
def randall_rainbow(n,t):
    l = []
    for i in range(0,n):
        tot = ()
        for i in range(0,4):
            y1 = randint(1,255)#intensity
            y2 = randint(1,255)
            y3 = randint(1,255)
            tup = (y1,y2,y3)
            tot += (tup,)
        l.append(tot)
        rgb(l,t)
    return l
def breathe(n,t,colorl = 'all'):
    l= []
    for i in range (0,n):
        if isinstance(colorl, list):
            color = colorl[i]
        else:
            color = colorl
        for i in range(0,255,50):
            if color == 'all':
                tup = (i,i,i)
            if color == 'blue':
                tup = (0,0,i)
            if color == 'green':
                tup = (0,i,0)
            if color == 'red':
                tup = (i,0,0)
            a = (tup,tup,tup,tup)
            l.append(a)
    rgb(l,t)
    return

def one():
    pairs(7,1,[1,2,3,4,5,4,5],255, ['green','red','red','blue','red','blue','red'])
    frand(5,.5)
    breathe(10,.5)
    spin(4,.5)
    randall_rainbow(5,.75)
#randall(5,.5)
#breathe(4,.25,colorl = ['all','blue','green','all'])
   
#randall_rainbow(7,[1,1,1,2,4,.5,2])
#rgb([((0,0,255),(0,0,0),(0,0,0),(0,0,0)),((0,0,0),(0,255,0),(0,0,255),(0,255,0)),((255,0,0),(0,0,0),(0,0,0),(255,0,255))],[1,2,3])
#rgb([((0,0,255),(0,0,255),(0,0,255),(255,255,255))],2)
#threading.Thread(target = spin).start()
#threading.Thread(target = rgb).start()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           spin(3,0.5, color_light ='blue')
#rgb([((255,0,0),(255,0,0),(255,0,0),(255,0,0)),((0,255,0),(0,255,0),(0,255,0),(0,255,0)),3])

