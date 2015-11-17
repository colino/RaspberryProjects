import RPi.GPIO as GPIO
import time

BeepPin = 17	# Pin Port

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BeepPin, GPIO.OUT)
	GPIO.output(BeepPin, GPIO.HIGH)	# setta il beeppin ad una corrente di +3.3V)

def loop():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)	# faccio suonare
		time.sleep(0.1)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.1)

def destroy():
	GPIO.output(BeepPin, GPIO.HIGH)	# Spengo il beep
	GPIO.cleanup()			# Rilascio la risorsa

if __name__ == '__main__':
	print 'Press Ctrl+C to end program...'
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
