import cv2
img = cv2.imread("D://python//opencv2//cat.jpg")
img1= cv2.flip(img, flipCode=1)
cv2.imshow('cat',img)
cv2.imshow('cat1',img1)
cv2.imwrite("D://python//opencv2//flip.jpg",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
