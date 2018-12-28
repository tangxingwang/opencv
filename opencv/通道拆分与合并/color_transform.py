import cv2
import numpy as np
"读取图片"
img = cv2.imread("D://python//opencv2//cat.jpg")
#"通道拆分与合并"
b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]
m = cv2.merge([b,g,r])
zeros = np.zeros(img.shape[:2], dtype = "uint8")
blue = cv2.merge([b, zeros, zeros])
green = cv2.merge([zeros,g,zeros])
red = cv2.merge([zeros,zeros,r])
cv2.imwrite("D://python//opencv2//green_cat.jpg",green)
cv2.imwrite("D://python//opencv2//red_cat.jpg",red)
cv2.imwrite("D://python//opencv2//blue_cat.jpg",blue)
cv2.imshow("blue",blue)
cv2.imshow("green",green)
cv2.imshow("red",red)
cv2.waitKey(0)
cv2.destroyAllWindows()
