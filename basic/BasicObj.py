from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AssFile:
    def __init__(self, file_location, file_name):
        self.file_location = file_location
        self.file_name = file_name
        pass


class ScreenShot:
    def __init__(self, img_id, img_ass, AssFile):
        pass


class Dialogue(Base):
    __tablename__ = "dialogue"
    id = Column(Integer, primary_key=True)
    text = Column(String(1000))
    start_time = Column(String(100))
    end_time = Column(String(100))
    raw_text = Column(String(1000))
    file_name = Column(String(1000))

    def __init__(self, id, text, start_time, end_time, raw_text, file_name):
        self.id = id
        self.text = text
        self.start_time = start_time
        self.end_time = end_time
        self.raw_text = raw_text
        self.file_name = file_name
        pass
