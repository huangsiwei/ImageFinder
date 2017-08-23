from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True, encoding='utf-8')
print(engine)
Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class Dialogue(Base):
    __tablename__ = "dialogue"
    uuid = Column(String(100), name="uuid", primary_key=True, default=generate_uuid)
    simple_text = Column(String(1000))
    start_time = Column(String(100))
    end_time = Column(String(100))
    raw_text = Column(String(1000))
    file_name = Column(String(1000))
    has_image = Column(Boolean)


Base.metadata.create_all(engine)
