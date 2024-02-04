import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')  # generating blank image
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0,255,0  # Green for certain area
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)  # thickness=cv.FILLED or =-1 and (250,250) for location
cv.imshow('Rectangle', blank)


# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)  # start x, stop y
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Can!', (25,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)