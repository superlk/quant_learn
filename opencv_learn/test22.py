import cv2 as cv
import numpy as np


# 圆检测，霍夫圆检测


def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("circles",image)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
# src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/line.jpg')
src = cv.imread('/Users/superlk/Downloads/circle.jpg')


# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)

# line_detection(src)
detect_circles_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()

# cv.GaussianBlur() 高斯模糊
