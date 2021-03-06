# LED RG (Red Green)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, 1)

try:
	while True:
		request = raw_input("Insert an Red Green combination: ")
		if(len(request) == 2):
			GPIO.output(18, int(request[0]))
			GPIO.output(24, int(request[1]))

except KeyboardInterrupt:
	GPIO.cleanup()
