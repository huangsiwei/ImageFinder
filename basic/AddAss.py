import os
import basic.BasicObj

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

img_dir = "D:\img"
raw_img_dir = "D:\\raw_img"

engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True, encoding='utf-8')
print(engine)
Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()

dialogue_list = session.query(basic.BasicObj.Dialogue).all()


def add_ass(image_uuid, simple_text):
    img = Image.open("D:\\raw_img\\{}.jpg".format(image_uuid))
    (img_x, img_y) = img.size
    ttfont = ImageFont.truetype('C:\Windows\Fonts\SIMLI.TTF', int(img_y / 18))
    draw = ImageDraw.Draw(img)
    x_offset = int(img_x)/2 - int(img_y / 18) * (len(simple_text)/2)
    draw.text((x_offset + 1, img_y - int((img_y * 2) / 20)), simple_text, (0, 0, 0), font=ttfont)
    draw.text((x_offset, img_y - int((img_y * 2) / 20) + 1), simple_text, (0, 0, 0), font=ttfont)
    draw.text((x_offset + 1, img_y - int((img_y * 2) / 20) + 1), simple_text, (0, 0, 0), font=ttfont)
    draw.text((x_offset - 1, img_y - int((img_y * 2) / 20) - 1), simple_text, (0, 0, 0), font=ttfont)
    draw.text((x_offset, img_y - int((img_y * 2) / 20)), simple_text, (255, 255, 255), font=ttfont)
    img.save(img_dir + '\\' + image_uuid + '.jpg', 'jpeg')


raw_img_list = os.listdir(raw_img_dir)

for raw_img in raw_img_list:
    print(raw_img)
    raw_img_id = raw_img.replace(".jpg", "")
    dialogue = [x for x in dialogue_list if x.uuid == raw_img_id][0]
    add_ass(raw_img_id, dialogue.simple_text)
