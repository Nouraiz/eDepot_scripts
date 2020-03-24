import os
import cv2

# use this script to remove unnecessary files created during testing.

# Directory paths
root_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\new stock march 2020"
x = 0

for i, folders in enumerate(os.listdir(root_dir)):
    for j, files in enumerate(os.listdir(os.path.join(root_dir, folders))):
        path = os.path.join(root_dir, folders, files)
        if files.endswith("0).jpg"):
            print("no change", files)

        if files.endswith("1).jpg") or files.endswith("4).jpg"):
            # print(files)
            img = cv2.imread(path)
            y_start = int(0)
            x_start = int(0 + img.shape[0] * 0.1)
            y_end = int(img.shape[1] * 0.8)
            x_end = int(img.shape[0] * 0.9)
            # print(y_start, x_start)

            crop_img = img[y_start:y_end, x_start:x_end].copy()
            cv2.imwrite(path[0:-4] + "-cropped.jpg", crop_img)
            x += 1
            # cv2.namedWindow("cropped", cv2.WINDOW_NORMAL)
            # cv2.imshow("cropped", crop_img)
            # cv2.resizeWindow("cropped", 600, 600)
            # cv2.waitKey(0)

        if files.endswith("2).jpg") or files.endswith("5).jpg"):
            #print(files)
            img = cv2.imread(path)

            y_start = int(0 + img.shape[1] * 0.5)
            x_start = int(0 + img.shape[0] * 0.5)
            y_end = int(img.shape[1])
            x_end = int(img.shape[0])
            # print(y_start, x_start)

            crop_img = img[y_start:y_end, x_start:x_end].copy()
            cv2.imwrite(path[0:-4]+"-cropped.jpg", crop_img)
            x += 1
            # cv2.namedWindow("cropped", cv2.WINDOW_NORMAL)
            # cv2.imshow("cropped", crop_img)
            # cv2.resizeWindow("cropped", 600, 600)
            # cv2.waitKey(0)
    print(x, "file(s) cropped in ", folders)
    x = 0

