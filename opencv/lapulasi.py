import cv2
img = cv2.imread("D://python//opencv2//car_lane.jpg", 0)
gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
laplacian = cv2.convertScaleAbs(gray_lap)
cv2.imshow('laplacian', laplacian)
cv2.imwrite("D://python//opencv2//laplacian.jpg",laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
