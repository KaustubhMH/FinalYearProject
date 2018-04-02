# from __future__ import print_function
# from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
# import argparse
import cv2
import sys
import os
# from face_detection import Face

def Humans(): 
	args = {'videotoframe': 'videotoframe'}
	# print(args)

	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


	try:
		if not os.path.exists('humandetected'):
			os.makedirs('humandetected')
	except OSError:
		print('Error: Creating directory of humandetected')

	# print(0)
	iterator = 0
	for imagePath in paths.list_images(args["videotoframe"]):
		# print(1)
		print(imagePath)
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# print(image)

		(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
		
		# print((type(rects), type(weights)))
		if len(rects) != 0 and len(weights) !=0 :
			
			print ("human")
			cv2.imwrite( 'humandetected/' + str(iterator) + '.jpg',image) #(orig)
			iterator += 1
	# Face()
Humans()