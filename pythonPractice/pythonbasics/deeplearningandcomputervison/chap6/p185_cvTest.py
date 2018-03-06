import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)
plt.imsave('/home/kevin/Desktop/GitSource/OpenCV/chap6/img_pyplot.png', img)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/img_cv2.jpg', img)
