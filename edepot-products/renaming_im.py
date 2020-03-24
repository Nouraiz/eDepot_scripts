import os
import shutil


# Directory paths
root_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020"


for i, folders in enumerate(os.listdir(root_dir)):
    x = 0
    for j, files in enumerate(os.listdir(os.path.join(root_dir, folders))):
        old_file = os.path.join(root_dir, folders, files)
        new_file = os.path.join(root_dir, folders, folders+"-("+str(j)+").jpg")
        #print(old_file, "\n", new_file)
        os.rename(old_file, new_file)
        x += 1
        #shutil.copyfile(new_file, new_file+"("+str(j+3)+")")
        #shutil.copyfile(new_file, new_file+"("+str(j+5)+")")
        #for products in folders:
    print(x, "file(s) renamed.")