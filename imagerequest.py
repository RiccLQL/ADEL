import requests
import os
from PIL import Image

class ImageRequest:
    def __init__(self):
        pass

    def processimage(self, pathtofile):

        img = Image.open(pathtofile)

        x,y = img.size

        if x < y:
            croplimit = (y - x)/2
            dimensions = (0, x, croplimit, croplimit+x)
            c = img.crop(box=dimensions)
            img = c.resize((int(1000), int(1000)), Image.BICUBIC)
        elif y < x:
            croplimit = (x - y)/2
            dimensions = (croplimit, croplimit+y, 0, y)
            c = img.crop(box=dimensions)
            img = c.resize((int(1000), int(1000)), Image.BICUBIC)
        else:
            img = img.resize((int(1000), int(1000)), Image.BICUBIC)

        img.save('C:/Ricky/Drone/Drone_AI_Vision/Drone_AI_Vision/temp/DJI_0641.JPG', dpi=(1000, 1000))
        #headers = {"Content-Type":"multipart/form-data"}
        url = "http://localhost:8000/process/img"
        file = {'media': open('C:/Ricky/Drone/Drone_AI_Vision/Drone_AI_Vision/temp/DJI_0641.JPG', 'rb')}
        print(file['media'].name)
        number = requests.post(url, files=file)
        print(number.status_code)
        print(number.text)
        #os.remove('C:/Ricky/Drone/Drone_AI_Vision/Drone_AI_Vision/temp/DJI_0641.JPG')
        return number
