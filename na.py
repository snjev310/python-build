import cv2
#import logging
filename = ('emma.png')
image=cv2.imread(filename)
coordinates = list()
#logging.basicConfig(filename=("mouse_log78.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
print([i for i in dir(cv2) if 'EVENT' in i])
cv2.namedWindow('image')
img = cv2.imread(filename, cv2.IMREAD_COLOR)
#cv2.imshow(img)
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

with open('coordinate.csv','w') as file:
    for line in coordinates:
        file.write("%s"%line)
        file.write(', ')