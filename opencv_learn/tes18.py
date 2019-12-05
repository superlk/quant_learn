import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 图像金字塔
def pyramid_demo(image):  # 高斯金字塔
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow('pyramin_dwon:' + str(i), dst)
        temp = dst.copy()
    return pyramid_image


def lapalian_demo(image):  # 拉普拉斯金字塔
    pyramid_image = pyramid_demo(image)
    level = len(pyramid_image)
    for i in range(level - 1, -1, -1):
        if i - 1 < 0:
            expand = cv.pyrUp(pyramid_image[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lpls:" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_image[i], dstsize=pyramid_image[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_image[i - 1], expand)
            cv.imshow("lpls:" + str(i), lpls)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)

# pyramid_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
