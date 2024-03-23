# Write a program for read an image and count number of cats in it 

import cv2
import numpy as np

image = cv2.imread("input\cats.jpeg")
cat_face_detector = cv2.CascadeClassifier (cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
img = cv2.resize(image, [700, 450])
faces = cat_face_detector.detectMultiScale(img)

count = 0
for face in faces:
    x, y, w, h = face
    cv2.rectangle(img, [x, y], [x+w, y+h], [0, 0, 150], 2)
    count +=1

cv2.imshow("cat's face", img)
cv2.imwrite("output\cat_detection.jpg", img)
cv2.waitKey()