import cv2 as cv
import numpy as np


# Canny 算法，边缘提取
# 1。 高斯模糊
# 2。 灰度转换
# 3。 计算梯度
# 4。 非最大信号抑制
# 5。 高低阈值输出二值图像


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)  # 高斯模糊 降噪
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # x 梯度
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # y 梯度
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)  # 50 底阈值，150高阈值,高是底的3倍
    # edge_output = cv.Canny(gray, 50, 150)  # 50 底阈值，150高阈值

    cv.imshow("Canny Edge", edge_output)
    # 彩色边缘
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow('color edge', dst)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)

edge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()

# cv.GaussianBlur() 高斯模糊
