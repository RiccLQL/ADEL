###NOTE TO THE PERSON CLASSIFYING: you will probably have to press the right button, close the picture window, and then press p to go to the next picture###
###Directives: Put all the new pictures in the new_pictures folder. Run this python3 script with admin privileges###
###The pictures in new_pictures have to be already cropped (using cropping.py)###

import os
import keyboard
import shutil
from time import sleep
from PIL import Image

current_folder = './'
base_folder = os.path.join(current_folder, 'new_pictures')
destination_base_folder = os.path.join(current_folder, 'classified')
if os.path.exists(destination_base_folder) == False:
    os.mkdir(destination_base_folder)

folder_0 = os.path.join(destination_base_folder, '0')
if os.path.exists(folder_0) == False:
    os.mkdir(folder_0)

folder_1 = os.path.join(destination_base_folder, '1')
if os.path.exists(folder_1) == False:
    os.mkdir(folder_1)

folder_2 = os.path.join(destination_base_folder, '2')
if os.path.exists(folder_2) == False:
    os.mkdir(folder_2)

folder_3 = os.path.join(destination_base_folder, '3')
if os.path.exists(folder_3) == False:
    os.mkdir(folder_3)

folder_4 = os.path.join(destination_base_folder, '4')
if os.path.exists(folder_4) == False:
    os.mkdir(folder_4)


base_directory_num_files = 0

for item in os.listdir(base_folder):
    base_directory_num_files += 1

print('number of files: ' + str(base_directory_num_files))

counter = 0

for item in os.listdir(base_folder):
    src = os.path.join(base_folder, item)
    print(src)
    print(str(counter) + '/' + str(base_directory_num_files))
    Image.open(src).show()
    while(True):
        if keyboard.is_pressed('1'):
            dst = os.path.join(folder_0, item)
            shutil.copyfile(src, dst)
            break
        elif keyboard.is_pressed('2'):
            dst = os.path.join(folder_1, item)
            shutil.copyfile(src, dst)
            break
        elif keyboard.is_pressed('w'):
            dst = os.path.join(folder_2, item)
            shutil.copyfile(src, dst)
            break
        elif keyboard.is_pressed('d'):
            dst = os.path.join(folder_3, item)
            shutil.copyfile(src, dst)
            break
        elif keyboard.is_pressed('a'):
            dst = os.path.join(folder_4, item)
            shutil.copyfile(src, dst)
            break
        elif keyboard.is_pressed('g'):
            break
        shutil.copyfile(src, './all_pictures')
        os.remove(src)
    while(True):
        if(keyboard.is_pressed('p')):
            counter += 1
            break
