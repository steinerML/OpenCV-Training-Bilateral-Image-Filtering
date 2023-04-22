import cv2
import numpy as np

'''We use the bilateralFIlter() function, that takes 4 arguments.
source image, pixel diameter in the neighbourhood, sigmacolor filters sigma in 
the color space, sigmaspace used to filter sigma in coordinate space'''
 
#Read image
image = cv2.imread('test.jpg')

bilateral_filter = cv2.bilateralFilter(src=image, d=10, sigmaColor=55, sigmaSpace=55)
 
cv2.imshow('Original', image)
cv2.imshow('Bilateral Filtering', bilateral_filter)
 
cv2.waitKey(0)
cv2.imwrite('bilateral_filtering.jpg', bilateral_filter)
cv2.destroyAllWindows()