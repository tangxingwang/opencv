import cv2
img = cv2.imread("D://python//opencv2//car_lane.jpg", 0)
img1 = cv2.GaussianBlur(img,(3,3),0)
img2 = cv2.Canny(img1,50,150)
cv2.imshow("img",img2)
cv2.imshow("img1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()