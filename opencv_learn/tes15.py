import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# 模版匹配

def template_demo():
    tpl = cv.imread("/Users/superlk/Downloads/tmp.jpg")
    target = cv.imread("/Users/superlk/Downloads/obsession-lg.jpg")
    cv.imshow("template", tpl)
    cv.imshow("target", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  # 0-1,相关性，相关性因子
    th, tw = tpl.shape[:2]  # 模版高。宽
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)  # 算出来的值
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)  # 矩形尺寸
        cv.rectangle(target, tl, br, (0, 0, 255), 2)  # 矩形绘制原图 ,(0, 0, 255),红色 2 矩形边宽度
        cv.imshow("match" + np.str(md), target)


# src = cv.imread('/Users/superlk/Downloads/obsession-lg.jpg')
src = cv.imread('/Users/superlk/Downloads/test.jpg')
# src = cv.imread('/Users/superlk/Downloads/test.png')

cv.namedWindow("import image", cv.WINDOW_AUTOSIZE)
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
