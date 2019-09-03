import cv2 as cv
import numpy as np


# 加
def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


# 减
def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("add_demo", dst)


# 除
def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("add_demo", dst)


# 乘
def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("add_demo", dst)


# 均值
def others(m1, m2):
    M1 = cv.mean(m1)
    M2 = cv.mean(m2)
    print(M1)
    print(M2)


# 方差
def others1(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    print(dev1)
    print(dev2)


# 与，或，非
def logic_demo(m1, m2):
    # dst = cv.bitwise_and(m1, m2) 与
    # dst = cv.bitwise_or(m1, m2) # 或
    dst = cv.bitwise_not(m1)  # 非
    cv.imshow("add_demo", dst)


# 对比度，亮点 ,c,对比度，d亮度
def contrast_brightness_demo(image, c, b):
    h, w, c = image.shape
    blank = np.zeros([h, w, c], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1 - c, b)
    cv.imshow("demo", dst)


src1 = cv.imread('/Users/superlk/Downloads/linuxLogo.jpg')
src2 = cv.imread('/Users/superlk/Downloads/windowsLogo.jpg')
print(src1.shape)
print(src2.shape)
# cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
# cv.imshow('image1', src1)
# cv.imshow('image2', src2)
# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
# others(src1, src2)
# others1(src1, src2)
logic_demo(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
