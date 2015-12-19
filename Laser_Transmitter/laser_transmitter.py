import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

laserStatus = 1

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, laserStatus)

try:
	while True:
		if(laserStatus == 0):
			laserStatus = 1
			print "Laser On"
		else:
			laserStatus = 0
			print "Laser Off"
		GPIO.output(27, laserStatus)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
