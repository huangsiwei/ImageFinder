from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import subprocess
import basic.BasicObj
import os
import sys

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

root_dir = "F:\\MOV\\银魂\\銀魂第一季(1-201)\\1-15\\"
img_dir = "C:\PycharmProjects\ImageFinder\img"

engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True, encoding='utf-8')
print(engine)
Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()

dialogue_list = session.query(basic.BasicObj.Dialogue).all()
for dialogue in dialogue_list:
    if dialogue.id > 5438:
        cmd = 'ffmpeg -ss {start_time} -i {file_location} -y -f mjpeg -vframes 1 -s 720x540 {uuid}.jpg'.format(
            start_time=dialogue.start_time, file_location=root_dir + dialogue.file_name + '.mp4', uuid=dialogue.uuid)
        subprocess.call(cmd)


# def add_ass(image_uuid, simple_text):
#     img = Image.open("C:\PycharmProjects\ImageFinder\\basic\\{}.jpg".format(image_uuid))
#     (img_x, img_y) = img.size
#     ttfont = ImageFont.truetype('C:\Windows\Fonts\STHUPO.TTF', int(img_y / 20))
#     draw = ImageDraw.Draw(img)
#     draw.text((int(img_x / 20), img_y - int((img_y * 1.3) / 20)), simple_text, (255, 255, 255), font=ttfont)
#     img.save(img_dir + '\\' + image_uuid + '.jpg', 'jpeg')
