
import guizero
from guizero import App, PushButton, Slider, Picture, Text
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)
#x=.03

def exitApp():
  app.destroy()
  GPIO.cleanup()
    
def toggleLED():
  ledButton.text="LED OFF"
  for i in range (1,10):
    GPIO.output(17, GPIO.HIGH)
    sleep(x)
    GPIO.output(17, GPIO.LOW)
    sleep(x)
  ledButton.text="LED ON"

app = App('KaleidoMnene', bg = "red")
          #width = 160, height = 128)
#picture = Picture(app, image = "title.gif", align = 'top', width =400, height=200)

ledButton = PushButton(app, toggleLED, text="LED ON")
#ledButton.text_size = 36

exitButton = PushButton(app, exitApp, text="Exit", align = 'bottom')
#exitButton.text_size = 36

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
p=GPIO.PWM(17, 50)

def serv_ang(deg, t):
  dc=deg/2
  print(dc)
  p.start(dc)


def slider_changed(slider_value):
  print(slider_value)
  serv_ang(int(slider_value), 1)

#print(theta)


slider = Slider(app, start = 15, end = 90, command=slider_changed)


  
text = Text(app, text="theta")
#picture = Picture(app, image = "JcC.gif")
#picture = Picture(app, image = "y.gif")

app.display()

GPIO.cleanup()
