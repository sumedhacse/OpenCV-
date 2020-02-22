import numpy as np

import cv2 as cv

img=cv.imread("lena.jpg",1)
#color format is BGR
#To draw line
img=cv.line(img,(50,50),(200,200),(0,0,255),10)
#To draw arrowed line
img=cv.arrowedLine(img,(100,100),(200,300),(0,255,0),10)
#To draw rectange
img=cv.rectangle(img,(150,150),(200,200),(255,0,0),-10)
#To draw circle
img=cv.circle(img,(447,63),63,(255,255,0),-1)
#Put text on image select font settings
font=cv.FONT_HERSHEY_COMPLEX_SMALL

img=cv.putText(img,"SAM",(10,500),font,10,(255,0,100),10,cv.LINE_AA)
cv.imshow("Image",img)
cv.waitKey(0) #return key value
cv.destroyAllWindows()
