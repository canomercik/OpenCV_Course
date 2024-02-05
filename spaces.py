import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)
"""
plt.imshow(img)
plt.show()
"""

# BGR(Blue, Green, Red) to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

# OpenCV uses BGR but other libs like matplotlib uses RGB so u might need convert

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# You can only do these transitions via BGR

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# L*a*b to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('Lab to BGR', lab_bgr)

rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('RGB to BGR', rgb_bgr)
"""
plt.imshow(rgb)
plt.show()
"""
cv.waitKey(0)