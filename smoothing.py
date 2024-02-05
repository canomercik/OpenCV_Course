import cv2 as cv
#Blurring techniques
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Averaging
avarage = cv.blur(img, (3,3))
cv.imshow('Avg Blur', avarage)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur (Cares edges of the image)
bilateral = cv.bilateralFilter(img, 15, 35, 35)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)