import cv2
import numpy as np
canvas = np.zeros([600,600])
canvas[400:500, 350:450] = 255
cv2.imshow("window", canvas)
cv2.waitKey(0)
