from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


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
    id = Column(Integer, primary_key=true)
    version = Column(Integer, default=0)
    uuid = Column(String(100), name="uuid", default=generate_uuid)
    simple_text = Column(String(1000))
    start_time = Column(String(100))
    end_time = Column(String(100))
    raw_text = Column(String(1000))
    file_name = Column(String(1000))

    def __init__(self, id, simple_text, start_time, end_time, raw_text, file_name):
        self.id = id
        self.uuid = generate_uuid()
        self.simple_text = simple_text
        self.start_time = start_time
        self.end_time = end_time
        self.raw_text = raw_text
        self.file_name = file_name

        pass
