import numpy as np
import cv2 as cv

img=cv.imread("messi5.jpg")
img2=cv.imread("opencv-logo.png")

print(img.size)
print(img.shape)
print(img.dtype)
 
b,g,r=cv.split(img)
img=cv.merge((b,g,r))
#create copy of ball & paste it to another location
ball=img[280:340,330:390]
#assign new locatio to ball
img[273:333,100:160]=ball 
img=cv.resize(img,(512,512))

#After adding ball to other place, display the image
cv.imshow("Image",img)
#Add ome more image on messi5 image 
img2=cv.resize(img2,(512,512))
dst1=cv.add(img,img2);
dst=cv.addWeighted(img,.2,img2,.1,0)
cv.imshow("Image2",dst)


cv.waitKey(0)
cv.destroyAllWindows()
