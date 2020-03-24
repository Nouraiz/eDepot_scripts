import os
import cv2
# use this script to resize images.

# Directory paths
root_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020"
x = 0

for i, folders in enumerate(os.listdir(root_dir)):
    for j, files in enumerate(os.listdir(os.path.join(root_dir, folders))):
        path = os.path.join(root_dir, folders, files)
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        width = int(999)
        height = int(999)
        dim = (width, height)
        # resize image
        resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA).copy()
        cv2.imwrite(path, resized_img, [cv2.IMWRITE_JPEG_OPTIMIZE, 1, cv2.IMWRITE_JPEG_QUALITY, 80])
        x += 1
    print(x, "file(s) resized in ", folders)
    x = 0