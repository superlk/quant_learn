import cv2 as cv
import numpy as np


# 泛洪填充
def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color", copyImg)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255

    cv.imshow("fill_color", image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill_color1", image)

src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)

# face = src[100:239, 135:227]
#
# gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# backface = cv.cvtColor(gray, cv.COLOR_BGRA2BGR)
# src[100:239, 135:227] = backface
# cv.imshow("face", src)
# fill_color_demo(src)
fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()
