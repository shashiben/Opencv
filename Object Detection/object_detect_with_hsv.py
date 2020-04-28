"""
Created on Tue Apr 28 20:11:37 2020

@author: shashiben
"""
import cv2
import numpy as np

def fun(x):
    pass

#Capture Video
video=cv2.VideoCapture(0)

# Window for trackbar
cv2.namedWindow("Detection")
cv2.createTrackbar("LH","Detection",0,255,fun)
cv2.createTrackbar("LS","Detection",0,255,fun)
cv2.createTrackbar("LV","Detection",0,255,fun)

cv2.createTrackbar("UH","Detection",180,180,fun)
cv2.createTrackbar("US","Detection",255,255,fun)
cv2.createTrackbar("UV","Detection",255,255,fun)


while True:
    
    #Read boolean and frame
    _,frame=video.read()
    
    #Convert it into HSV
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Handle Keyboard events
    key=cv2.waitKey(1) & 0xFF
    if key==27:
        break
    elif key==ord("s"):
        cv2.imwrite("Image.jpeg",frame)
        break
    
    #Get positions of trackbars
    lh=cv2.getTrackbarPos("LH","Detection")
    ls=cv2.getTrackbarPos("LS","Detection")
    lv=cv2.getTrackbarPos("LV","Detection")
    
    uh=cv2.getTrackbarPos("UH","Detection")
    us=cv2.getTrackbarPos("US","Detection")
    uv=cv2.getTrackbarPos("UV","Detection")
    
    #Lower bound of color
    lower_bound=np.array([lh,ls,lv])
    
    #Higher bound of color 
    upper_bound=np.array([uh,us,uv])
    
    #create mask
    mask=cv2.inRange(hsv,lower_bound,upper_bound)
    
    #Bitwise And operation
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    #Display normal frame
    cv2.imshow("Frame", frame)
    
    #Display the mask
    cv2.imshow("Mask",mask)
    
    #Display only the needed color
    cv2.imshow("Result",result)
    
#Release the video
video.release()

#Destroy the windows
cv2.destroyAllWindows()     



