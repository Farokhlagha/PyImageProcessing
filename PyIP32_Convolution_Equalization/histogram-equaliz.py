# Histogram Equalization
# cv2.equalizeHist() improve the contrast of images.
# cv2.createCLAHE() CLAHE stands for Contrast Limited Adaptive Histogram Equalization.

import cv2
import matplotlib.pyplot as plt

image1=cv2.imread("input/unequalized.jpg", cv2.IMREAD_GRAYSCALE)
# image2=cv2.imread("input/from_sky.jpg", cv2.IMREAD_GRAYSCALE)
# image3=cv2.imread("input/lab.jpg", cv2.IMREAD_GRAYSCALE)

image1_ok=cv2.equalizeHist(image1)

# hist1=cv2.calcHist([image1], [0], None, [256], [0, 256])
hist1_1=cv2.calcHist([image1_ok], [0], None, [256], [0, 256])
# plt.plot(hist1)
plt.plot(hist1_1)
plt.show()
cv2.imwrite('output/equaliz.jpg', image1_ok)