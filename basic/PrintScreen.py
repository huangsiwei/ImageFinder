import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import basic.BasicObj
from utils.DataBaseMgnt import *
import os
from utils.Config import *

img_dir = "C:\PycharmProjects\ImageFinder\img"


class ImageShot:
    def __init__(self):
        database = DataBase()
        current_config = Configuration().current_config()
        self.database = database
        self.dialogue_list_to_shot = database.find_all(basic.BasicObj.Dialogue)
        self.image_list_to_add_ass = database.find_all(basic.BasicObj.Dialogue)
        self.mov_dir = current_config.get("mov_dir")
        self.img_dir = current_config.get("raw_image_dir")

    # TODO: 完成后需要更新数据库标记已经截图
    def shot_image(self):
        for dialogue in self.dialogue_list_to_shot:
            cmd = 'ffmpeg -ss {start_time} -i {file_location} -y -f mjpeg -vframes 1 -s 720x540 {uid}.jpg'.format(
                start_time=dialogue.start_time, file_location=self.mov_dir + dialogue.file_name + '.mp4',
                uid=self.img_dir + dialogue.uid)
            subprocess.call(cmd)
            dialogue.has_image = false
            self.database.update_obj(dialogue)

    # TODO: 完成后需要更新数据库标记已经截图
    def shot_gif(self):
        for dialogue in self.dialogue_list_to_shot:
            start_time = round(
                float(dialogue.start_time.split(":")[1]) * 60 + float(dialogue.start_time.split(":")[2]))
            end_time = round(float(dialogue.end_time.split(":")[1]) * 60 + float(dialogue.end_time.split(":")[2]))
            t = end_time - start_time
            cmd = 'ffmpeg -ss {start_time} -t {t} -i {file_location} -s 350x270 {uid}.gif'.format(
                start_time=dialogue.start_time, t=t,
                file_location=self.mov_dir + dialogue.file_name + '.mp4',
                uid=dialogue.uid)
            subprocess.call(cmd)

    # TODO: 完成后需要更新数据库标记已经添加字幕
    def add_ass_to_image(self):
        for dialogue in self.image_list_to_add_ass:
            img = Image.open("D:\\raw_img\\{}.jpg".format(dialogue.uid))
            (img_x, img_y) = img.size
            ttfont = ImageFont.truetype('C:\Windows\Fonts\SIMLI.TTF', int(img_y / 18))
            draw = ImageDraw.Draw(img)
            x_offset = int(img_x) / 2 - int(img_y / 18) * (len(dialogue.simple_text) / 2)
            draw.text((x_offset + 1, img_y - int((img_y * 2) / 20)), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset, img_y - int((img_y * 2) / 20) + 1), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset + 1, img_y - int((img_y * 2) / 20) + 1), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset - 1, img_y - int((img_y * 2) / 20) - 1), dialogue.simple_text, (0, 0, 0), font=ttfont)
            draw.text((x_offset, img_y - int((img_y * 2) / 20)), dialogue.simple_text, (255, 255, 255), font=ttfont)
            img.save(img_dir + os.sep + dialogue.uid + '.jpg', 'jpeg')
