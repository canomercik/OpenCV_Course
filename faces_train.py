import os
import cv2 as cv
import numpy as np

p = []
DIR = r'C:\Users\Can\Downloads\archive\train'

for i in os.listdir(DIR):
	p.append(i)

print(p)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
	for person in p:
		path = os.path.join(DIR, person)
		label = p.index(person)

		for img in os.listdir(path):
			img_path = os.path.join(path, img)

			img_array = cv.imread(img_path)
			gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

			faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)

			for (x,y,w,h) in faces_rect:
				faces_roi = gray[y:y+h, x:x+w]
				features.append(faces_roi)
				labels.append(label)

create_train()

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

print('Training done ---------------')

features = np.array(features, dtype='object')  # Converting to array
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)  # Training the recognizer on the features and labels

face_recognizer.save('face_trained.yml')  # Saving it for later use

np.save('features.npy', features)
np.save('labls.npy', labels)

