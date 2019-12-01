import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 直方图均衡化
def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)  # 直方图均衡化
    cv.imshow("sss", dst)


# 局部直方图均衡化
def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("--", dst)


def create_rgb_hist(image):
    h, w, c = image.shape
    rgHist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            rgHist[np.int(index), 0] = rgHist[np.int(index), 0] + 1
    return rgHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(
        hist1, hist2, cv.HISTCMP_BHATTACHARYYA  # 巴氏距离
    )
    match2 = cv.compareHist(
        hist1, hist2, cv.HISTCMP_CORREL  # 相关性
    )
    match3 = cv.compareHist(
        hist1, hist2, cv.HISTCMP_CHISQR  # 卡方

    )
    print(match1,match2,match3)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.jpg')
src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)

# equalHist_demo(src)
clahe_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
