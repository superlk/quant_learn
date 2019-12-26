from PIL import Image, ImageFont, ImageDraw

image1 = Image.open('/Users/superlk/Downloads/templete1.png')
# image3 = Image.open('/Users/superlk/Downloads/templete2.png')

print(image1.size)
# print(image3.size)

image1.show()
# image3.show()

image2 = Image.open('/Users/superlk/Downloads/head.png')
# print(image2)


width = image1.size[0]
high = image1.size[1]

seconded_layer = Image.new('RGBA', (width, high + 1500), (0, 0, 0, 0,))
# seconded_layer = Image.new('RGBA', image2.size, (0, 0, 0, 0,))

# print(seconded_layer)
# seconded_layer.paste(image2, (47, 45))
# image = Image.composite(image1, image2, image1)
# s=Image.open(image)
# image.show()
# image1.paste(image2, (0, 1180))
image1.show()
box = (0, 1325, 1080, 2110)
new_image = image1.crop(box)
box1 = (0, 2110, 1080, 2339)
bottom = image1.crop(box1)
# new_image.show()


seconded_layer.paste(image1, (0, 0))
seconded_layer.paste(new_image, (0, 2110))
seconded_layer.paste(bottom, (0, 2895))

#
#
seconded_layer.show()
