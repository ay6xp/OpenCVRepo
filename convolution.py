import cv2
import numpy as np

img = cv2.imread('pikachu.png')

#identity kernel
K = np.array([
   [0,0,0],
   [0,1,0],
   [0,0,0]
])

#sharpening kernel
S = np.array([
   [0,-1,0],
   [-1,5,-1],
   [0,-1,0]
])


#params: image, depth
convolution = cv2.filter2D(img,-1, S)

cv2.imshow('original', img)
cv2.imshow('convolved', convolution)
cv2.waitKey(0)
cv2.destroyAllWindows()
