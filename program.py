import numpy as np
import cv2

# reading image
filename = 'emma.png'
img = cv2.imread(filename)

# displaying image

cv2.imshow(filename, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# display negative
neg = 255 - img

cv2.imshow('negative image', neg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# write image file

cv2.imwrite('neg.png', neg)

# cropping

subimage = img[0:520, 650:1290]

neg[0:520,650:1290] = subimage

cv2.imshow('crop image', neg)
cv2.waitKey(0)
cv2.destroyAllWindows()

