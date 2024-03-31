# Change the background of the image below. Fly Superman in the sky.

import cv2
import numpy as np
import matplotlib.pyplot as plt

superman_image = cv2.imread("input/superman.jpg")
sky_fire_image = cv2.imread("input/sky_fire.jpg")

superman_image_copy = superman_image.copy()
superman_image_HSV = cv2.cvtColor(superman_image_copy, cv2.COLOR_BGR2HSV)

H, S, V = cv2.split(superman_image_HSV)

for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if 30 < H[i, j] < 80 :  #green
            superman_image[i, j] = sky_fire_image[i, j]
        if H[i, j] < 0:
            superman_image[i, j] = sky_fire_image[i, j]
                 
cv2.imwrite("output/superman.jpg", superman_image)