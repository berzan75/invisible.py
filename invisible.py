import cv2
import numpy as np
import time 

raw_video=cv2.VideoCapture("C:\\Users\\berza\\OneDrive\\Documenten\\cv\\invisible man\\video.mp4")
time.sleep(1)

count=0
bg=0
for i in range(60):
    return_val,bg=raw_video.read()
    if return_val== False:
        continue
bg=np.flip(bg,axis=1)

while(raw_video.isOpened()):
    return_val,img=raw_video.read()
    if not return_val:
        break
    count+=1
    img=np.flip(img,axis=1)

#hue, saturation, value
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_red=np.array([100,40,40])
    upper_red=np.array([100,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    lower_red2=np.array([155,40,40])
    upper_red2=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)