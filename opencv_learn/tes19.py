import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 图像梯度
def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradxy", gradxy)


def lapalin_demo(image):  # 拉普拉斯算子
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lpls', lpls)


def lapalin_demo1(image):  # 拉普拉斯算子
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lpls', lpls)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)

# sobel_demo(src)
# lapalin_demo(src)  # 拉普拉斯算子

lapalin_demo1(src)
cv.waitKey(0)
cv.destroyAllWindows()
