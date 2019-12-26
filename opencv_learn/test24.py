import cv2 as cv
import numpy as np


# 对象侧量
def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshold value", ret)
    cv.imshow("binary image", binary)

    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 轮廓
        # rect = cv.boundingRect(contour)  # 轮廓的外接矩形
        x, y, w, h = cv.boundingRect(contour)
        mm = cv.moments(contour)  # 轮廓的几何距
        print(type(mm))
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)  # 画中心
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print("面积",area)
    cv.imshow("measure_object", image)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
# src = cv.imread('/Users/superlk/Downloads/demo.jpg')
# src = cv.imread('/Users/superlk/Downloads/line.jpg')
# src = cv.imread('/Users/superlk/Downloads/circle.jpg')
src = cv.imread('/Users/superlk/Downloads/num.jpg')


# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)

# line_detection(src)
measure_object(src)

cv.waitKey(0)
cv.destroyAllWindows()

# cv.GaussianBlur() 高斯模糊
