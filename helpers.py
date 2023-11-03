from machine import Pin, I2C
import utime
import sys

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Paramaters of display
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Declaring display
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


# Heart Symbol
lcd.custom_char(0, bytearray([
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000,
    0b00000,
]))

# Welcome Screen
def welcome():
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putchar(chr(0))
    lcd.move_to(4, 0)
    lcd.putstr("Happiest")
    lcd.move_to(2, 1)
    lcd.putstr("Anniversary")
    lcd.move_to(15, 1)
    lcd.putchar(chr(0))
    
    
def break_str(string):
    # Break a str into enough parts for the lcd to display
    strs = []
    new_strs = []
    counter = 0
    
    # Split str
    for i in string:
        counter += 1
        if counter == 32:
            strs.append(string[:counter])
            string = string[counter:]
            counter = 0
    
    # Add & format new string 
    for s in strs:
        s = s[:16] + "    " + s[16:]
        new_strs.append(s)
        
    # Add rest of string (<32)
    new_strs.append(string)
        

    return new_strs


# Display message
def message(message):
    lcd.clear()
    lcd.move_to(0, 0)
    new_str = break_str(message)
    if len(new_str) > 1:
        for i in new_str:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr(i)
            utime.sleep(3)
    else:
        lcd.clear()
        lcd.putstr(new_str[0])
        

# Different measurements of how long we've been together
def times():
    years = "3"
    months = "36"
    days = "1095"
    hours = "26280"
    minutes = "1576800"
    seconds = "94608000"
    
    time = [("3", "Jahre"), ("36", "Monate"), ("1095", "Tage"), ("26280", "Stunden"), ("1576800", "Minuten"), ("94608000", "Sekunden")]
    
    lcd.clear()
    lcd.move_to(4, 0)
    lcd.putstr("Wir sind \n zusammen seit:")
    utime.sleep(3)
    for i in time:
        lcd.clear()
        lcd.move_to(4, 0)
        lcd.putstr(i[0])
        lcd.move_to(4, 1)
        lcd.putstr(i[1])
        utime.sleep(2)
    lcd.clear()
    lcd.move_to(1, 0)
    lcd.putstr("Die besten \n meines Lebens")
    lcd.move_to(15, 1)
    lcd.putchar(chr(0))
    
    
# Display different reasons for my love
def reasons():
    
    reasons = [
        "wunderschoene \n     Augen",
        "  suessestes \n    Laecheln",
        "  lustigster \n     Mensch",
        "   nettester \n     Mensch",
        "    besten \n     Kuesse",
        "allerschoenste \n      Maus"
        ]
    

    lcd.clear()
    lcd.putstr("Gruende, warum \n ich dich liebe:")
    utime.sleep(3)
    for i in reasons:
        lcd.clear()
        lcd.move_to(1, 0)
        lcd.putstr(i)
        lcd.move_to(15, 1)
        lcd.putchar(chr(0))
        utime.sleep(2.5)
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putchar(chr(0))
    lcd.move_to(2, 0)
    lcd.putstr("Ich habe so \n Glueck mit dir")
    lcd.move_to(15, 1)
    lcd.putchar(chr(0))    


# Declaration of love in different languages 
def love():
    languages = [
        "  I love you",
        "Ich liebe dich",
        "   Je t'aime",
        "    Te amo",
        "0100100101001100\n01011001"
        ]
    
    for i in languages:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putchar(chr(0))
        lcd.move_to(1, 0)
        lcd.putstr(i)
        lcd.move_to(15, 1)
        lcd.putchar(chr(0))
        utime.sleep(2.5)
        
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putchar(chr(0))
    lcd.move_to(5, 0)
    lcd.putstr("Danke")
    lcd.move_to(15, 0)
    lcd.putchar(chr(0))
    lcd.move_to(3, 1)
    lcd.putstr("fuer Alles")
    
def test():
    ...
    
    
test()
