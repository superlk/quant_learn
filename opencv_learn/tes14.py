import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_project_demo():
    sample = cv.imread("/Users/superlk/Downloads/sample.png")
    target = cv.imread("/Users/superlk/Downloads/target.png")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow("sample", sample)
    cv.imshow('target', target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [36, 48], [0, 180, 0, 245])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("demo", dst)


# 直方图反向投影
def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 255], [0, 180, 0, 256])
    # cv.imshow("histID",hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title('2d histogram')
    plt.show()


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/test.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)

# equalHist_demo(src)
# clahe_demo(src)
# hist2d_demo(src)
back_project_demo()
cv.waitKey(0)
cv.destroyAllWindows()
