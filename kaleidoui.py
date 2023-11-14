import guizero, StepperCode, ServoCode, LEDs, camcode, Music, threading
from guizero import App, PushButton, Slider, Picture, Text
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
GPIO.setwarnings(False)

x = True
def exitApp():
  app.destroy()
  GPIO.cleanup()

def toggleLED():
  ledButton.text="LED OFF"
  print("test")
  ledButton.text="LED OFF"
  LEDs.pattern1
  #ledButton.text="LED ON"

def Start():
    threading.Thread(target=Turn).start()

def Turn():
  global x
  x = True
  while x:
    StepperCode.full_step_clockwise(100, 0.01)
    if not x:
      break
  
def Stop():
  threading.Thread(target=Stop1).start()

def Stop1():
  global x
  x = False
  print(x)
  
def vid():
  camcode.Video()
  
def pic():
  camcode.Picture()

def music():
  Music.BR()
  
app = App('KaleidoMnene', bg = "red")
          #width = 160, height = 128)
picture = Picture(app, image = "title.gif", align = 'top', width =400, height=200)

ledButton = PushButton(app, toggleLED, text="LED ON")
#ledButton.text_size = 36

exitButton = PushButton(app, exitApp, text="Exit", align = 'bottom')
#exitButton.text_size = 36


turnButton = PushButton(app, text = "Turn Servo")
turnButton.when_clicked = Stop
turnButton.when_double_clicked = Start
VideoButon = PushButton(app, vid, text = "Take Video")

PicButton = PushButton(app, pic, text = "Take Picture")

MusicButton = PushButton(app, music, text = "Bops")

def slider_changed(slider_value):
  print(slider_value)
  ServoCode.serv_ang(int(slider_value), 1)



slider = Slider(app, start = 0, end = 90, command=slider_changed)

  
text = Text(app, text="theta")
picture = Picture(app, image = "JcC.gif")

app.display()

GPIO.cleanup()
