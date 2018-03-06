import cv2

color_img = cv2.imread('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat.jpg')
print(color_img.shape)
# cv2.imshow('gitcat', color_img)

gray_img = cv2.imread('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat_copygray.jpg', gray_img)
reload_grayscale = cv2.imread('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat_copygray.jpg')
print(reload_grayscale.shape)

cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat_JEPG_QUALITY_90.jpg', color_img,
            (cv2.IMWRITE_JPEG_QUALITY, 80))
cv2.imwrite('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat_PNG_COMPRESSSION_5.jpg', color_img,
            (cv2.IMWRITE_PNG_COMPRESSION, 5))
