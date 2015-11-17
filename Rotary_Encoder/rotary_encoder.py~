import RPi.GPIO as GPIO


### Config
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

# check initial state
oldPinA = GPIO.input(23)
index = 0
inc = 5		# increment unit
REmax = 127	# max value
REmin = 0	# min value


while True:
	encoderPinA=GPIO.input(23)
	encoderPinB=GPIO.input(24)
	if(encoderPinA == True) and (oldPinA==False):
		if(encoderPinB == False):
			index = index + inc
			if index > REmax:		# max limit value
				index = REmax
		else:
			index = index-inc		# anticlockwise
			if index < REmin:
				index = REmin
		print index

	oldPinA=encoderPinA



