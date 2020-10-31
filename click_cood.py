import numpy as np
import cv2

filename = 'aquaman.png'

coordinates = list()

print([i for i in dir(cv2) if 'EVENT' in i])
cv2.namedWindow('image')
img = cv2.imread(filename, cv2.IMREAD_COLOR)

def clickEventHandler(event, x, y, flags, param):
	global coordinates
	if event == cv2.EVENT_LBUTTONDOWN:
		print('new cood ({},{}) recorded'.format(x,y))
		coordinates.append([x,y])

cv2.setMouseCallback('image', clickEventHandler)

while True:
	cv2.imshow('image', img)
	if cv2.waitKey(20) & 0xFF == 27:
		break
cv2.destroyAllWindows()
print(coordinates)