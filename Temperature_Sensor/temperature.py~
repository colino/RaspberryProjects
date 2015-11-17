import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-000006c7b002/w1_slave'

# read row data

def temp_raw():
	f=open(temp_sensor,'r')
	lines=f.readlines()
	f.close()
	return lines

# parse row data

def read_temp():
	lines=temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines=temp_raw()

# get temperature output
# we can find it at this row 74 01 4b 46 7f ff 0c 10 55 t=23250
# t=23250

	temp_output = lines[1].find('t=')

	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string)/1000.0	# Celsius
		temp_f = temp_c * 9.0 / 5.0 + 32.0	# Fahrenheit
		return 'Celsius: ' + str(temp_c) + '°C', 'Fahrenheit: ' + str(temp_f) + '°F'

while True:
	print(read_temp())
	time.sleep(1)


	
