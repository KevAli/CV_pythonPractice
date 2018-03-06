import cv2

img = cv2.imread('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat.jpg')
img_200x200 = cv2.resize(img, (200, 200))
img_200x300 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

print(img.shape)
patch_tree = img[20:320, 50:250]

cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/cropped_tree.jpg', patch_tree)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_200x200.jpg', img_200x200)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_200x300.jpg', img_200x300)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_300x300.jpg', img_300x300)

img_0_100x0_100 = img[100:200, 100:200]
img_0_100xF100_0 = img[100:200, -200:-100]
img_F100_0xF100_0 = img[-200:-100, -200:-100]
img_F100_0x0_100 = img[-200:-100, 100:200]

cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_0_100x0_100.jpg', img_0_100x0_100)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_0_100xF100_0.jpg', img_0_100xF100_0)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_F100_0xF100_0.jpg', img_F100_0xF100_0)
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/p186/img_F100_0x0_1000.jpg', img_F100_0x0_100)

