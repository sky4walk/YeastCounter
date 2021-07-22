#!/usr/bin/python3
import math
import cv2 as cv
import numpy as np


img = cv.imread("../../Images/unsorted/Yeast1.jpg")
#img = cv.imread("../../Images/unsorted/Yeast2.jpg")
#img = cv.imread("../../Images/unsorted/Yeast3.png")
scalingFactor = 1.0
#scalingFactor = 2.0

img = cv.resize(img, None, fx=scalingFactor, fy=scalingFactor,interpolation=cv.INTER_AREA)
gray = cv.cvtColor(~img, cv.COLOR_BGR2GRAY)

#ret, thresh_gray = cv.threshold(gray, 200, 210, cv.THRESH_BINARY)
thresh_gray = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,10)
#thresh_gray = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

#contours, hierarchy = cv.findContours(thresh_gray, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)[-2:]
#_,contours, hierarchy = cv.findContours(thresh_gray, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

#circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2,20, param1=50,param2=30,minRadius=5,maxRadius=13)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2,15, param1=25,param2=15,minRadius=5,maxRadius=13)
entries = 0
if circles is not None:
  circles = np.round(circles[0, :]).astype("int")
  
  for (x, y, r) in circles:
    entries = entries + 1
    cv.circle(img, (x, y), r, (0, 0, 0), 4)

#print(circles)
print(entries)

cv.imshow('Input', img)
cv.waitKey()