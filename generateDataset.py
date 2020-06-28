# CS542 Final Project
# Sign Language Recognition

# Ben Suffin
# Bo Zhang
# Tyler Reece

# Creates the sign language recognition dataset
# Usage:
#	(0) Ensure you have a ./dataset folder already created.
# 	(1) Enter the letter you want to record (capitalized) Ex. A
#	(2) A video screen will pop up. Make the sign with your hand inside the green box. Try to fill the box up as much as possible.
#	(3) Press Enter to start recording. Slowly rotate/move your hand slightly to generate variations of the sign.
#	(4) Wait until the recording is complete (about 20 seconds).



# Import Modules
import cv2
import os
import sys
import numpy as np
from pathlib import Path

CAM = cv2.VideoCapture(0)
COUNTER = 0
TOTAL_PICS = 1
CAP_FLAG = False
PATH = Path.cwd() / 'newData'
PREPROCESSED_PATH = './newPreprocessed/'



def preprocess():
	letters = os.listdir(PATH)
	for letter in letters:
	    images = os.listdir(os.path.join(str(PATH), letter))
	    os.mkdir(PREPROCESSED_PATH + letter)
	    for i in images:
	        image_path = os.path.join(str(PATH), letter, i)
	        print(image_path)
	        print(image_path)
	        image = cv2.imread(image_path)
	        preprocessed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	        preprocessed_image = cv2.threshold(preprocessed_image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
	        preprocessed_image = cv2.resize(preprocessed_image, (50,50))
	        cv2.imwrite(os.path.join(PREPROCESSED_PATH, letter, i), preprocessed_image)

def captureData():

	letter = input("Please enter a letter to capture (capitalized): \n")
	print("Please hit Enter when you want to start capturing " + letter + "\n")

	path = PATH / letter
	path.mkdir()

	while CAM.isOpened():
	    
	    ret, frame = CAM.read()
	    frame = cv2.flip(frame, 1)
	    cv2.rectangle(frame, (300,300), (100,100), (0,255,0), 0)
	    cv2.imshow("Current Frame", frame)
	    sub_window = frame[100:300, 100:300]
	    grayScaleImg = cv2.cvtColor(sub_window, cv2.COLOR_BGR2GRAY)    
	    model_frame = cv2.threshold(grayScaleImg,210,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
	    cv2.imshow("Model View", model_frame)

	    
	    if CAP_FLAG:
	        COUNTER += 1
	        print("Captured Picture", str(COUNTER), "of", str(TOTAL_PICS))
	        savedImg = cv2.resize(sub_window, (50,50))
	        savedImg = np.array(savedImg)
	        save_path = path / (str(COUNTER) + ".jpg")
	        cv2.imwrite(str(save_path), savedImg)
	    
	    k = cv2.waitKey(1)
	    if COUNTER == TOTAL_PICS:
	        break
	    if k == 27: # ESC Key
	        break
	    elif k == 13: # Enter Key
	        CAP_FLAG = True

	CAM.release()
	cv2.destroyAllWindows()
	cv2.waitKey(1)

if len(sys.argv) != 2:
	print("Not enough arguments - see usage")
elif sys.argv[1] == "capture":
	captureData()
elif sys.argv[1] == "preprocess":
	preprocess()
else:
	print("Incorrect arguments - see usage")
