import os
import cv2
import numpy as np
import random

pathDataSet = 'C:/Users/tanay/Desktop/a/dataset'
k = 7
for f in os.listdir('C:/Users/tanay/Desktop/a/data'):
	if f.endswith('.jpg'):
		name = f[:-4]
		im = cv2.imread(f)
		im = cv2.resize(im,(128,128))
		avg = cv2.blur(im, (k, k))
		gauss = cv2.GaussianBlur(im, (k, k), 2)
		avg = np.concatenate((im, avg), axis=1)
		gauss = np.concatenate((im, gauss), axis=1)
		cv2.imwrite(pathDataSet + '/' + name + '.jpg',avg)
		cv2.imwrite(pathDataSet + '/' + name + 'x.jpg',gauss)
		print(name," done",sep = '')