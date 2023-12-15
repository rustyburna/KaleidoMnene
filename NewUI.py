import guizero, StepperCode, Music, threading, LED, camcode, texttest
from guizero import App, PushButton, Slider, Picture, Text
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import tkinter as tk
from tkinter import *
GPIO.setwarnings(False)
from PIL import Image, ImageTk
from itertools import count, cycle
x = True


GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
p=GPIO.PWM(24, 25)
p.start(0)

###########################################################################

def welcome():
  texttest.start()
  
threading.Thread(target=welcome).start()

##############################################################################################################################3

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        self.next_frame()

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

#################################################################################################################################


root = tk.Tk()
root.title("KaleidoMneme UI")

lbl = ImageLabel(root)
lbl.pack()
lbl.load('JcC.gif')

##########################################################################################################################33
def music():
  Music.BR()

def pause():
  Music.end()

def LED1():
    threading.Thread(target=TEST).start()

def TEST():
    LED.one()
    
immersion_frame = LabelFrame(root, text = "Immersion Config",bg="#ccef1b", font="Z003")
immersion_frame.pack()
immersion_frame.place(relx=.2,rely=.785,anchor=CENTER)
led1 = Button(immersion_frame, command = LED1, text="LED 1",font="Quicksand", bg = "#1BCCEF")
led1.pack()
led2 = Button(immersion_frame, text="LED 1", font="Quicksand", bg = "#1BCCEF")
led2.pack()
led3 = Button(immersion_frame, text="LED 1", font="Quicksand", bg = "#1BCCEF")
led3.pack()
musicButton = Button(immersion_frame, command=music, text="Play Music", font="Quicksand", bg = "#1BCCEF")
musicButton.pack()


  

######################################################################################################################

def Start(event):
    threading.Thread(target=Turn).start()

def Turn():
  global x
  x = True
  while x:
    if not x:
      break
    StepperCode.full_step_clockwise(150, 0.01)

  
def Stop(event):
  threading.Thread(target=Stop1).start()

def Stop1():
  global x
  x = False
  print(x)
turnButton = Button(root, text="Spin Display",font="Quicksand", bg = "#1BCCEF")
turnButton.pack()
turnButton.place(relx=.5,rely=.825,anchor=CENTER)
turnButton.bind("<Button-1>", Stop)
turnButton.bind("<Double-1>", Start)
t = Label(root, text="Double click to spin\n Click to stop",bg="#ccef1b", font="Z003")
t.pack()
t.place(relx=.5,rely=.89,anchor=CENTER)
  
######################################################################################################################
def vid():
  camcode.Video()
vidButton = Button(root, command=vid, text="Take Video",font="Quicksand", bg = "#1BCCEF")
vidButton.pack()
vidButton.place(relx=.5,rely=.685,anchor=CENTER)

#########################################################################################################################
def pic():
  camcode.Picture()
  
picButton = Button(root, command = pic, text="Take Picture", font="Quicksand", bg = "#1BCCEF")
picButton.pack()
picButton.place(relx=.8,rely=.685,anchor=CENTER)


##########################################################################################################################
def exitApp():
  serv_ang(0)
  pause()
  GPIO.cleanup()
  root.destroy()

exitButton = Button(root, command = exitApp, text="Exit", bg ='red', highlightcolor="pink")
exitButton.pack(side=TOP)



#####################################################################################################################

def serv_ang(slider_value):
  dc=int(slider_value)/25
  p.ChangeDutyCycle(dc)

w = Scale(root, command = serv_ang, from_=0, to=90, orient=HORIZONTAL, font="Quicksand", bg = "#1BCCEF")
w.pack()
w.place(relx=.8,rely=.825,anchor=CENTER)

t2 = Label(root, text="Mirror Angle (Degrees)",bg="#ccef1b", font="Z003")
t2.pack()
t2.place(relx=.8,rely=.885,anchor=CENTER)

#######################################################################################################################
                                           
root.mainloop()
