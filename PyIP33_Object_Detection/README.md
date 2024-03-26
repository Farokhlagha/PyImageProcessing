# Object_Detection
This program uses [opencv](https://github.com/opencv/opencv) and  numpy and matplotlib libraries.

## 1-Dice Recognition
A notebook for count the number of dots on the dice.

Hint: use the hierarchy to find children and parent contours.

## 2-boundingRect
Implement cv2.boundingRect() function from scratch.
```
x, y, w, h = cv2.boundingRect(contour)
```

## 3-contourArea
Implement cv2.contourArea() function from scratch.
```
area = cv2.contourArea(contours)
```

## 4-findContours
Implement cv2.findContours() function from scratch.
```
contours, _ = cv2.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
```
## 5-Funny webcam
A funny webcam application 😂
A notebook for count the number of dots on the dice.

### How to Install
Run following command:
```
pip install -r requirement.txt
```

### How to Run
execute this command in terminal:
```
python Dice_recognition.ipynb
```

### Result
dice![](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP33_Object_Detection/output/dice_number.png)

webcam![](https://raw.githubusercontent.com/Farokhlagha/PyImageProcessing/main/PyIP33_Object_Detection/output/funny_camera.png)






