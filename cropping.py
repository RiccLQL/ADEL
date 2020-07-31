###NOTE to the user: put all the pictures directly taken from the drone and run this python3 script with admin privileges.###
###IMPORTANT: increment the counter so that other pictures dont get overwritten###

from PIL import Image
import os
import shutil

base_folder = './big_pictures'
dest_folder = './new_pictures'
storage_folder = './storage'

counter = 5000

x = [0, 2000]
y = [0, 1000]

for item in os.listdir(base_folder):
    src = os.path.join(base_folder, item)
    print(src)
    img = Image.open(src)
    for j in y:
        for i in x:
            dimensions = (i, j, i+2000, j+2000)
            c = img.crop(box=dimensions)
            d = c.resize((int(1000), int(1000)), Image.BICUBIC)
            d.save(os.path.join(dest_folder, 'image_' +
                                str(counter) + '.jpg'), dpi=(1000, 1000))
            counter += 1
    img.close()
    shutil.copyfile(src, os.path.join(storage_folder, item))
