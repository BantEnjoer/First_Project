import numpy as np
import cv2
import time

def frames_maker():
    cap = cv2.VideoCapture('input.mp4')
    t = time.time()

    i = 0
    hui, image = cap.read()
    while not (image is None):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if i % 4 == 0:
            cv2.imwrite('CC\\' + str(i // 4) + '.jpg', image)
        hui, image = cap.read()
        i += 1