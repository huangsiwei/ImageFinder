import uuid

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True, encoding='utf-8')
print(engine)
Base = declarative_base()


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


Base.metadata.create_all(engine)
