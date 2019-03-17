import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
 
    ret, frame = cap.read()

    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    #cv2.namedWindow('test')
    
    cv2.imshow('test',frame)
    #cv2.moveWindow('test',400,200)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()