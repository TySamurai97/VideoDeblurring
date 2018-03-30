import glob as gb
import os
import numpy as np
import cv2

def format_image(image_path):
    image = cv2.imread(image_path)
    # slice image into full and blur images
    image_blur = image[:,:(image.shape[1])//2]
    image_full = image[:,(image.shape[1])//2:]
    # return the numpy arrays
    return getOneD(image_full), getOneD(image_blur)


def getImages(jpeg_dir,data_type):
    c = 0
    data_path = jpeg_dir + '/%s/*.jpg' % data_type
    images_path = gb.glob(data_path)
    data_full = []
    data_blur = []
    for image_path in images_path:
        image_full, image_blur = format_image(image_path)
        data_full.append(image_full)
        data_blur.append(image_blur)
        c+=1
        print(c,' done',sep = '')
    data_full = np.array(data_full)
    data_blur = np.array(data_blur)
    return data_blur, data_full


if __name__ == '__main__':
    getImages('C:/Users/tanay/Desktop/a','tmp')