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
print("[ " + time.asctime() + " ]   Imports Complete")

# Raspberry Pi pin setup
lcd_rs = 25 ; print("[ " + time.asctime() + " ]   LCD_RS Pin Set")
lcd_en = 24 ; print("[ " + time.asctime() + " ]   LCD_EN Pin Set")
lcd_d4 = 23 ; print("[ " + time.asctime() + " ]   LCD_D4 Pin Set")
lcd_d5 = 17 ; print("[ " + time.asctime() + " ]   LCD_D5 Pin Set")
lcd_d6 = 18 ; print("[ " + time.asctime() + " ]   LCD_D6 Pin Set")
lcd_d7 = 22 ; print("[ " + time.asctime() + " ]   LCD_D7 Pin Set")
lcd_backlight = 2 ;  print("[ " + time.asctime() + " ]   LCD_BACK Pin Set")
lcd_columns = 16 ;   print("[ " + time.asctime() + " ]   LCD_COLUMS Set")
lcd_rows = 2 ;       print("[ " + time.asctime() + " ]   LCD_ROWS Set")
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

print("[ " + time.asctime() + " ]   LCD Setup Complete")

GPIO.setmode(GPIO.BCM) ;  print("[ " + time.asctime() + " ]   GPIO_MODE Set BCM")
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) ;  print("[ " + time.asctime() + " ]   GP16, IN, Set GPIO.PUD_UP")
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) ;  print("[ " + time.asctime() + " ]   GP19, IN, Set GPIO.PUD_UP")
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) ;  print("[ " + time.asctime() + " ]   GP12, IN, Set GPIO.PUD_UP")
print("[ " + time.asctime() + " ]   Button Setup Complete")

fun=0
while fun <= 50:
	print("[ " + time.asctime() + " ]   RAND_THING.CooL_LOOKING")
	fun += 1
	time.sleep(.05)

fun=0
while fun <= 10:
	print("[ " + time.asctime() + " ]   WELCOME TO ENCRYPTON")
	fun += 1
	time.sleep(.05)

def encrypt():
	# # # # # # # # # # # # # VARS # # # # # # # # # # # # #
	string = "Encrypting"                                                                      # For Visual
	periodcount = 0 ; periodover = 0

	# # # # # # # # # # # # # MAIN # # # # # # # # # # # # #
	lcd.message("Please insert \nyour drive"); print("Please insert your drive")             # # INSERT Drive
	while True:                                                                        # TEMP
		if True: time.sleep(2.0); lcd.clear(); break                                           # DETECT DRIVE MOUNTED:

	lcd.message("Press ENCRYPT \nagain to confirm")                                          # # Confirm
	while True:
		if not GPIO.input(16): break
	lcd.clear()
	lcd.message("Please scan \n ID Card")
	rfid = raw_input()
	lcd.clear()
	lcd.message("##Encrypting")
	os.system("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt0.7z /media/pi/MAIN/* -p" + rfid)
	os.system("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt1.7z /media/pi/MAIN1/* -p" + rfid)
	os.system("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt2.7z /media/pi/MAIN2/* -p" + rfid)

	os.system("sudo rm -r /media/pi/MAIN/*")
	os.system("sudo rm -r /media/pi/MAIN1/*")
	os.system("sudo rm -r /media/pi/MAIN2/*")

	os.system("sudo mv /home/pi/Encrypton/encrypt0.7z /media/pi/MAIN/")
	os.system("sudo mv /home/pi/Encrypton/encrypt1.7z /media/pi/MAIN1/")
	os.system("sudo mv /home/pi/Encrypton/encrypt2.7z /media/pi/MAIN2/")
<<<<<<< HEAD:Encrypton/V4.py
	
=======

>>>>>>> d67424914d34b33083944e2dcd4033ff75ee970a:Bin/Versions/V4.py
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
	time.sleep(2.0)
	main()


def decrypt():
	# # # # # # # # # # VARS # # # # # # # # #
	#flashdir = shutil.make_archive(output_filename, 'zip', dir_name)   # Dir for drive needed here
	string = "Decrypting"                                                                  # For Visual
	periodcount = 0 ; periodover = 0

	# # # # # # # # # # MAIN # # # # # # # # #
	lcd.message("Please insert\nyour drive"); print("Please insert your drive")
	while True:                                                                 # TEMP
		if True: time.sleep(2.0); lcd.clear(); break                                     # # DETECT DRIVE MOUNTED

	lcd.message("Press DECRYPT \nagain to confirm")
	while True:
		if not GPIO.input(19): break
	lcd.clear()
	lcd.message("Please scan \n ID Card")
	rfid = raw_input()
	lcd.clear()
	lcd.message("##Decrypting")
	os.system("7z x /media/pi/MAIN/encrypt0.7z -o/media/pi/MAIN/ -p" + rfid)
	os.system("7z x /media/pi/MAIN/encrypt1.7z -o/media/pi/MAIN1/ -p" + rfid)
	os.system("7z x /media/pi/MAIN/encrypt2.7z -o/media/pi/MAIN2/ -p" + rfid)
	os.system("7z x /media/pi/MAIN1/encrypt0.7z -o/media/pi/MAIN/ -p" + rfid)
	os.system("7z x /media/pi/MAIN1/encrypt1.7z -o/media/pi/MAIN1/ -p" + rfid)
	os.system("7z x /media/pi/MAIN1/encrypt2.7z -o/media/pi/MAIN2/ -p" + rfid)
	os.system("7z x /media/pi/MAIN2/encrypt0.7z -o/media/pi/MAIN/ -p" + rfid)
	os.system("7z x /media/pi/MAIN2/encrypt1.7z -o/media/pi/MAIN1/ -p" + rfid)
	os.system("7z x /media/pi/MAIN2/encrypt2.7z -o/media/pi/MAIN2/ -p" + rfid)

	os.system("sudo rm /media/pi/MAIN/encrypt0.7z")
	os.system("sudo rm /media/pi/MAIN/encrypt1.7z")
	os.system("sudo rm /media/pi/MAIN/encrypt2.7z")
	os.system("sudo rm /media/pi/MAIN1/encrypt0.7z")
	os.system("sudo rm /media/pi/MAIN1/encrypt1.7z")
	os.system("sudo rm /media/pi/MAIN1/encrypt2.7z")
	os.system("sudo rm /media/pi/MAIN2/encrypt0.7z")
	os.system("sudo rm /media/pi/MAIN2/encrypt1.7z")
	os.system("sudo rm /media/pi/MAIN2/encrypt2.7z")

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
	time.sleep(2.0)
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
	lcd.clear()
	lcd.message("Please scan \n ID Card")
	rfid = raw_input()
	lcd.clear()
	lcd.message("##Cloning")
	os.system("sudo cp -a /media/pi/MAIN /media/pi/CLONE")
	os.system("sudo cp -a /media/pi/MAIN /media/pi/CLONE1")
	os.system("sudo cp -a /media/pi/MAIN /media/pi/CLONE2")

	os.system("sudo cp -a /media/pi/MAIN1 /media/pi/CLONE")
	os.system("sudo cp -a /media/pi/MAIN1 /media/pi/CLONE1")
	os.system("sudo cp -a /media/pi/MAIN1 /media/pi/CLONE2")
    
	os.system("sudo cp -a /media/pi/MAIN2 /media/pi/CLONE")
	os.system("sudo cp -a /media/pi/MAIN2 /media/pi/CLONE1")
	os.system("sudo cp -a /media/pi/MAIN2 /media/pi/CLONE2")

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

lcd.clear()
main()
GPIO.cleanup()
