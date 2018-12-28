import cv2
import numpy as np
img = cv2.imread("D://python//opencv2//cat.jpg")
cv2.imshow('picture',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matSrc = np.float32([[0,0],[0,height-1],[width-1,0]])
matDst = np.float32([[50,50],[300,height-200],[width-300,100]])
matAffine = cv2.getAffineTransform(matSrc,matDst)
dst = cv2.warpAffine(img,matAffine,(width,height))
cv2.imshow('Affine',dst)
cv2.imwrite("D://python//opencv2//Affine.jpg",dst)
cv2.waitKey(0)