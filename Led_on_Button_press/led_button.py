import Tkinter as tk
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)	
GPIO.output(24, GPIO.LOW)	# Spengo il led

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)

def keypress(event):
        if event.keysym == 'Escape':
		GPIO.cleanup()
                root.destroy()
        x = event.char
        if x == "w":
                print "Hai premuto il tasto w"
		GPIO.output(23, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(23, GPIO.LOW)
        elif x == "s":
                print "Hai premuto il tasto s"
		GPIO.output(24, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(24, GPIO.LOW)
        else:
                print x


root = tk.Tk()
print "Press a key (Escape to exit)"
root.bind_all('<Key>', keypress)

#root.withdraw()
root.mainloop()
