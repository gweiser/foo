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
        

# Different measurements of how long together
def times(endbtn, setbtn):
    years = 3
    months = 36
    days = 1095
    hours = 26280
    minutes = 1576800
    seconds = 94608000
    
    time = [years, months, days, hours, minutes, seconds]
    
    lcd.clear()
    
    while endbtn.value() == False:
        for i in time:
            while setbtn.value() == False:
                foo = "foo"
            lcd.clear()
            lcd.putint(i)
    
