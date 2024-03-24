# Convolution and Histogram
This program uses [opencv](https://github.com/opencv/opencv) and  numpy libraries.

## 1-Histogram 📊
A. Write a function to get an image as input argument then calculate histogram and return it. 

B. Call the function, then visualize the result with plt.plot(), plt.hist() and plt.bar().

## 2-Foreground focus, Blur background 🌷
A blurred background draws the focus to what’s important. It also often plays a part in differentiating the professional portrait 😍 from the casual snapshot 😐.

Focus on the flower and blur the background.

## 3-Edge detection 
Use Laplacian Operator to detect edges of image.

## 4-Vertical and horizontal edge detection
Use A suitable kernel to detect vertical and horizontal edges of image.

## 5-Noise reduction 🩻
Mean filtering is a simple and easy to implement method of smoothing images. It is often used to reduce noise in images. The mean filter is computed using a convolution. The idea of mean filtering is simply to replace each pixel value in an image with the mean (average) value of its neighbors, including itself. Often a 3×3 square kernel is used, although larger kernels (e.g. 5×5 squares) can be used for more severe smoothing.

Apply a 3x3 average filter to reduce noise in images. What happens if a 5x5 or a 15x15 filter is used?

### How to Install
Run following command:
```
pip install -r requirement.txt
```

### How to Run
execute this command in terminal:
```
python noise-reduction.py
```

### Result
![histogram](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP31_Convolution_Histogram/output/plt.hist().png)

![focus](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP31_Convolution_Histogram/output/focus_foreground.jpg)

![edge](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP31_Convolution_Histogram/output/edge_lion.jpg)

![v_h_edge](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP31_Convolution_Histogram/output/v_edege_building.jpg)

![vnoise](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP31_Convolution_Histogram/output/xray_3in3.jpg)


