import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

check_state = False


try:
	while True:
	    input_state = GPIO.input(23)
	    if input_state == False:
		GPIO.output(24, GPIO.HIGH)	
	    else:
		GPIO.output(24, GPIO.LOW)

except KeyboardInterrupt:
	GPIO.cleanup()
