import cv2 as cv
import numpy as np


# EPF
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


# 边缘模糊
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
