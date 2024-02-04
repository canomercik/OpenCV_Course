import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)  # Normal image

def rescaleFrame(frame, scale=0.75):  # Rescale Function
	# Images, Videos and Live Video
	width = int(frame.shape[1] * scale)
	height = int (frame.shape[0] * scale)

	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)  # Resized image

def changeRes(width, height):
	# Live Video
	capture.set(3,width)
	capture.set(1,height)

# Reading Videos
capture = cv.VideoCapture('Videos/CatVideo.mp4')  # 0,1,2 is cameras

while True:
	isTrue, frame = capture.read()

	frame_resized = rescaleFrame(frame, scale=.2)

	cv.imshow('Video', frame)  # Normal video
	cv.imshow('Video Resized', frame_resized)  # Resized video

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv. destroyAllWindows()

cv.waitKey(0)