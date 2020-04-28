#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:28:52 2020

@author: shashiben
"""
import numpy as np
import cv2

image=np.zeros((512,512,3),np.uint8)
def func(x):
    #To print x coordinate value
    print(x)
cv2.namedWindow("Color Changer")

#Create Trackbars

cv2.createTrackbar("Blue","Color Changer",0,255,func)
cv2.createTrackbar("Green","Color Changer",0,255,func)
cv2.createTrackbar("Red","Color Changer",0,255,func)

while(1):
    #display image
    cv2.imshow("Color Changer",image)
    
    k=cv2.waitKey(1) & 0xFF
    
    # Press esc to close window
    if k==27:
        break
    elif k==ord("s"):
        cv2.imwrite("image.jpeg",image)
    
    #Tracking the trackbars
    b=cv2.getTrackbarPos("Blue","Color Changer")
    g=cv2.getTrackbarPos("Green","Color Changer")
    r=cv2.getTrackbarPos("Red","Color Changer")
    
    #Font for text
    font=cv2.FONT_HERSHEY_TRIPLEX
    
    # changing image colors
    image[:]=[b,g,r]
    
    #Text tto display rgb value
    cv2.putText(image,str((b,g,r)),(25,256),font,1,(255-b,255-g,255-r))
#Destroying all windows    
cv2.destroyAllWindows()
