import cv2

image = cv2.imread("butterfly.jpg")
greyimage= cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("display", greyimage)
cv2.waitKey(0)