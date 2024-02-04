import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  # Have to be odd number
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)  # You can reduce the lines by applying blur
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)  # CUBIC(best quality, slowest), LINEAR, AREA(works with making img smaller)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)