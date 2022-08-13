import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img_1 = cv.imread('6_sur_new.png')
img_2 = cv.imread('8_sur_new.png')

#crop_1 = img_1[0:332,]
#crop_2 = img_2[:, 0:297]

gray_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
gray_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

ret_1, binary_1 = cv.threshold(gray_1, 55,255, cv.THRESH_BINARY)
ret_2, binary_2 = cv.threshold(gray_2, 55,255, cv.THRESH_BINARY)

img_1_px = np.asarray(binary_1)
img_2_px = np.asarray(binary_2)

img_1_px = img_1_px.astype('float32')
img_2_px = img_2_px.astype('float32')

img_1_px /= 255.0
img_2_px /= 255.0

rows, columns = binary_1.shape
img_size = rows * columns
img_1_black_px = img_size - cv.countNonZero(binary_1)
img_2_black_px = img_size - cv.countNonZero(binary_2)

spread_area_2D = img_2_black_px - img_1_black_px

time_interval = 2

avg_spread_velocity_2D = spread_area_2D / time_interval

print('The Average Spread Velocity is:' , avg_spread_velocity_2D , 'Pixels/Seconds')

plt.subplot(221)
plt.imshow(cv.cvtColor(img_1, cv.COLOR_BGR2RGB))
plt.subplot(222)
plt.imshow(cv.cvtColor(img_2, cv.COLOR_BGR2RGB))
plt.subplot(223)
plt.imshow(binary_1, cmap='gray')
plt.subplot(224)
plt.imshow(binary_2, cmap='gray')

plt.show()
