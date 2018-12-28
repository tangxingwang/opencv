import cv2
import numpy as np
img = cv2.imread("D://python//opencv2//cat.jpg")
cv2.imshow('picture',img)
imgInfo = img.shape
dst = np.ones(imgInfo,np.uint8)
height = imgInfo[0]
width = imgInfo[1]
for i in range(0,height):
    for j in range(0,width):
        dst[i,j] = img[height-1-i,j]
cv2.imshow('mirroring',dst)
cv2.waitKey(0)
