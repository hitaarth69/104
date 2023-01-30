import cv2
pot = cv2.imread("poster.jpg")
rocket = pot[120:360,400:500]
pot[0:240,500:600] = rocket
text = "Hitaarth"
cv2.putText(pot, text, (20,200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,255))
cv2.imshow("display", pot)
cv2.waitKey(0)