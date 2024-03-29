import cv2 as cv
import numpy as np

# Boundries of objects

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)  # Recomended
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # LIST return all contours, EXTERNAL only external, TREE hierartical
print(f'{len(contours)} countour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)