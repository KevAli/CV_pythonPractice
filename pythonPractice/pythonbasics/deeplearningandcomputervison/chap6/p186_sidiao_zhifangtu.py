import cv2

img = cv2.imread('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Hello Worold', img)
cv2.waitKey(3000)
