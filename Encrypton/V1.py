#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
# If this is your first time reading this code, we recommend that you visit our github page at:
# https://github.com/lennymelnik/encrypton and view our readme at
# https://github.com/lennymelnik/encrypton/blob/master/README.md
# Also, sorry about the terrible commenting and organization
#     Your's Truly
#     The Encrypton Team


import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import os
import shutil
import zipfile

import subprocess

print("[ " + time.asctime() + " ]   Imports Complete")

# Raspberry Pi pin setup
lcd_rs = 25 ; print("[ " + time.asctime() + " ]   LCD_RS Pin Setup")
lcd_en = 24 ; print("[ " + time.asctime() + " ]   LCD_EN Pin Setup")
lcd_d4 = 23 ; print("[ " + time.asctime() + " ]   LCD_D4 Pin Setup")
lcd_d5 = 17 ; print("[ " + time.asctime() + " ]   LCD_D5 Pin Setup")
lcd_d6 = 18 ; print("[ " + time.asctime() + " ]   LCD_D6 Pin Setup")
lcd_d7 = 22 ; print("[ " + time.asctime() + " ]   LCD_D7 Pin Setup")
lcd_backlight = 2 ;  print("[ " + time.asctime() + " ]   LCD_BACK Pin Setup")
lcd_columns = 16      # Define LCD column and row size for 16x2 LCD.
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

print("[ " + time.asctime() + " ]   LCD Setup Complete")

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("[ " + time.asctime() + " ]   Button Setup Complete")

def allfiles():
	allFiles = []
	#for root, subfiles, files in os.walk(os.getcwd()):
		#for names in files:
			#allFiles.append(os.path.join(root, names))
	return allFiles



def encrypt():
	# # # # # # # # # # # # # VARS # # # # # # # # # # # # #
	#flashdir = shutil.make_archive(output_filename, 'zip', dir_name)                           # Dir for drive needed here
	string = "Encrypting"                                                                      # For Visual
	periodcount = 0 ; periodover = 0

	# # # # # # # # # # # # # MAIN # # # # # # # # # # # # #
	lcd.message("Please insert \nyour drive"); print("Please insert your drive")             # # INSERT Drive
	while True:                                                                        # TEMP
		if True: time.sleep(5.0); lcd.clear(); break                                           # DETECT DRIVE MOUNTED:

	lcd.message("Press ENCRYPT \nagain to confirm")                                          # # Confirm
	while True:
		if not GPIO.input(16): break
		lcd.clear()
		lcd.message("Please scan \n ID Card")
	rfid = raw.input()
	subprocess.call("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt.7z /media/pi/ -p" + rfid)
	# encryptfile((raw_input, flashdir))                                                      # # ENCRYPTION

	while periodcount <= 5 and periodover <= 1:                                              # # Loading...
		lcd.clear()
		lcd.message(string + "." * periodcount)
		if periodcount >= 3:
			periodcount = 0
			periodover += 1
		periodcount += 1
		time.sleep(.5)

	lcd.clear()
	lcd.message("Done!")
	time.sleep(2.0); lcd.clear()
	lcd.message("Your drive has \nbeen encrypted!"); print("Your drive has been encrypted")
	time.sleep(5.0)
	main()


def decrypt():
	# # # # # # # # # # VARS # # # # # # # # #
	#flashdir = shutil.make_archive(output_filename, 'zip', dir_name)   # Dir for drive needed here
	string = "Decrypting"                                                                  # For Visual
	periodcount = 0 ; periodover = 0

	# # # # # # # # # # MAIN # # # # # # # # #
	lcd.message("Please insert\nyour drive"); print("Please insert your drive")
	while True:                                                                 # TEMP
		if True: time.sleep(5.0); lcd.clear(); break                                     # # DETECT DRIVE MOUNTED

	lcd.message("Press DECRYPT \nagain to confirm")
	while True:
		if not GPIO.input(19): break

	while periodcount <= 5 and periodover <= 1:
		lcd.clear()
		lcd.message(string + "." * periodcount)
		if periodcount >= 3:
			periodcount = 0
			periodover += 1
		periodcount += 1
		time.sleep(.5)
	
	lcd.clear()
	lcd.message("Done!")
	time.sleep(2.0); lcd.clear()
	lcd.message("Your drive has \nbeen decrypted"); print("Your drive has been decrypted")
	time.sleep(5.0)
	main()


def clone():
	# VARS
	#flashdir = shutil.make_archive(output_filename, 'zip', dir_name)  # Dir for drive needed here
	string = "Cloning"
	periodcount = 0,
	periodover = 0

	lcd.message("Please insert\ndrive to clone"); print("Please insert drive to clone")
	while True:
		if True: time.sleep(3.0); lcd.clear(); break  # DETECT DRIVE MOUNTED:

	lcd.message("Please insert\noutput drive"); print("Please insert output drive")
	while True:
		if True: time.sleep(3.0); lcd.clear(); break  # DETECT DRIVE MOUNTED:

	lcd.message("Press CLONE \nagain to confirm")                    # CONFIRM
	while True:
		if not GPIO.input(12): 	lcd.clear(); break

	while periodcount <= 5 and periodover <= 1:
		lcd.message(string + "." * periodcount)
		if periodcount >= 3:
			periodcount = 0
			periodover = + 1
		periodcount += 1
		time.sleep(.5); lcd.clear()
	lcd.message("Done!")
	time.sleep(2.0); lcd.clear()
	lcd.message("Your drive has \nbeen cloned"); print("Your drive has been cloned")
	time.sleep(5.0)
	main()


def main():
	#VARS
	#GPIO.input(16)
	#GPIO.input(19)
	#GPIO.input(12)


	lcd.clear()
	lcd.message("Welcome to\nENCRYPTON")
	while True:
		encryptButt = GPIO.input(16)
		decryptButt = GPIO.input(19)
		cloneButt = GPIO.input(12)
		if encryptButt == False:
			lcd.clear()
			print("[ " + time.asctime() + " ]   ENCRYPT BUTTON")
			encrypt()
		if decryptButt == False:
			lcd.clear()
			decrypt()
		if cloneButt == False: 
			lcd.clear()
			clone()

main()
GPIO.cleanup()
