import numpy as np
import matplotlib.pyplot as plt
import cv2


cood = np.array([[369.15774084, 268.00001531,   1.00216612],
 [332.17619462, 277.00001531,   1.00229945],
 [294.19464839, 286.0000153,    1.00243278],
 [253.21310217, 293.0000153,    1.0025661 ],
 [210.23155595, 303.0000153,    1.00269943],
 [368.52834707, 230.00055804,   1.00215445],
 [363.89895331, 187.00110077,   1.00214278],
 [364.26955955, 147.00164351,   1.00213111],
 [359.64016579, 103.00218624,   1.00211944],
 [388.76671018, 276.99999433,   1.00215668],
 [410.37567953, 289.99997335,   1.00214724],
 [433.98464888, 301.99995237,   1.0021378 ],
 [458.59361822, 315.99993139,   1.00212836]])

orig = np.array([ [370 ,	 268], 
[333, 	 277],
[295, 	 286], 	
[254, 	 293],
[211, 	 303], 	 
[369, 	 230], 	 
[364, 	 187], 	 
[364, 	 147], 
[359, 	 103], 	
[390, 	 277], 	 
[412, 	 290], 	 
[436, 	 302], 	 
[461, 	 316]])


img = cv2.imread('calib-object.jpg')
plt.imshow(img)
plt.plot(cood[:,0], cood[:,1], 'ro')
plt.plot(orig[:,0], orig[:,1], 'b+')
plt.show()