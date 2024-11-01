import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
while True:
    success, frame = cam.read()

    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(1)

    cv2.imshow("qrscan", frame)
    cv2.waitKey(1)