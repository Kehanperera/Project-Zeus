
import cv2
import mediapipe
import time
import face_recognition_models
def face():
    cap = cv2.VideoCapture(0)


    while True:
        success, img = cap.read()

        cv2.imshow("Project Zeus", img)
