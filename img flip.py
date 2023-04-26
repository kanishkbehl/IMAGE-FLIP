import cv2
import numpy as num

img = cv2.imread("sample.jpg")

img_flip = cv2.flip(img,0)      #FLIP ON VERTICAL AXIS
cv2.imshow("window",img_flip)    #SHOW THE IMAGE
cv2.waitKey(0)              #SO THAT IT WAITS ON THE WINDOW

img_flip = cv2.flip(img,1)      #FLIP ON HORIZONTAL AXIS
cv2.imshow("window",img_flip)    #SHOW THE IMAGE
cv2.waitKey(0)              #SO THAT IT WAITS ON THE WINDOW

img_flip = cv2.flip(img,-1)     #FLIP ON BOTH HORIZONTAL AND VERTICAL
cv2.imshow("window",img_flip)    #SHOW THE IMAGE
cv2.waitKey(0)              #SO THAT IT WAITS ON THE WINDOW