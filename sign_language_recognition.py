import cv2
import os
import sys
import pathlib
import numpy as np
from keras.models import load_model

MODEL_PATH = "./alphabet_model_5000.h5"
model = load_model(MODEL_PATH)
CLASSES = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'K',
    11:'L',
    12:'M',
    13:'N',
    14:'O',
    15:'P',
    16:'Q',
    17:'R',
    18:'S',
    19:'T',
    20:'U',
    21:'V',
    22:'W',
    23:'X',
    24:'Y',
}

def predict(cl):
    image = cv2.resize(cl, (50,50))
    image = image.reshape(1,50,50,1)
    image = image / float(255)
    prediction = model.predict(image)
    i = prediction.argmax()
    return CLASSES[i]

def run_prediction():
    print("\n\n\n Ready to capture signs! Please place sign in green box.")

    CAM = cv2.VideoCapture(0)
    (ret, frame) = CAM.read()
    old_text = ''
    predicted_text = ''
    frameCounter = 0
    text_so_far = ''
    RECORDING_TOGGLE = False
    while True:
        if frame is not None: 
            frame = cv2.flip(frame, 1)
            frame = cv2.resize( frame, (400,400))
            cv2.rectangle(frame, (300,300), (100,100), (0,255,0), 2)
            crop_img = frame[100:300, 100:300]
            grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(grey,210,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
            blackboard = np.zeros(frame.shape, dtype=np.uint8)
            cv2.putText(blackboard, "", (30, 40), cv2.FONT_ITALIC, 1, (255, 255, 0))
            if frameCounter > 30 and predicted_text != "":
                text_so_far += predicted_text
                frameCounter = 0
            if frameCounter > 30 and predicted_text == "":
                text_so_far += " "
                frameCounter = 0
            if RECORDING_TOGGLE == True:
                old_text = predicted_text
                predicted_text = predict(thresh)
                if old_text == predicted_text:
                    frameCounter += 1
                else:
                    frameCounter = 0
                cv2.putText(blackboard, text_so_far, (30, 80), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 127))
            res = np.hstack((frame, blackboard))
            
            cv2.imshow("Camera", res)
            cv2.imshow("Computer's Vision", thresh)
            
        rval, frame = CAM.read()
        keypress = cv2.waitKey(1)
        if keypress == 13: # Enter Key
            RECORDING_TOGGLE = True
        if keypress == 27: # ESC Key
            break

    CAM.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    CAM.release()


run_prediction()


