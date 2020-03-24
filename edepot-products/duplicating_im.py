import os
import shutil


# Directory paths
root_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020"
x = 0

for i, folders in enumerate(os.listdir(root_dir)):
    for j, files in enumerate(os.listdir(os.path.join(root_dir, folders))):
        x = j
        path = os.path.join(root_dir, folders, files)
        shutil.copyfile(path, path+"copy("+str(j+1)+")")
        shutil.copyfile(path, path+"copy("+str(j+2)+")")
    print(x, "file(s) duplicated in ", folders)