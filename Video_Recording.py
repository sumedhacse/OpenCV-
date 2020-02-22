import cv2 as cv
cap=cv.VideoCapture(0);
#fet code from fcccode.org
fourcc=cv.VideoWriter_fourcc(*'XVID')
op=cv.VideoWriter("Output.avi",fourcc,20.0,(640,480))

print(cap.isOpened())#If file exist then open

while (cap.isOpened()):
  ret,frm=cap.read()
  if ret==True:
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    op.write(frm)
    #to convert video inro gray color use follow
    gray =cv.cvtColor(frm,cv.COLOR_BGR2GRAY)
    cv.imshow("Frame",gray)
    if cv.waitKey(1) & 0xFF ==ord('q'): 
      break
  else:
    break
cap.release()
op.release()
cv.destroyAllWindows()
