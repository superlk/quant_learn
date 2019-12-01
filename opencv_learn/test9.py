import cv2 as cv
import numpy as np


# 模糊操作
def blur_demo(image):
    dst = cv.blur(image, (1, 5))
    cv.imshow("blur",dst)


src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)
blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

# cv.GaussianBlur() 高斯模糊
