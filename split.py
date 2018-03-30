import os
import shutil

c = 0
partPath = 'C:/Users/tanay/Desktop/a/data/part'
source = 'C:/Users/tanay/Desktop/a/dataset/'
part = 0

os.mkdir(partPath + str(part) + '/')

for file in os.listdir(source):
	print(c)
	if( c%5000 ==0 ):
		part += 1
		os.mkdir(partPath + str(part) + '/')
	shutil.copy(source + file, partPath + str(part) + '/')
	c += 1