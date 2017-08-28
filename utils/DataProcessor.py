from utils.DataBaseMgnt import *
from basic.AssReader import *


class DataProcessor:
    def __init__(self):
        self.database = DataBase()

    def update_dialogue_data(self):
        ass_reader = AssReader()
        dialogue_list = ass_reader.generate_dialogue_list()
        self.database.save_objs(dialogue_list)


dp = DataProcessor()
dp.update_dialogue_data()
