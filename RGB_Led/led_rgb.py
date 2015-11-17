# Script per l'uso dei un LED RGB

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) #BLUE
GPIO.output(18, 1)

GPIO.setup(23, GPIO.OUT) #GREEN
GPIO.output(23, 1)

GPIO.setup(24, GPIO.OUT) #RED
GPIO.output(24, 1)


try:
	while True:
		request = raw_input("Insert an RGB combination: ")
		if(len(request) == 3):
			GPIO.output(24, int(request[0]))
			GPIO.output(23, int(request[1]))
			GPIO.output(18, int(request[2]))

except KeyboardInterrupt:
	GPIO.cleanup()
