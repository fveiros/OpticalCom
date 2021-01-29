import cv2
import numpy as np 
from matplotlib import pyplot as plt 

#Import images
image1=cv2.imread("A10.jpg")
image2=cv2.imread("test_photo1.jpg")

#Resize images
image1_resized=cv2.resize(image1,(340,280))
image2_resized=cv2.resize(image2,(340,280))

#Gray scale
image1_gray=cv2.cvtColor(image1_resized,cv2.COLOR_BGR2GRAY)
image2_gray=cv2.cvtColor(image2_resized,cv2.COLOR_BGR2GRAY)

#Threshold
ret, thresh1 = cv2.threshold(image1_gray,90,255,cv2.THRESH_TOZERO)
ret2, thresh2 = cv2.threshold(image2_gray,90,255,cv2.THRESH_TOZERO)

#Difference between patterns
#image3_gray=cv2.add(image1_gray,image2_gray)
difference=cv2.add(image1_resized,image2_resized)

#Subtraction(no DC component)
nodc_1=cv2.subtract(image1_resized,ret)
nodc_2=cv2.subtract(image2_resized,ret2)




#Show images

cv2.imshow("Speckle pattern t=0s",image1_resized)
cv2.moveWindow("Speckle pattern t=0s",0,0)
cv2.imshow("Speckle_pattern t=2s",image2_resized)
cv2.moveWindow("Speckle_pattern t=2s",500,0)
cv2.imshow("image1_gray t=0s",image1_gray)
cv2.moveWindow("image1_gray t=0s",1000,0)
cv2.imshow("image2_gray t=2s",image2_gray)
cv2.moveWindow("image2_gray t=2s",1500,0)
#threshold images
cv2.imshow("Threshold1",thresh1)
cv2.moveWindow("Threshold1",430,500)
cv2.imshow("Threshold2",thresh2)
cv2.moveWindow("Threshold2",805,500)
#Difference between patterns images
cv2.imshow("Difference between patterns",difference)
cv2.moveWindow("Difference between patterns",0,500)
#no DC images
cv2.imshow("No DC component pattern t=0s",nodc_1)
cv2.moveWindow("No DC component pattern t=0s",1180,500)
cv2.imshow("No DC component pattern t=2s",nodc_2)
cv2.moveWindow("No DC component pattern t=2s",4004,500)


key=cv2.waitKey(0) & 0xFF
if key==27:

    cv2.destroyAllWindows()

