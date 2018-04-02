import cv2
import sys
from imutils import paths
import os
import matplotlib.pyplot as plt
# from videotoframe import videoframe

def Face():

	cascPath = "haarcascade_frontalface_default.xml"

	faceCascade = cv2.CascadeClassifier(cascPath)
	
	args = {'humandetected': 'humandetected'}
	
	iterator = 0

	try:
		if not os.path.exists('face'):
			os.makedirs('face')
	except OSError:
		print('Error: Creating directory of face')


	for imagePath in paths.list_images(args["humandetected"]):
	# Read the image
		image = cv2.imread(imagePath)
		print(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


	# Detect faces in the image
		faces = faceCascade.detectMultiScale(
	    	gray,
	    	scaleFactor=1.15,
	    	minNeighbors=3,
	    	minSize=(30, 30)
	    #flags = cv2.CV_HAAR_SCALE_IMAGE
		)

		print("Found {0} faces!".format(len(faces)))



	# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
			print ("face") 
			cv2.imwrite( 'face/' + str(iterator) + '.jpg',image)
			iterator += 1


Face()