import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import basic.BasicObj
import utils.BasicUtils
from utils.Config import *
from utils.DataBaseMgnt import *


class ImageShot:
    def __init__(self):
        database = DataBase()
        current_config = Configuration().current_config()
        self.database = database
        self.dialogue_list_to_shot = database.query(basic.BasicObj.Dialogue, basic.BasicObj.Dialogue.has_image, False)
        self.image_list_to_add_ass = database.query(basic.BasicObj.Dialogue, basic.BasicObj.Dialogue.ass_added, False)
        self.mov_dir = current_config.get("mov_dir")
        self.raw_img_dir = current_config.get("raw_image_dir")
        self.img_dir = current_config.get("image_dir")
        self.font = current_config.get("font")

    # TODO: 完成后需要更新数据库标记已经截图
    def shot_image(self):
        for dialogue in self.dialogue_list_to_shot:
            cmd = 'ffmpeg -ss {start_time} -i {file_location} -y -f mjpeg -vframes 1 -s 720x540 {uid}.jpg'.format(
                start_time=dialogue.start_time, file_location=self.mov_dir + dialogue.file_name + '.mp4',
                uid=self.raw_img_dir + dialogue.uid)
            subprocess.call(cmd)
            dialogue.has_image = True
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
            img = Image.open(self.raw_img_dir + "{}.jpg".format(dialogue.uid))
            (img_x, img_y) = img.size
            ttfont = ImageFont.truetype(self.font, int(img_y / 18))
            draw = ImageDraw.Draw(img)
            if "}" not in dialogue.simple_text:
                if "\\N" in dialogue.simple_text:
                    if dialogue.simple_text.count("\\N") == 1:
                        line_1 = dialogue.simple_text.split("\\N")[0]
                        line_2 = dialogue.simple_text.split("\\N")[1]
                        x_offset_1 = ImageShot.cal_x_offset(line_1, img_x, img_y)
                        ImageShot.add_ass(draw, line_1, (255, 255, 255), ttfont, 1, (0, 0, 0), x_offset_1,
                                          img_y - int((img_y * 2) / 14))
                        x_offset_2 = ImageShot.cal_x_offset(line_2, img_x, img_y)
                        ImageShot.add_ass(draw, line_2, (255, 255, 255), ttfont, 1, (0, 0, 0), x_offset_2,
                                          img_y - int((img_y * 2) / 20))
                        img.save(self.img_dir + os.sep + dialogue.uid + '.jpg', 'jpeg')
                    else:
                        text_to_add = dialogue.simple_text.replace_all("\\N", " ")
                        x_offset = ImageShot.cal_x_offset(text_to_add, img_x, img_y)
                        ImageShot.add_ass(draw, text_to_add, (255, 255, 255), ttfont, 1, (0, 0, 0), x_offset,
                                          img_y - int((img_y * 2) / 20))
                        img.save(self.img_dir + os.sep + dialogue.uid + '.jpg', 'jpeg')
                else:
                    x_offset = ImageShot.cal_x_offset(dialogue.simple_text, img_x, img_y)
                    ImageShot.add_ass(draw, dialogue.simple_text, (255, 255, 255), ttfont, 1, (0, 0, 0), x_offset,
                                      img_y - int((img_y * 2) / 20))
                    img.save(self.img_dir + os.sep + dialogue.uid + '.jpg', 'jpeg')
            dialogue.ass_added = True
            self.database.update_obj(dialogue)

    @staticmethod
    def add_ass(img_draw, text_to_add, text_color, ttfont, border_width, border_color, x_offset, y_offset):
        img_draw.text((x_offset + border_width, y_offset), text_to_add, border_color, font=ttfont)
        img_draw.text((x_offset, y_offset + border_width), text_to_add, border_color, font=ttfont)
        img_draw.text((x_offset + border_width, y_offset + border_width), text_to_add, border_color, font=ttfont)
        img_draw.text((x_offset - border_width, y_offset - border_width), text_to_add, border_color, font=ttfont)
        img_draw.text((x_offset, y_offset), text_to_add, text_color, font=ttfont)

    @staticmethod
    def cal_x_offset(text_to_add, img_x, img_y):
        alphabets = utils.BasicUtils.count_alphabet(text_to_add)
        hans = len(text_to_add) - alphabets
        return int(img_x) / 2 - int(img_y / 18) * ((hans + alphabets / 2) / 2)
