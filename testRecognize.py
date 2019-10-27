"""
:param
    无
:return
    无
功能：识别图像中的目标边缘
"""""

import numpy as np
import cv2

img_path = "img.jpg"
image = cv2.imread(img_path)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将彩色图转化为灰度图
gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)    # 高斯平滑去噪
edged_img = cv2.Canny(gray_img, 35, 125)     # Canny算子阈值化
cv2.imshow("降噪效果图", edged_img)          # 显示降噪后的图片
cv2.waitKey(0)
# 获取纸张的轮廓数据
img, countours, hierarchy = cv2.findContours(edged_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# print(len(countours))
c = max(countours, key=cv2.contourArea)    # 获取最大面积对应的点集
cv2.minAreaRect(c)       # 最小外接矩形