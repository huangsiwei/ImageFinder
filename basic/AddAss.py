import os
import sys

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img_dir = "C:\PycharmProjects\ImageFinder\img"
raw_img_dir = "C:\PycharmProjects\ImageFinder\\raw_img"


def add_ass(image_uuid, simple_text):
    img = Image.open("C:\PycharmProjects\ImageFinder\\raw_img\\{}.jpg".format(image_uuid))
    (img_x, img_y) = img.size
    ttfont = ImageFont.truetype('C:\Windows\Fonts\STHUPO.TTF', int(img_y / 20))
    draw = ImageDraw.Draw(img)
    draw.text((int(img_x / 20), img_y - int((img_y * 1.3) / 20)), simple_text, (255, 255, 255), font=ttfont)
    img.save(img_dir + '\\' + image_uuid + '.jpg', 'jpeg')


raw_img_list = os.listdir(raw_img_dir)

for raw_img in raw_img_list:
    print(raw_img)
    raw_img.replace(".jpg", "")

    pass
