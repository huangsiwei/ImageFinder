import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import basic.BasicObj
from utils.DataBaseMgnt import *
import os

root_dir = "F:\\MOV\\银魂\\銀魂第一季(1-201)\\1-15\\"
img_dir = "C:\PycharmProjects\ImageFinder\img"


class ImageShot:
    def __init__(self):
        database = DataBase()
        self.dialogue_list_to_shot = database.find_all(basic.BasicObj.Dialogue)
        self.image_list_to_add_ass = database.find_all(basic.BasicObj.Dialogue)
        self.root_dir = root_dir
        self.img_dir = img_dir

    # TODO: 完成后需要更新数据库标记已经截图
    def shot_image(self):
        for dialogue in self.dialogue_list_to_shot:
            cmd = 'ffmpeg -ss {start_time} -i {file_location} -y -f mjpeg -vframes 1 -s 720x540 {uuid}.jpg'.format(
                start_time=dialogue.start_time, file_location=self.root_dir + dialogue.file_name + '.mp4',
                uuid=dialogue.uuid)
            subprocess.call(cmd)

    # TODO: 完成后需要更新数据库标记已经截图
    def shot_gif(self):
        for dialogue in self.dialogue_list_to_shot:
            start_time = round(
                float(dialogue.start_time.split(":")[1]) * 60 + float(dialogue.start_time.split(":")[2]))
            end_time = round(float(dialogue.end_time.split(":")[1]) * 60 + float(dialogue.end_time.split(":")[2]))
            t = end_time - start_time
            cmd = 'ffmpeg -ss {start_time} -t {t} -i {file_location} -s 350x270 {uuid}.gif'.format(
                start_time=dialogue.start_time, t=t,
                file_location=root_dir + dialogue.file_name + '.mp4',
                uuid=dialogue.uuid)
            subprocess.call(cmd)

    # TODO: 完成后需要更新数据库标记已经添加字幕
    def add_ass_to_image(self):
        for dialogue in self.dialogue_list_to_shot:
            img = Image.open("D:\\raw_img\\{}.jpg".format(dialogue.uuid))
            (img_x, img_y) = img.size
            ttfont = ImageFont.truetype('C:\Windows\Fonts\SIMLI.TTF', int(img_y / 18))
            draw = ImageDraw.Draw(img)
            x_offset = int(img_x) / 2 - int(img_y / 18) * (len(dialogue.simple_text) / 2)
            draw.text((x_offset + 1, img_y - int((img_y * 2) / 20)), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset, img_y - int((img_y * 2) / 20) + 1), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset + 1, img_y - int((img_y * 2) / 20) + 1), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset - 1, img_y - int((img_y * 2) / 20) - 1), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset, img_y - int((img_y * 2) / 20)), dialogue.simple_text, (255, 255, 255), font=ttfont)
            img.save(img_dir + os.sep + dialogue.uuid + '.jpg', 'jpeg')
            pass
