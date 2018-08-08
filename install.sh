#!/bin/bash
#Thanks for installing Encrypton!!
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip
cd Dependencies | sudo pip install RPi.GPIO
sudo python Adafruit_Python_CharLCD/setup.py install
sudo apt-get install exfat-fuse exfat-utils
