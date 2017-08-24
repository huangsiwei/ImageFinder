from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DataBase:
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(DataBase, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:test@localhost:3306/imagefinder?charset=utf8', echo=True,
                                    encoding='utf-8')
        DB_Session = sessionmaker(bind=self.engine)
        session = DB_Session()
        self.session = session

    def save_obj(self, objs):
        for obj in objs:
            self.session.add(obj)
        self.session.commit()
