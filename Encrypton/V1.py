#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import os
import shutil
# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# VARIABLES

lcd.message("Welcome to\nENCRYPTON!")


def Encrypt():
	lcd.clear()
	lcd.message("Please insert \nyour drive")
		while true:
			if os.path.ismount(
	lcd.message("Your drive has \nbeen encrypted!")

def Decrypt():
	lcd.clear()
	lcd.message("Your drive has \nbeen decrypted!")
def Clone():
	lcd.clear()
	lcd.message("Your drive has\nbeen cloned!")
def main():
	RSNor = True
	while RSNor == True:
		encryptButt = GPIO.input(16)
		decryptButt = GPIO.input(19)
		cloneButt = GPIO.input(12)
		if encryptButt == False:
			#print("pretest1")
			RSNor=False
			#print("Test1")
			Encrypt()
		if decryptButt == False:
			#print("pretest2")
			RSNor=False
			#print("test2")
			Decrypt()
		if cloneButt == False:
			#print("pretest3")
			RSNor=False
			#print("test3")
			Clone()


	#GPIO.add_event_detect(
main()

# Wait 5 seconds

#time.sleep(5.0)
#lcd.clear()
#text = raw_input("Type Something to be displayed: ")
#lcd.clear()
#lcd.message(text)

# Wait 5 seconds
#time.sleep(5.0)
#lcd.clear()
#lcd.message('Your drive has\nbeen encrypted')

#time.sleep(5.0)
#lcd.clear()
