from picamera import PiCamera
from time import sleep

camera = PiCamera(sensor_mode=0)

camera.iso = 100
camera.resolution = (640, 480)
camera.framerate = 2
camera.rotation = 180
camera.brightness = 40
camera.exposure_mode = "auto"
camera.zoom = (0, 0.32, 1, 0.48)
camera.video_stabilization = True
camera.start_preview()
sleep(10)
camera.stop_preview()

i = 0
while i < 10000:
    sleep(0.5)
    camera.capture("/home/pi/Desktop/frames/IMG_" + str(i) + ".jpg")
    i += 1

camera.close()