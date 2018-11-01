import cv2
import numpy as np


def canny(image):
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)#changes the 3 color grops to gray only for easy detecetion of edges
    canny = cv2.Canny(gray, 50 ,150)#sets threashold to the low and high and anything inbetween is shown/uses dirivite in all directions
    return canny
image = cv2.imread('ant_one.jpg')
ant_image= np.copy(image)#create a new matrix of the imamge
canny = canny(ant_image)
cv2.imshow("result",canny)#show the image but in gray
cv2.waitKey(0)#infinitely shows image
