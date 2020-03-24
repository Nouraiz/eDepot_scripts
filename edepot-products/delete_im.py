import os

# use this script to remove unnecessary files created during testing.

# Directory paths
root_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020"
x = 0

for i, folders in enumerate(os.listdir(root_dir)):
    for j, files in enumerate(os.listdir(os.path.join(root_dir, folders))):
        path = os.path.join(root_dir, folders, files)
        if (files.endswith("5).jpg")):
            os.remove(path)
            x += 1
    print(x, "file(s) removed in ", folders)
    x = 0