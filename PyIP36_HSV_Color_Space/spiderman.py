# Change Spiderman's clothes to green and yellow. 🕷️

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input/spiderman.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  

H, S, V = cv2.split(image)
H_new = H.copy().astype(np.float32)  

for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if V[i, j] < 180:
            if 100 < H[i, j] < 125 :  #blue
                H_new[i, j] -= 70
                V[i, j] += 100
        
        if H[i, j] < 15 or H[i, j] > 165 :    #red
            H_new[i, j] += 60

H_new = H_new.astype(np.uint8)            
result = cv2.merge((H_new, S, V))
result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
plt.imshow(result)

result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
cv2.imwrite("output/spiderman.jpg", result)