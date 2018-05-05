import cv2
import os

image_folder = 'data/small/test'
# video_name = 'vid/generated_video.mp4'
video_name = 'vid/blur_video.mp4'
k = 5
fourcc = cv2.VideoWriter_fourcc(*"XVID")

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width = 128, 128

video = cv2.VideoWriter(video_name, fourcc, 15, (width,height))

for image in images:
	im = cv2.imread(os.path.join(image_folder, image))
	# im = cv2.resize(im,(128,128))
	im = im[:,:128,:]
	im = cv2.GaussianBlur(im, (k, k), 2)
	video.write(im)

cv2.destroyAllWindows()
video.release()