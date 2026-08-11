import cv2
import numpy as np
image = np.array(cv2.imread("img2.jpg"))
BlueArray = image[:, :, 0];
GreenArray = image[:, :, 1];
RedArray = image[:, :, 2];
print(RedArray.shape)
print(BlueArray.shape)
print(GreenArray.shape)
BlueWeight = float(input("enter the weight of Blue array between [0 , 1] :"));
GreenWeight = float(input(f"enter the weight of Blue array [0 , {1-BlueWeight}]:"));
if((1-BlueWeight-GreenWeight) < 0):

    print("Wrong Weights Assigned");
    exit();
else:
    RedWeight = float(input("enter the weight of Blue array [0 , 1] :"));
if(BlueWeight+GreenWeight+RedWeight != 1):
    print("invalid Weights Taken")
    exit();
rows,col = RedArray.shape;
meanArray = np.ones((rows , col));
for i in range(rows):
    for j in range(col):
        sum = int(BlueArray[i][j]) + int(GreenArray[i][j]) + int(RedArray[i][j]);
        meanArray[i][j] = sum/3;
print(BlueArray[0][0] ,GreenArray[0] , RedArray[0] , meanArray[0]);
cv2.imshow("img2.jpg", meanArray);
cv2.waitKey(0)
cv2.destroyAllWindows()