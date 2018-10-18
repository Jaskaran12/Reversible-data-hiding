import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import misc
from PIL import Image

lena = misc.imread('my.png')
print(lena.shape)
extract = np.zeros(shape=(512,512))

ptr1=0
msg=''

for i in range(512):
	for j in range(512):
		extract[i][j]=lena[i][j]

print(extract)

for i in range(512):
	for j in range(512):
		if ptr1 >40:
			break
		if extract[i][j]==155:
			msg=msg+'1'
			ptr1=ptr1+1
		if extract[i][j]==154:
			msg=msg+'0'
			ptr1=ptr1+1


                       


print(msg)