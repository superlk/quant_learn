import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)  # 0 usb摄像头
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)  # 高，宽， 像素通道
    print(image.size)  # 大小
    print(image.dtype)  # 像素点通道位数
    pixel_data = np.array(image)
    print(pixel_data)


def access_pixels(image):
    # print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(width, height, channels)
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def create_image():
    ### 多通道
    # img = np.zeros([400, 400, 3], np.uint8)
    # img[:, :, 0] = np.ones([400, 400]) * 255
    #
    # cv.imshow("new image", img)
    ### 单通道
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow("new image", img)


# opencv  Api
def inverse(image):
    dst = cv.bitwise_not(image)  # 像素取反
    cv.imshow("new image", dst)


# 色彩空间 相互转换
def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 转换灰度
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('ycrcb', ycrcb)


def extract_object_demo():
    capture = cv.VideoCapture(0)  # 0 usb摄像头
    while True:
        ret, frame = capture.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        if not ret:
            break
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break


src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
cv.imshow('import image', src)
# get_image_info(src)
# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 获取灰度图片
# cv.imwrite("/Users/superlk/Downloads/result.jpg", gray)  # 保存图像
# video_demo()
t1 = cv.getTickCount()
# access_pixels(src)
# create_image()
# inverse(src)
# color_space_demo(src)
# extract_object_demo()

# 三个通道分离
b, g, r = cv.split(src)  # 三个通道，
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
# 三个通道合并
src = cv.merge([b, g, r])

cv.imshow("合并",src)

t2 = cv.getTickCount()

time = (t2 - t1) / cv.getTickFrequency()
print("time>>>>", time * 1000)
cv.waitKey(0)
cv.destroyAllWindows()
