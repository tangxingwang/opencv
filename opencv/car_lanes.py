import cv2
import numpy as np
'读取图片'
car_lines= cv2.imread("D://python//opencv2//car_lane.jpg", 1)
'把读片变成灰度图'
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
'高斯滤波使图像平滑'
def gaussian_blur(img,kernel_size):
    return cv2.GaussianBlur(img,(kernel_size,kernel_size),0)
'canny边缘检测'
def canny(img,low_threshold,high_threshold):
    return  cv2.Canny(img,low_threshold,high_threshold)
'霍夫变换识别直线'
def hough_lines(img, rho, theta, threshold):
    lines = cv2.HoughLinesP(img, rho, theta, threshold)
def line_detect(image):
    gray = grayscale(image)
    kernel_size = 3
    blur_gray = gaussian_blur(gray,kernel_size)
    low_threshold = 50
    high_threshold = 200
    edges = canny(blur_gray,low_threshold,high_threshold)
    rho = 1
    theta = np.pi/180
    threshold = 100
    min_line_length = 100
    max_line_gap = 10
    line_image = hough_lines(edges,rho,theta,threshold)
    return edges,blur_gray,line_image
edges,blur_gray,line_image = line_detect(car_lines)
cv2.imshow("edges",edges)
cv2.imshow("blur_gary",blur_gray)
cv2.imshow("line_image",line_image)
cv2.waitKey(0)

