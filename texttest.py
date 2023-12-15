import I2C_LCD_driver, threading
from time import *
mylcd = I2C_LCD_driver.lcd()
str_pad = " " * 16
string = "Welcome to KaleidoMneme"
string = str_pad + string

mylcd.lcd_display_string("Be Enchanted", 2,2)

def start():
    while True:
        for i in range (0, len(string)):
            lcd_text = string[i:(i+16)]
            mylcd.lcd_display_string(lcd_text,1)
            sleep(.4)
            mylcd.lcd_display_string(str_pad,1)
        for i in range (5):
            sleep(.3)
            mylcd.lcd_clear()
            sleep(.3)
            mylcd.lcd_display_string("Be Enchanted", 2,2)



