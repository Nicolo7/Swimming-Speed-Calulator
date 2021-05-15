'''
  This file serves the purpose of displaying the speed and other information on a 16x2 LCD screen.
  I am using an OSEPP 16x2 LCD screen. I am following the guide found on this link (https://pimylifeup.com/raspberry-pi-lcd-16x2/).
  The following code is tweaked from the github repository found from the link provided above.
'''

#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD

lcd_rs        = 25 
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

class SwimLCD():
    
    def __init__(self):
        
        # Initialize the LCD using the pins above.
        self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                   lcd_columns, lcd_rows, lcd_backlight)
    
    def lcdShowMessage(self, firstline, secondline):
        message = firstline
        message += '\n'
        message += 'secondline'
        self.lcd.message(message)
        return message
        
    def showLcdCursor(self):
        self.lcd.show_cursor(True)
        
    def blinkLcdCursor(self):
        self.lcd.blink(True)
        
    def staticLcdCursor(self):
        self.lcd.blink(False)
    
    def hideLcdCursor(self):
        self.lcd.show_cursor(False)
        
    def clearLcd(self):
        self.lcd.clear()
        
    def scrollRight(self, firstline, secondline):
        message = self.lcdShowMessage(firstline, secondline)
        
        for i in range(lcd_columns-len(message)):
            time.sleep(0.5)
            self.lcd.move_right()
            
    def scrollLeft(self, firstline, secondline):
        message = self.lcdShowMessage(firstline, secondline)
        
        for i in range(lcd_columns-len(message)):
            time.sleep(0.5)
            self.lcd.move_left()
