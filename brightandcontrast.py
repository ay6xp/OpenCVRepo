#apply contrast and brightness to an image

import cv2
import numpy as np
img = cv2.imread('pikachu.png')

#image,alpha =  contrast, secondimage matrix full of zeros,dataparam = 0, gamma value = brightness
cb_img = cv2.addWeighted(img, 4, np.zeros(img.shape, dtype=img.dtype),0,100)

cv2.imshow('img',cb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
