import os

import basic.BasicObj as bo
import tools.zh_wiki

zh2Hans_keys = tools.zh_wiki.zh2Hans.keys()
zh2Hant_keys = tools.zh_wiki.zh2Hant.keys()


class AssReader:
    def __init__(self):
        root_dir = "/Users/huangsiwei/PycharmProjects/ImageFinder/assfile/"
        files_name_list = os.listdir(root_dir)
        self.dialogue_list = []
        self.ass_file_list = []
        for file_name in files_name_list[:]:
            if file_name.endswith(".ass"):
                ass_file_location = root_dir + file_name
                assFile = bo.AssFile(ass_file_location, file_name)
                self.ass_file_list.append(assFile)

    def generate_dialogue_list(self):
        rid = 16411
        for ass_file in self.ass_file_list:
            file = open(ass_file.file_location, 'r', encoding="utf-16")
            lines = tuple(file)
            for index in range(len(lines)):
                current_line = lines[index]
                if current_line.startswith("Dialogue") and "NTP" in current_line and "Default" in current_line:
                    dialogue_s = []
                    raw_dialogue_s = current_line.split(",")[-1].replace("\n", "")
                    for hanzi in raw_dialogue_s:
                        if hanzi in zh2Hans_keys:
                            dialogue_s.append(tools.zh_wiki.zh2Hans.get(hanzi))
                        elif hanzi in zh2Hant_keys:
                            dialogue_s.append(tools.zh_wiki.zh2Hant.get(hanzi))
                        else:
                            dialogue_s.append(hanzi)
                    rid += 1
                    simple_text = "".join(dialogue_s)
                    start_time = current_line.split(",")[1]
                    end_time = current_line.split(",")[2]
                    file_name = ass_file.file_location.split("\\")[-1].replace(".ass", "")
                    self.dialogue_list.append(
                        bo.Dialogue(simple_text=simple_text, start_time=start_time, end_time=end_time,
                                    raw_text=raw_dialogue_s,
                                    file_name=file_name))
        return self.dialogue_list
