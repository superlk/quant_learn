import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 超大图像二值化
def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, 2, cw):
            roi = gray[row:row + ch, col:cw + col]
            dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 全局阈值
            dst = cv.threshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)  # 局部阈值，自适应阈值

            gray[row:row + ch, col:cw + col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("/Users/superlk/Downloads/binary.png")


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
# template_demo()
# threshold_demo(src)
# local_threshold(src)
big_image_binary(src)

cv.waitKey(0)
cv.destroyAllWindows()
