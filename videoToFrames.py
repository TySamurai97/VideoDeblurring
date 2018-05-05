import cv2
import numpy as np

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

st = []

def genrateNames():
	for i in l:
		for j in l:
			for k in l:
				st.append( i + j + k )
genrateNames()

vidcap = cv2.VideoCapture('vid/a.mp4')
vidcap.set(cv2.CAP_PROP_POS_MSEC,10000)
s,im = vidcap.read()
w,h = im.shape[:2]
c = 0
k = 5
for i in range(1000*60*0,1000*60*1,200):
	vidcap.set(cv2.CAP_PROP_POS_MSEC,i)
	success,image = vidcap.read()
	image = cv2.resize(image,(128,128))
	image = cv2.GaussianBlur(image, (k, k), 2)
	image = np.concatenate((image, image), axis=1)
	cv2.imwrite('data/small/test/' + str(st[c]) + '.jpg',image)
	c += 1
	print(st[c])
cv2.destroyAllWindows()
vidcap.release()