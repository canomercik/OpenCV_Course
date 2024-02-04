import cv2 as cv

'''
# Reading Images

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)  # Displays the image in new window

cv.waitKey(0)

# 'py read.py' to the console

'''
# Reading Videos

capture = cv.VideoCapture('Videos/CatVideo.mp4')  # 0,1,2 is cameras

while True:
	isTrue, frame = capture.read()

	cv.imshow('Video', frame)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv. destroyAllWindows()

