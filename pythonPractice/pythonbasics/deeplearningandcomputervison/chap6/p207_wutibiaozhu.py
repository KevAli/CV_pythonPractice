# weiwancheng

import cv2
import os
from tkFileDialog import askdirectory
from tkMessageBox import askyesno

WINDOW_NAME = 'Simple Bounding Box Labeling Tool'
FPS = 24
SUPPOTED_FORMATS = ['jpg', 'jpeg', 'png']
DEFAULT_COLOR = {'Obeject': (255, 0, 0)}
COLOR_GRAY = (192, 192, 192)
BAR_HEIGHT = 16

KEV_EMPTY = 0
get_bbox_name = '{}.bbox'.format
