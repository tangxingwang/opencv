import cv2
import numpy as np
img = cv2.imread("D://python//opencv2//car_lane.jpg", 0)
img = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(img, 50, 150)
result = img.copy()
#经验参数
minLineLength = 200
maxLineGap = 15
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):

      lines = cv2.HoughLinesP(canny,1,np.pi/180,80,minLineLength,maxLineGap)
      line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
      draw_lanes(line_img, lines)
      return line_img

for x1,y1,x2,y2 in lines[0]:
	cv2.line(img,(x1,y1),(x2,y2),(255,0,0),20)


def draw_lanes(img, lines, color=[255, 0, 0], thickness=8):
	left_lines, right_lines = [], []
	for line in lines:
		for x1, y1, x2, y2 in line:
			k = (y2 - y1) / (x2 - x1)
			if k < 0:
				left_lines.append(line)
			else:
				right_lines.append(line)

	if (len(left_lines) <= 0 or len(right_lines) <= 0):
		return img
cv2.imshow('Canny',img)
cv2.imwrite("D://python//opencv2//canny.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
