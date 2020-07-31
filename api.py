from fastapi import FastAPI, File, UploadFile
from keras.models import load_model


app = FastAPI()
url = "/process/img"

@app.post(url)
async def processimg(image: UploadFile = File('C:/Ricky/Drone/Drone_AI_Vision/Drone_AI_Vision/temp/DJI_0641.JPG')):
    model = load_model("./models/drone_detection.h5")
    print('ez')
    print(model)
    number = model.predict(image)
    print('number: ')
    print(number)
    return number