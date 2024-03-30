# Transparent your Microsoft logo and remove it's background

import cv2

def conver2PNG(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j][0] >= 170 and image[i, j][1]>= 170 and image[i, j][2] >= 170:
                image[i, j][3] = 0
    
    return image


bgr_logo = cv2.imread("input/ms_logo.png")
bgra_logo = cv2.cvtColor(bgr_logo, cv2.COLOR_BGR2BGRA)

png_logo=conver2PNG(bgra_logo)

cv2.imshow("", png_logo)
cv2.waitKey()

cv2.imwrite("output/microsoft_logo.png", png_logo)