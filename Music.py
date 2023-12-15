import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
pygame.mixer.init()
def BR():
    pygame.mixer.music.load('TestAudio.wav')
    pygame.mixer.music.play()

def end():
    pygame.mixer.music.stop()
