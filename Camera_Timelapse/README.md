Camera TimeLapse
================



First of all is necessary to enable camera module

```bash
sudo raspi-config
```

and then enable camera


then use this code

```python
import time
import picamera

VIDEO_DAYS = 1
FRAMES_PER_HOUR = 60
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def capture_frame(frame):
	with picamera.PiCamera() as cam:
		time.sleep(2)
		cam.capture('/home/pi/captured_image/frame%03d.jpg' % frame)

# Catturo i vari frames

for frame in range(FRAMES):
	start = time.time()
	capture_frame(frame)
	# Resto in attesa del prossimo frame
	time.sleep(int(60*60/FRAMES_PER_HOUR) - (time.time() - start))

```
