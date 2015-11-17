import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

# con PWM dovrei assegnare la porta 23
red = GPIO.PWM(23, 100)

# il led red parte con una intennsita di 100
red.start(100)

pause_time = 0.02

try:
	while True:
		# diminuisco l'intensita
		for i in range(0,101):
			red.ChangeDutyCycle(100 - i)
			sleep(pause_time)
		# aumento l'intensita
		for i in range(0,101):
			red.ChangeDutyCycle(0 + i)
			sleep(pause_time)

except KeyboardInterrupt:
	red.stop()
	GPIO.cleanup()
