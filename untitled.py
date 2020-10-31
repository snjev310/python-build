import numpy as np
import cv2

# reading image
filename = 'vassu.png'
img1 = cv2.imread(filename)

# displaying image

cv2.imshow(filename, img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# display negative
negative = 255 - img1

cv2.imshow('negative image', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()

# write image file

cv2.imwrite('neg.png', negative)

# cropping

subimage1 = img1[0:520, 650:1290]

negative[0:520,650:1290] = subimage1

cv2.imshow('crop image', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()