import numpy as np
import cv2
f = np.array([[-5.22506847e-06, -1.41561376e-05, -1.07636611e-06],
 [ 3.91682870e-06, -2.82969435e-03, -3.85385679e-04],
 [ 1.98059622e-03, -2.99677804e-03,  9.99989470e-01]])
pts_left=[202,321,1]
pts_right=[9,358,1]
pts_right = np.array(pts_right)
pt=pts_right.transpose()
a = np.matmul(np.matmul(np.array(pt),f),np.array(pts_left))
print(a)