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
    mask=mask1+mask2
#removing noise from picture = removing small unwanted pixels from the picture, it makes the mask smoother and cleaner to detect specifick colors
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    #cv2.morphologyEx is a functoin of cv2 which works on erosion, dilation, opening, closing
    #cv2.MORPH_OPEN specifuculy works on opening =erosion + dilation
    mask=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)
    #dilation expands white regen in the mask filling the small gaps making the mask smoother
    mask2=cv2.bitwise_not(mask)
    #mask is the cloak area, mask2 is everything exept cloak 

    cloak1=cv2.bitwise_and(bg,bg,mask=mask)
    cloak2=cv2.bitwise_and(img,img,mask=mask2)
    output=cv2.addWeighted(cloak1,1,cloak2,1,0)
    #invisibility effect
    cv2.imshow("invisible man", output)
    key=cv2.waitKey(10)
    if key== 27:
        break
