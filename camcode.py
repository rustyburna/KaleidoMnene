from picamera import PiCamera
from time import sleep

camera = PiCamera()

def Video():
    camera.resolution = (1920,1080)
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/tst.h264')
    sleep(20)
    camera.stop_recording()
    camera.stop_preview()
    
    

def Picture():
    camera.resolution = (2592,1944)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/tst.jpg')
    camera.stop_preview()
