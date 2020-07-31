# NOTE: optional python3 script to change the resolution of images to 1000x1000 pixels

from PIL import Image
import os

base_folder = './classified'
all_folders = os.listdir(base_folder)

counter = 0

for folder in all_folders:
    if os.path.isdir == False:
        continue
    current_folder = os.path.join(base_folder, folder)
    all_files_in_folder = os.listdir(current_folder)
    for File in all_files_in_folder:
        src = os.path.join(current_folder, File)
        img = Image.open(src)
        img2 = img.resize((int(1000), int(1000)), Image.BICUBIC)
        img2.save(src)
        counter += 1
        print(counter)
