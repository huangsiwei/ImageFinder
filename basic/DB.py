from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True, encoding='utf-8')
print(engine)
Base = declarative_base()


class Dialogue(Base):
    __tablename__ = "dialogue"
    id = Column(Integer, primary_key=True)
    text = Column(String(1000))
    start_time = Column(String(100))
    end_time = Column(String(100))
    raw_text = Column(String(1000))
    file_name = Column(String(1000))
    pass


# Base.metadata.create_all(engine)


def save_obj(objs):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    for obj in objs:
        session.add(obj)
    session.commit()
