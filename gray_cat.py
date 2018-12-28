import cv2
img = cv2.imread("D://python//opencv2//cat.jpg")
img1= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('cat1',img)
cv2.imshow('cat',img1)
cv2.imwrite("D://python//opencv2//gray_cat.jpg",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
