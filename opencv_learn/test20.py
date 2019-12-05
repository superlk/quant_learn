import cv2 as cv
import numpy as np


# Canny 算法，边缘提取
def blur_demo(image):
    dst = cv.blur(image, (1, 5))
    cv.imshow("blur", dst)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)
blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

# cv.GaussianBlur() 高斯模糊
