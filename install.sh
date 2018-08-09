#!/bin/bash
#Thanks for installing Encrypton!!
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip -y
sudo pip install RPi.GPIO
cd | git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
sudo python Adafruit_Python_CharLCD/setup.py install
sudo apt-get install exfat-fuse exfat-utils -y
sudo apt-get install p7zip-full -y
sudo mkdir /home/pi/Encrypton
sudo apt-get install usbmount
sudo nano /lib/systemd/system/systemd-udevd.service
