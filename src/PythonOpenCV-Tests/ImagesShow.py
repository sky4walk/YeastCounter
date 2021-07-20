#!/usr/bin/python3
import numpy
import cv2 as cv

print( cv.__version__ )
img = cv.imread("../../Images/unsorted/Yeast1.jpg")
cv.imshow("image show", img)
cv.waitKey()