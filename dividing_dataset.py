import os
import shutil

base_folder = './classified'
all_folders = os.listdir(base_folder)

destination_folder = './re-classified'
destination_folder_train = os.path.join(destination_folder, 'train')
destination_folder_validation = os.path.join(destination_folder, 'validation')
destination_folder_test = os.path.join(destination_folder, 'test')

if(os.path.exists(destination_folder) == True):
    os.rmdir(destination_folder)
os.mkdir(destination_folder)
os.mkdir(destination_folder_train)
os.mkdir(destination_folder_validation)
os.mkdir(destination_folder_test)


destination_folder_all_folders = [
    destination_folder_train, destination_folder_validation, destination_folder_test]


for folder in all_folders:
    if os.path.isdir == False:
        continue
    current_folder = os.path.join(base_folder, folder)

    for Type in destination_folder_all_folders:
        sub_destination_folder = os.path.join(Type, folder)
        if os.path.exists(sub_destination_folder == False):
            os.mkdir(sub_destination_folder)

    counter = 0
    all_files_in_folder = os.listdir(current_folder)
    for File in all_files_in_folder:
        src = os.path.join(current_folder, File)
        if os.path.isfile(src) == False:
            continue

        if counter == 0 or counter == 1:
            dst = os.path.join(destination_folder_train, folder, File)
            shutil.copyfile(src, dst)
            counter += 1
            continue
        elif counter == 2:
            dst = os.path.join(destination_folder_validation, folder, File)
            shutil.copyfile(src, dst)
            counter += 1
            continue
        elif counter == 3:
            dst = os.path.join(destination_folder_test, folder, File)
            shutil.copyfile(src, dst)
            counter = 0
            continue
