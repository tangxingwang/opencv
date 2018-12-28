import  cv2
import numpy as np
img = cv2.imread('D://python//opencv2//car_lane.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
detected_edges = cv2.Canny(detected_edges,30,100)
#cv2.imshow('canny demo', detected_edges)
def hough_lines(img, rho, theta, threshold):
    lines = cv2.HoughLinesP(img, rho, theta, threshold
                            )
    dst = cv2.bitwise_and(img, img, mask=lines)  # just add some colours to edges from original image.
    cv2.imshow('canny demo', dst)
cv2.namedWindow('canny demo')
lowThreshold = 0
max_lowThreshold = 200

cv2.createTrackbar('Min threshold', 'hough demo', lowThreshold, max_lowThreshold, hough_lines)
hough_lines(detected_edges,1,np.pi/180,0)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()