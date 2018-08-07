import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
	while True:
		GPIO.input(36)
		if GPIO.input(36) == False:
			print("Button!!")
		#while GPIO.input(36) == False:
			#GPIO.input(36) = GPIO.input(36)

main()
GPIO.cleanup()
