import cv2
import numpy as np

img = cv2.imread('D://python//opencv2//car_lane.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gaus = cv2.GaussianBlur(gray, (3, 3), 0)

edges = cv2.Canny(gaus, 50, 150, apertureSize=3)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)

cv2.imshow("houghline", lines)
cv2.waitKey()
cv2.destroyAllWindows()
