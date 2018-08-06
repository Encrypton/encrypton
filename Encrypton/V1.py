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




def encrypt():
	lcd.clear()
	lcd.message("Please insert \nyour drive")
	print("Please insert your drive")
	time.sleep(5.0)	                                           #TEMP
	#lcd.clear()
	#while True:                                               #FIX
	if True:                                                   #TEMP
		if True:                                               #DETECT DRIVE MOUNTED:
			lcd.clear()
			lcd.message("Press ENCRYPT \nagain to confirm")
			while True:
				if GPIO.input(16) == False:
					break
			lcd.clear()
			lcd.message("Encrypting")
			time.sleep(.5)
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting.")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting..")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting...")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting.")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting..")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Encrypting...")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Done!")
			time.sleep(2.0)
			lcd.clear()
			print("Your drive has been encrypted")
			#while True:
			lcd.message("Your drive has \nbeen encrypted!")
			time.sleep(5.0)
			main()


def decrypt():
	lcd.clear()
	lcd.message("Please insert\nyour drive")
	print("Please insert your drive")
	time.sleep(5.0)                                             #TEMP
	# lcd.clear()
	# while True:                                               #FIX
	if True:  # TEMP
		if True:  # DETECT DRIVE MOUNTED:
			lcd.clear()
			lcd.message("Press DECRYPT \nagain to confirm")
			while True:
				if not GPIO.input(19):
					break
			lcd.clear()
			lcd.message("Decrypting")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Decrypting.")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Decrypting..")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Decrypting...")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Decrypting.")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Decrypting..")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Decrypting...")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Done!")
			time.sleep(2.0)
			lcd.clear()
			print("Your drive has been decrypted")
			lcd.message("Your drive has \nbeen decrypted")
			time.sleep(5.0)
			main()
			lcd.clear()
			lcd.message("Your drive has \nbeen decrypted!")
			time.sleep(5.0)
			main()


def clone():
	lcd.clear()
	lcd.message("Please insert\nyour drive")
	print("Please insert your drive")
	time.sleep(5.0)  # TEMP
	# lcd.clear()
	# while True:                                               #FIX
	if True:  # TEMP
		if True:  # DETECT DRIVE MOUNTED:
			lcd.clear()
			lcd.message("Press CLONE \nagain to confirm")
			while True:
				if not GPIO.input(12):
					break
			lcd.clear()
			lcd.message("Cloning")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Cloning.")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Cloning..")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Cloning...")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Cloning.")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Cloning..")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Cloning...")
			time.sleep(0.5)
			lcd.clear()
			lcd.message("Done!")
			time.sleep(2.0)
			lcd.clear()
			print("Your drive has been cloned")
			lcd.message("Your drive has \nbeen cloned")
			time.sleep(5.0)
			main()
			lcd.clear()
			lcd.message("Your drive has \nbeen cloned!")
			time.sleep(5.0)
			main()


def main():
	RSNor = True
	lcd.clear()
	lcd.message("Welcome to\n ENCRYPTON")
	while RSNor == True:
		#lcd.message("Welcome to Encrypton")
		encryptButt = GPIO.input(16)
		decryptButt = GPIO.input(19)
		cloneButt = GPIO.input(12)
		if encryptButt == False:
			#print("pretest1")
			RSNor=False
			#print("Test1")
			encrypt()
		if decryptButt == False:
			#print("pretest2")
			RSNor=False
			#print("test2")
			decrypt()
		if cloneButt == False:
			#print("pretest3")
			RSNor=False
			#print("test3")
			clone()


	#GPIO.add_event_detect(

lcd.clear()
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
