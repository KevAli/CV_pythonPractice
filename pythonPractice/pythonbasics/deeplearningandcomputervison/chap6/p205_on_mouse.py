import cv2


def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left button down at({},{})'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('Left button up at({},{})'.format(x, y))
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('Left button double clicked at({},{})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('Right button down at({},{})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        print('Right button up at({},{})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print('Right button double clicked at({},{})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONDOWN:
        print('Middle button down at({},{})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONUP:
        print('Middle button up at({},{})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print('Middle button double clicked at({},{})'.format(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        print('Moving  at({},{})'.format(x, y))


img = cv2.imread('/home/kevin/Desktop/GitSource/OpenCV/chap6/githubcat.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Hello World')
cv2.setMouseCallback('Hello World', on_mouse)
cv2.imshow('Hello World', img)
cv2.waitKey(0)
