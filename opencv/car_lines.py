import cv2
import numpy as np
'读取图片'
img1= cv2.imread("D://python//opencv2//car_lane.jpg", 1)
'把读片变成灰度图'
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
'高斯滤波使图像平滑'
def gaussian_blur(img,kernel_size):
    return cv2.GaussianBlur(img,(kernel_size,kernel_size),0)
'canny边缘检测'
def canny(img,low_threshold,high_threshold):
    return  cv2.Canny(img,low_threshold,high_threshold)
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img
def weighted_img(img, initial_img, a=0.8, b=1., r=0.):
    return cv2.addWeighted(initial_img, a, img, b, r)
def line_detect(image):
    gary = grayscale(image)
    kernel_size = 9
    blur_gray = gaussian_blur(gary,kernel_size)
    low_threshold = 10
    high_threshold = 150
    edges = canny(blur_gray,low_threshold,high_threshold)
    imshape = image.shape
    vertices = np.array([[(0,imshape[0]),(int(0.45*imshape[1]),int(0.6*imshape[0])),
                          (int(0.6*imshape[1]),int(0.6*imshape[0])), (imshape[1],imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges,vertices)
    rho = 1
    theta = np.pi/180
    threshold = 30
    min_line_length = 150
    max_line_gap = 100
    line_image = hough_lines(masked_edges,rho,theta,threshold,min_line_length,max_line_gap)
    result = weighted_img(line_image,image, a=0.8, b=1.)
    return edges,masked_edges,result,line_image
edges,masked_edges,result,line_images = line_detect(img1)
cv2.imshow('car_lines',result)
cv2.imshow("edges",edges)
cv2.imshow("masked_edges",masked_edges)
cv2.imshow("line_image",line_images)
cv2.waitKey(0)
cv2.destroyAllWindows()






