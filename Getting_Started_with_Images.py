import cv2 as cv

#First read the image 
image=cv.imread("Demo.jpg",0) # Argument 0 is used to load image in grayscale mode 
#imread() return the image in matrix format
print(image)

cv.imshow("Image",image)

key=cv.waitKey(0) #return key value
#return if esc key pressed (ESC Ascii value is 27)
if key==27: 
  #We have to distroy all the windows created by this program
  cv.destroyAllWindows()

# if we want to save the image press 's'
elif key==ord("s"): 
  cv.imwrite("Demo_copy.png",image)
  cv.destroyAllWindows()
