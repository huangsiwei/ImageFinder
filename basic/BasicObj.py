from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import uuid
import hashlib

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


def custom_md5(simple_text, start_time, end_time, raw_text, file_name):
    md5obj = hashlib.md5()
    md5obj.update(simple_text.encode())
    md5obj.update(start_time.encode())
    md5obj.update(end_time.encode())
    md5obj.update(raw_text.encode())
    md5obj.update(file_name.encode())
    return md5obj.hexdigest()


class AssFile:
    def __init__(self, file_location, file_name):
        self.file_location = file_location
        self.file_name = file_name


class ScreenShot:
    def __init__(self, img_id, img_ass, AssFile):
        pass


class Dialogue(Base):
    __tablename__ = "dialogue"
    uid = Column(String(100), name="uid", primary_key=True)
    simple_text = Column(String(1000))
    start_time = Column(String(100))
    end_time = Column(String(100))
    raw_text = Column(String(1000))
    file_name = Column(String(1000))
    has_image = Column(Boolean, default=False)
    ass_added = Column(Boolean, default=False)
