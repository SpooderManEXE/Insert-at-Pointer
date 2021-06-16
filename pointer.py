import screenpoint
import cv2
import pyscreenshot
import numpy as np
import insertim
def show(img='temp.png'):
	image = cv2.imread(img, 0)
	view = cv2.imread('view.jpg', 0)

	# Project centroid.
	x, y, img_debug = screenpoint.project(view, image, True)
	print(x,y)

	# Write debug image.
	cv2.imwrite('match_debug.png', img_debug)
	insertim.img(x,y,img)
	return x,y
