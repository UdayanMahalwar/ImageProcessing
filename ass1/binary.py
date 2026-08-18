import cv2
import numpy as np
img = cv2.imread("grayscale.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found!")
    exit()
height,width = img.shape
binary_m = np.zeros((height,width), dtype = np.uint8)
mean_img = np.mean(img)
for y in range(height):
	for x in range(width):
		if img[y][x] < mean_img:
			binary_m[y][x]=0
		else:
			binary_m[y][x] = 255

cv2.imshow("Binary Image", img)
cv2.imshow("Binary Image", binary_m)
cv2.waitKey(0)
cv2.destroyAllWindows()
