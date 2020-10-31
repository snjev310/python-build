import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('left.jpg')
img2 = cv2.imread('right.jpg')
img1 = cv2.resize(img1, (0,0), fx=0.35, fy=0.35)
img2 = cv2.resize(img2, (0,0), fx=0.35, fy=0.35)
coordinate_left = list()
coordinate_right = list()

cv2.namedWindow('image')

def clickEventHandler(event, x, y, flags, param):
    global coordinate_left
    if event == cv2.EVENT_LBUTTONDOWN:
        print('new cood in left image ({},{}) recorded'.format(x,y))
        coordinate_left.append([ x, y, 0])
cv2.setMouseCallback('image', clickEventHandler)

while True:
    cv2.imshow('image', img1)
    if cv2.waitKey(20) & 0xFF == 27:
        break

#cv2.destroyAllWindows()
def clickEventHandler(event, X, Y, flags, param):
    global coordinate_right
    if event == cv2.EVENT_LBUTTONDOWN:
        print('new cood in right image ({},{}) recorded'.format(X,Y))
        coordinate_right.append([ X, Y, 1])

cv2.setMouseCallback('image', clickEventHandler)

while True:
    cv2.imshow('image', img2)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

#now we calculate fundamental matrix using point
pts_left = np.int32(coordinate_left)
pts_right = np.int32(coordinate_right)
#F, mask = cv2.findFundamentalMat(pts_left,pts_right,cv2.FM_LMEDS)
F = list()
for (x, y, c), (X, Y,C) in zip(coordinate_left, coordinate_right):
	F.append([X*x,X*y,X,Y*x,Y*y,Y,x,y,1])
F = np.array(F)

print("computing SVD")

u, s, vh = np.linalg.svd(F)

fMat = vh[-1].reshape((3,3))
# pts_left_trans = pts_left.transpose()
# a = np.matmul(np.matmul(np.array(pts_left_trans),fMat),np.array(pts_right))

print(pts_left)
print(pts_right)
print(u)
print(s)
print(vh)

print(F)
print("*"*60)
print(fMat)
print("*"*60)
#print(a)
