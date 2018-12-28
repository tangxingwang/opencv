import cv2
import numpy as np
img = cv2.imread("D://python//opencv2//cat.jpg")
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dst = np.zeros((height,width,1),np.uint8)

for i in range(0,height):
    for j in range(0,width):
        dst[i,j] = 255 - gray[i,j]

cv2.imshow('picture',gray)
cv2.imshow('cat',dst)
cv2.waitKey(0)