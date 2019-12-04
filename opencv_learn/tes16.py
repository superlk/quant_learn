import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 图像二值化

def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 灰度图
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # THRESH_OTSU计算阈值,THRESH_TRIANGLE三角计算阈值
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)  # 自己指定阈值
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)  # 截断
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)  # 小于127的变0

    print('threshold value:', ret)
    cv.imshow("binary", binary)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 灰度图
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                  cv.THRESH_BINARY, 255,
                                  10)  # 自适应阈值，ADAPTIVE_THRESH_GAUSSIAN_C高斯m值,blockSize 必须是寄数，10，C 常量大于她变黑色
    cv.imshow("binary", binary)


def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 灰度图
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    print("mean:", mean) # 均值
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)  # 小于127的变0
    cv.imshow("binary", binary)

# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
# template_demo()
# threshold_demo(src)
# local_threshold(src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
