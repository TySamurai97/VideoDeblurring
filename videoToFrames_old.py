import cv2

count = 0
frcnt = 0
h, w = 718, 1280
vidcap = cv2.VideoCapture('a.mp4')
fourcc = cv2.VideoWriter_fourcc(*'WMV1')
video = cv2.VideoWriter('output.mkv', fourcc, 40, (w,h))
for i in range(1000*60*10,1000*60*11,200):
	vidcap.set(cv2.CAP_PROP_POS_MSEC,i)
	success,image = vidcap.read()
	video.write(image)
	print('#',end='')
