import numpy as np
import cv2

sensitivity=150

img = cv2.imread('originale.jpg', 1)
retus=img.copy()

def podebljaj(image): 
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image,kernel,iterations=3)
    image = cv2.bitwise_not(image)
    return (image)

height, width, sat= retus.shape
for x in range(0,height):
         for y in range(0,width):
           if (retus.item(x,y,0))>sensitivity:
             retus.itemset((x,y,0),255)
             retus.itemset((x,y,1),255)
             retus.itemset((x,y,2),255)

rr=podebljaj(retus)
cv2.imwrite("cleaned.jpg",rr)

