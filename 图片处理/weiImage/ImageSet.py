from PIL import Image, ImageFont, ImageDraw
from flask import Flask

from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    # start()
    return render_template('hello.html', name=name)


def start():
    # 原始图片
    image1 = Image.open('/Users/superlk/Downloads/templete1.png')
    # image3 = Image.open('/Users/superlk/Downloads/templete2.png')
    # image1.show()
    # image3.show()

    # 头像
    headImage = Image.open('/Users/superlk/Downloads/head.png')
    headImage.thumbnail((100, 100))
    # image2.show()

    width = image1.size[0]  # 原始图片宽度
    high = image1.size[1]  # 原始图片高度
    # 图片高度
    imageHigh = 1220

    # 底部高度
    bottomHigh = 220
    # 现有点赞数
    num = 5
    n = num // 7 + 1
    ys = num % 7

    # 需要点赞数
    need_num = 68
    add_high = 0  # 图像增加高度
    need_n = need_num // 7 + 1
    add_high = need_n * 115  # 需要增加的高度
    seconded_layer = Image.new('RGBA', (width, imageHigh + add_high + bottomHigh), color="#f1f1f1")
    # seconded_layer = Image.new('RGBA', image2.size, (0, 0, 0, 0,))

    # print(seconded_layer)
    # seconded_layer.paste(image2, (47, 45))
    # image = Image.composite(image1, image2, image1)
    # s=Image.open(image)
    # image.show()
    # image1.paste(image2, (0, 1180))
    # image1.show()

    #  照片部分
    image_box = (0, 0, 1080, 1220)
    image = image1.crop(image_box)
    # image.show()

    # box = (0, 1325, 1080, 2110)
    # new_image = image1.crop(box)

    startBox = (0, 1220, 127, 1220 + 115)
    startImage = image1.crop(startBox)
    # startImage.show()

    startBox1 = (0, 1220 + 115, 127, 1220 + 115 + 115)
    startImage1 = image1.crop(startBox1)

    endBox = (1080 - 161, 1220, 1080, 1220 + 115)
    endImage = image1.crop(endBox)
    # endImage.show()

    # 评论
    box1 = (0, 2118, 1080, 2339)
    bottom = image1.crop(box1)
    # bottom.show()

    seconded_layer.paste(image, (0, 0))
    # for i in range(need_num):
    #     seconded_layer.paste(headImage, (0, 2110))
    #
    # seconded_layer.paste(bottom, (0, 2895))
    head_box = (127, 1220, 127 + 115, 1220 + 115)
    head_image = image1.crop(head_box)

    # 生成图片
    ss = make_image(seconded_layer, need_num, imageHigh, bottom, head_image, startImage, startImage1, endImage)
    # print("生成图片")
    # ss.save("./Image.png")
    ss.show()
    # print("生成图片成功")


def make_image(seconded_layer, need_num, imageHigh, bottom, headImage, startImage, startImage1, endImage):
    n = need_num // 7
    for i in range(need_num):
        num = (i // 7)
        col = (i % 7) * 115
        print(col)
        seconded_layer.paste(headImage, (127 + col, imageHigh + (num * 115)))

    for f in range(n + 1):
        if f == 0:
            seconded_layer.paste(startImage, (0, imageHigh))
            seconded_layer.paste(endImage, (1080 - 162, imageHigh))

        else:
            seconded_layer.paste(startImage1, (0, imageHigh + (f) * 115))
            seconded_layer.paste(endImage, (1080 - 162, imageHigh + (f) * 115))

    g = ((need_num // 7) + 1) * 115
    seconded_layer.paste(bottom, (0, imageHigh + g))
    # seconded_layer.show()

    return seconded_layer


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
