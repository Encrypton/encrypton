#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
# If this is your first time reading this code, we recommend that you visit our github page at:
# https://github.com/lennymelnik/encrypton and view our readme at
# https://github.com/lennymelnik/encrypton/blob/master/README.md
# Also, sorry about the terrible commenting and organization
#     Your's Truly,
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
# For some reason the clone button does not work
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) ;  print("[ " + time.asctime() + " ]   GP21, IN, Set GPIO.PUD_UP")
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) ;  print("[ " + time.asctime() + " ]   GP20, IN, Set GPIO.PUD_UP")
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
	os.system("sudo rm -rf /media/pi/*")
	# # # # # # # # # # # # # MAIN # # # # # # # # # # # # #


    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/encrypting/insertdrive.png"); print("Please insert your drive")             # # INSERT Drive
	while True:                                                                        # TEMP
		if True: time.sleep(2.0); lcd.clear(); break                                           # DETECT DRIVE MOUNTED:

    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/encrypting/scan_card.png")                                       # # Confirm
    while True:
		if not GPIO.input(16): break
    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/encrypting/press_to_confirm.png")
    rfid = raw_input()
    os.system("sudo rm /home/pi/Encrypton/encrypt0.7z")
    os.system("sudo rm /home/pi/Encrypton/encrypt1.7z")
    os.system("sudo rm /home/pi/Encrypton/encrypt2.7z")

    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/encrypting/encrypting.png")
    os.system("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt.7z /media/usb0/* -p" + rfid)
    os.system("sudo rm -rf /media/usb0/*")
	os.system("sudo mv /home/pi/Encrypton/encrypt.7z /media/usb0/")
	os.system("sudo rm /home/pi/Encrypton/encrypt.7z")

	os.system("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt.7z /media/usb1/* -p" + rfid)
	os.system("sudo rm -rf /media/usb1/*")	
	os.system("sudo mv /home/pi/Encrypton/encrypt.7z /media/usb1/")
	os.system("sudo rm /home/pi/Encrypton/encrypt.7z")

	os.system("7z -mhc=on -mhe=on a /home/pi/Encrypton/encrypt.7z /media/usb2/* -p" + rfid)
	os.system("sudo rm -rf /media/usb2/*")
	os.system("sudo mv /home/pi/Encrypton/encrypt.7z /media/usb2/")
	os.system("sudo rm /home/pi/Encrypton/encrypt.7z")
	
	while periodcount <= 5 and periodover <= 1:                                              # # Loading...
		lcd.clear()
		lcd.message(string + "." * periodcount)
		if periodcount >= 3:
			periodcount = 0
			periodover += 1
		periodcount += 1
		time.sleep(.5)

    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/encrypting/done.png"); print("Your drive has been encrypted")
    main()


def decrypt():
	# # # # # # # # # # VARS # # # # # # # # #
	#flashdir = shutil.make_archive(output_filename, 'zip', dir_name)   # Dir for drive needed here
	string = "Decrypting"                                                                  # For Visual
	periodcount = 0 ; periodover = 0

	# # # # # # # # # # MAIN # # # # # # # # #


    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/decrypting/insert_drive.png"); print("Please insert your drive")
	while True:                                                                 # TEMP
		if True: time.sleep(2.0); lcd.clear(); break                                     # # DETECT DRIVE MOUNTED

    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/decrypting/press_to confirm.png")
    while True:
		if not GPIO.input(21): break
    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/decrypting/scan_card.png")
	rfid = raw_input()
    os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/decrypting/decrypting.png")
	os.system("7z x /media/usb2/encrypt.7z -o/media/usb2/* -p" + rfid)
	os.system("sudo rm /media/usb2/encrypt.7z")
	os.system("7z x /media/usb0/encrypt.7z -o/media/usb0/* -p" + rfid)
	os.system("sudo rm /media/usb0/encrypt.7z")
	os.system("7z x /media/usb1/encrypt.7z -o/media/usb1* -p" + rfid)
	os.system("sudo rm /media/usb1/encrypt.7z")


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
	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/assets/decrypting/decrypted.png"); print("Your drive has been decrypted")
	time.sleep(2.0)
	lcd.clear()
	main()


def clone():
	# VARS
	#flashdir = shutil.make_archive(output_filename, 'zip', dir_name)  # Dir for drive needed here
	string = "Cloning"
	periodcount = 0,
	periodover = 0,
	os.system("sudo umount /media/pi/* | sudo rm -rf /media/pi/*")
	lcd.message("Please insert\ndrive to clone"); print("Please insert drive to clone")
	while True:
		if True: time.sleep(4.0); lcd.clear(); break  # DETECT DRIVE MOUNTED:

	lcd.message("Please insert\noutput drive"); print("Please insert output drive")
	while True:
		if True: time.sleep(4.0); lcd.clear(); break  # DETECT DRIVE MOUNTED:

	lcd.message("Press CLONE \nagain to confirm")                    # CONFIRM
	while True:
		if not GPIO.input(19): 	lcd.clear(); break
	lcd.clear()
	lcd.message("Please scan \n ID Card")
	rfid = raw_input()
	lcd.clear()
	lcd.message("##Cloning")
	os.system("sudo cp -a /media/usb0/* /media/usb1/")


	while periodcount <= 5 and periodover <= 1:
		lcd.message(string + "." * periodcount)
		if periodcount >= 3:
			periodcount = 0
			periodover = + 1
		periodcount += 1
		time.sleep(.5); lcd.clear()
	lcd.clear()
	lcd.message("Done!")
	time.sleep(2.0); lcd.clear()
	lcd.message("Your drive has \nbeen cloned"); print("Your drive has been cloned")
	time.sleep(5.0)
	main()


def main():
	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a encrypton/Logos/1920x1080/1920x1080\ FINAL.png")
	while True:
		encryptButt = GPIO.input(16)
		decryptButt = GPIO.input(21)
		cloneButt = GPIO.input(19)
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
