# A small script for the raspberry pi to take pictures

import os
from picamera import PiCamera
from time import sleep
camera = PiCamera()

# checking if the directory exists
picture_directory = '/home/pi/rpi_pics'
if(os.path.exists(picture_directory) == False):
    os.mkdir(picture_directory)

index = 0

camera.resolution = (1000, 1000)

camera.start_preview()
sleep(5)

while(True):
    file_name = 'image_' + str(index) + '.jpg'
    file_directory = os.path.join(picture_directory, file_name)
    if(os.path.exists(file_directory)):
        index += 1
    else:
        camera.capture(file_directory)
        print(file_name + ' has just been taken!')
        index += 1
        sleep(3)


camera.stop_preview()
