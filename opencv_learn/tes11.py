import cv2 as cv
import numpy as np


# EPF ，双线性模糊
def bi_demo(image):
    dst = cv.bilateralFilter(image, False, 100, 15)
    cv.imshow("bi_demo", dst)


# 边缘模糊,均值迁移
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("bi_demo", dst)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/test.jpg')
cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)
# bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
