# Convolution 2D and Histogram Equalization
This program uses [opencv](https://github.com/opencv/opencv) and  numpy and matplotlib libraries.

## 1-Convolution 2D 📊
Apply five 2D filters with different kernels on my custom image. 

Use
```
 np.hstack()
```
  to place the output image next to the input image.
  ```
  result = np.hstack((input_image, output_image))
  ```

## 2-Average filter
Use the average filter to reveal hidden things.

## 3-Median Filter
Use median filter to reduce noise in images. 

## 4-Histogram Equalization
improve the contrast of these images with:
```
cv2.equalizeHist()
```
CLAHE stands for Contrast Limited Adaptive Histogram Equalization. maybe this function helps to improve the contrast of the image.
```
cv2.createCLAHE()
```

### How to Install
Run following command:
```
pip install -r requirement.txt
```

### How to Run
execute this command in terminal:
```
python average_filter.py
```

### Result
convolution![](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP32_Convolution_Equalization/output/2Dfilter_emboss.jpg)

average![](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP32_Convolution_Equalization/output/hidden_character.jpg)

median![](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP32_Convolution_Equalization/output/baloon.jpg)

equalization![](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP32_Convolution_Equalization/output/equaliz.jpg)




