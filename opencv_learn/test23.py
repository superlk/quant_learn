import cv2 as cv
import numpy as np


# 轮廓发现
def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值图像
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值图像

    cv.imshow("binary", binary)
    contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # RETR_EXTERNAL 最大轮廓
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)  # 最后一个参数，-1 填充轮廓，2 画线 ，像素
        print(i)
    cv.imshow("detect contours", image)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
# src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/line.jpg')
src = cv.imread('/Users/superlk/Downloads/circle.jpg')

# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)

# line_detection(src)
contours_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()

# cv.GaussianBlur() 高斯模糊
