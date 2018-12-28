import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D://python//opencv2//flower1.jpg')
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = cv2.guidedfilter(img,(5,5),0)
titles = ['Source Image', 'Guassian  Image']
images = [source, result]
for i in range(2):
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()