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

root_dir = "F:\\MOV\\银魂\\銀魂第一季(1-201)\\31-45\\"
img_dir = "C:\PycharmProjects\ImageFinder\gif"

engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True, encoding='utf-8')
print(engine)
Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()

dialogue_list = session.query(basic.BasicObj.Dialogue).all()

for dialogue in dialogue_list[0:50]:
    start_time = round(
        float(dialogue.start_time.split(":")[1]) * 60 + float(dialogue.start_time.split(":")[2]))
    end_time = round(float(dialogue.end_time.split(":")[1]) * 60 + float(dialogue.end_time.split(":")[2]))
    t = end_time - start_time
    cmd = 'ffmpeg -ss {start_time} -t {t} -i {file_location} -s 350x270 {uuid}.gif'.format(
        start_time=dialogue.start_time, t=t,
        file_location=root_dir + dialogue.file_name + '.mp4',
        uuid=dialogue.uuid)
    subprocess.call(cmd)
    print(dialogue)
