import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import misc
from PIL import Image
import binascii
img = cv2.imread('lena512color.jpg',0)
#histo = plt.hist(img.ravel(),256,[0,256]); plt.show()
hist,bins = np.histogram(img.ravel(),256,[0,256])
maxi=0


for i in range(0,256):
	if maxi < hist[i]:
		maxi=hist[i]
		a=i
mini=15654

for j in range(0,256):
	if mini >= hist[j]:
		mini=hist[j]
		b=j

print(hist)
print(a)
print(b)
print(mini)
print(maxi)

lena = misc.imread('Grayscale.png','L')
print(lena.shape)
embed = np.zeros(shape=(512,512))


for i in range(512):
	for j in range(512):
		embed[i][j]=lena[i][j]

#print(embed)

for i in range(512):
	for j in range(512):
		if embed[i][j]>=155 and embed[i][j]<255:
			embed[i,j] = embed[i][j]+1

#print(embed)

strp="hello" #secret message
m =''.join(format(ord(x),'08b') for x in strp)
k=m[0]
print(m)
#print(b[0])
ind=0
def str_to_bin(string):
	l=list(string)
	a=''
	for i in l:
		a=a+format(ord(i),'08b')
	print(a)

str_to_bin("hello")


#print(m)
#print(len(m))

#for i in range(35):
	#print(m[i])
#print(m[0])

for i in range(512):
	for j in range(512):
		if(embed[i][j]==154):
			if ind == len(m)-1:
				break
			if m[ind] == m[1]:
				print('hello')
				ind=ind+1
				embed[i][j]=embed[i][j]+1

			else:
				#print('helo')
				ind=ind+1


				

#print(embed)

imgl= Image.fromarray(embed).convert('L')
imgl.save('my.png')
#imgl.show()














