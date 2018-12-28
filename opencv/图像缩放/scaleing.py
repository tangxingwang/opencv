import cv2
img = cv2.imread("D://python//opencv2//cat.jpg")
img1 = cv2.resize(img, None, fx=1.2,fy=1.4)
cv2.imshow('cat',img)
cv2.imshow('cat1',img1)
cv2.imwrite("D://python//opencv2//scaleing_cat.jpg",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
