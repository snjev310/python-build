import numpy as np
from matplotlib import pyplot as plt
import cv2

img_left = cv2.imread('left.jpg')
img_right = cv2.imread('right.jpg')

left=np.array([[611, 357,   1],
 [490, 337,   1],
 [417, 270,   1],
 [335, 224,   1],
 [300, 195,   1],
 [158, 201,   1],
 [176, 240,   1],
 [194, 259,   1]])
right=np.array([[  5, 434,   1],
 [ 37, 383,   1],
 [132, 354,   1],
 [205, 332,   1],
 [195, 306,   1],
 [151, 323,   1],
 [ 84, 337,   1],
 [ 10, 355,   1]])

F =np.array([[-6.21077734e-07,  5.81516769e-06, -9.95475050e-04],
 [-6.94719170e-06,  2.21914190e-05, -2.59969631e-03],
 [ 2.30873944e-03, -8.07259732e-03,  9.99960876e-01]])
# a = np.matmul(np.matmul(left[1],F),right[1])
# print(a)
L1 = list()
for x in right:
    L1.append(F.dot(x))


L2 = list()
for x in left:
    L2.append(F.dot(x))

# print(L1)
# print(L2)

plt.subplot(1, 2, 1)
plt.imshow(img_left[:,:,[2,1,0]])

xs = np.arange(img_left.shape[1])
#print(xs)
for (A, B, C) in L1:
    ys = ((-A/B) * xs) - (C / B)  
    #print(ys)
    plt.plot(ys)
plt.title('Left image and points')

plt.subplot(1, 2, 2)
plt.imshow(img_right[:,:,[2,1,0]])

xs = np.arange(img_right.shape[1])

for (A, B, C) in L2:
    ys = ((-A/B) * xs) - (C / B)  
    #print(ys)
    plt.plot(ys)
plt.title('Right image and points')
plt.show()


plt.show()