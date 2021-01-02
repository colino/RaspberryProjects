#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 

# infinite loop
while True:
        time.sleep(1)

        msg = ""

        if GPIO.input(channel):
                # Input is high
                msg = str(datetime.datetime.now()) + " - No Water Detected!"
                print msg
        else:
                # Input is low
                msg = str(datetime.datetime.now()) + " - Water Detected!"
                print msg

        f = open("soil_moisture.log", "a")
        f.write(msg)
        f.close()