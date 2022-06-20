import cv2
import mediapipe as mp
import numpy as np
import uuid
import os

mp_drawing= mp.solutions.drawing_utils
mp_hand=mp.solutions.hands


cap=cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success,frame=cap.read()
        imag=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        imag.cv2.flip(imag,1)
        imag.flag.writable=False
        result=hands.process(imag)
       
        imag.flag.writable=True
        imag=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        cv2.imshow('Virtual Mouse Controller', imag)
        if cv2.waitKey(5) == ord('q'):
                    break
cap.release()
cv2.destroyAllWindows()