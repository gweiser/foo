from functions import message, times
from machine import Pin
import utime

set_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
text_button = Pin(4, Pin.IN, Pin.PULL_DOWN)
time_button = Pin(5, Pin.IN, Pin.PULL_DOWN)

def main():
    while True:
        if text_button.value() == True:
            message("foo")
        elif time_button.value() == True:
            times(time_button, set_button)
            

main()