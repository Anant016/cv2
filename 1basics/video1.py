import numpy as np
import cv2

cap = cv2.VideoCapture(0)

color=(0,255,0)
line_width=2
radius=100
point=(0,0)

def click(event,x,y,flags,param):
    global point, pressed
    if(event==cv2.EVENT_LBUTTONDOWN):
        print("pressed",x,y)
        point=(x,y)

cv2.namedWindow('test')
cv2.setMouseCallback('test',click)

while(True):
 
    ret, frame = cap.read()

    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    #cv2.namedWindow('test')
    cv2.circle(frame,point,radius,color,line_width)
    cv2.imshow('test',frame)
    cv2.moveWindow('test',400,200)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()