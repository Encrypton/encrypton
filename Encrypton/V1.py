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

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lcd_columns = 16      # Define LCD column and row size for 16x2 LCD.
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)



def encrypt():
	# # # # # # # # # # # # # VARS # # # # # # # # # # # # #
	flashdir = shutil.make_archive(output_filename, 'zip', dir_name)                           # Dir for drive needed here
	string = "Encrypting"                                                                      # For Visual
	periodcount = 0 ; periodover = 0

	# # # # # # # # # # # # # MAIN # # # # # # # # # # # # #
	lcd.message("Please insert \nyour drive"); print("Please insert your drive")             # # INSERT Drive
	while True:                                                                        # TEMP
		if True: time.sleep(5.0); lcd.clear(); break                                           # DETECT DRIVE MOUNTED:

	lcd.message("Press ENCRYPT \nagain to confirm")                                          # # Confirm
	while True:
		if not GPIO.input(16): break
    lcd.message("Please scan \n ID Card")
    rfid = raw.input()
    subprocess.call()
	# encryptfile((raw_input, flashdir))                                                      # # ENCRYPTION

	while periodcount <= 5 and periodover <= 1:                                              # # Loading...
		lcd.clear()
		lcd.message(string + "." * periodcount)
		if periodcount >= 3:
			periodcount = 0
			periodover += 1
		periodcount += 1
		time.sleep(.5)

	lcd.message("Done!")
	time.sleep(2.0); lcd.clear()
	lcd.message("Your drive has \nbeen encrypted!"); print("Your drive has been encrypted")
	time.sleep(5.0)
	main()


def decrypt():
	# # # # # # # # # # VARS # # # # # # # # #
	flashdir = shutil.make_archive(output_filename, 'zip', dir_name)   # Dir for drive needed here
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
			periodover = + 1
		periodcount += 1
		time.sleep(.5)

	lcd.message("Done!")
	time.sleep(2.0); lcd.clear()
	lcd.message("Your drive has \nbeen decrypted"); print("Your drive has been decrypted")
	time.sleep(5.0)
	main()


def clone():
	# VARS
	flashdir = shutil.make_archive(output_filename, 'zip', dir_name)  # Dir for drive needed here
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
	encryptButt = GPIO.input(16)
	decryptButt = GPIO.input(19)
	cloneButt = GPIO.input(12)

	lcd.clear()
	lcd.message("Welcome to\n ENCRYPTON")
	while True:
		if not encryptButt: lcd.clear(); encrypt()
		if not decryptButt: lcd.clear(); decrypt()
		if not cloneButt: lcd.clear(); clone()


main()
