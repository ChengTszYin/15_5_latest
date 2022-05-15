import sys
import cv2
import numpy as np
import time
from matplotlib import pyplot as pltq
import serial
import struct
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB1'
digi = 0
ss = ''
x = 0

ser.open()
size = 100
curX = 300
cap = cv2.VideoCapture(0)
while cap.isOpened():
    cc = ser.read(1)
    if (cc.isdigit()==True):
        ss = ss + cc.decode("utf-8")
        digi += 1
        if digi > 4:
        	print(ss)
        	#x = int(((int(ss) - 20000)/15000) * 500)
        	digi = 0
        	ss = ''
    ret, frame = cap.read() 
    image = cv2.flip(frame, 0)
    #image = cv2.flip(image, 1)
    cv2.circle(image,(curX,x), 20, (0,255,0), 0)
    cv2.imshow('webcam', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
   	 break
cap.release()
cv2.destroyAllWindows()
