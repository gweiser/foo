from helpers import welcome, message, times, reasons, love
from machine import Pin
import utime

set_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
text_button = Pin(4, Pin.IN, Pin.PULL_DOWN)
time_button = Pin(5, Pin.IN, Pin.PULL_DOWN)
reasons_button = Pin(6, Pin.IN, Pin.PULL_DOWN)
love_button = Pin(7, Pin.IN, Pin.PULL_DOWN)

def main():
    welcome()
    while True:
        if text_button.value() == True:
            message("foo")
        elif time_button.value() == True:
            times()
        elif reasons_button.value() == True:
            reasons()
        elif love_button.value() == True:
            love()
            

main()
