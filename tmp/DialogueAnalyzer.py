import os
from os import path

import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

import tools.zh_wiki
import operator
import collections

zh2Hans_keys = tools.zh_wiki.zh2Hans.keys()
zh2Hant_keys = tools.zh_wiki.zh2Hant.keys()


def load_all_ass_file_list(ass_dir):
    ass_file_list = []
    files_name_list = os.listdir(ass_dir)
    for file_name in files_name_list:
        if file_name.endswith(".ass"):
            ass_file_list.append(file_name)
    return ass_file_list


def generate_word_dict(ass_file_list, encoding, dialogue_key_words):
    word_dict = {}
    for ass_file in ass_file_list:
        file = open(ass_file, 'r', encoding=encoding)
        lines = tuple(file)
        for index in range(len(lines)):
            current_line = lines[index]
            if current_line.startswith("Dialogue"):
                if all(dialogue_key_word in current_line for dialogue_key_word in dialogue_key_words):
                    dialogue_s = []
                    raw_dialogue_s = current_line.split(",")[-1].replace("\n", "")
                    for hanzi in raw_dialogue_s:
                        if hanzi in zh2Hans_keys:
                            dialogue_s.append(tools.zh_wiki.zh2Hans.get(hanzi))
                        # elif hanzi in zh2Hant_keys:
                        #     dialogue_s.append(tools.zh_wiki.zh2Hant.get(hanzi))
                        else:
                            dialogue_s.append(hanzi)
                    seg_list = jieba.lcut("".join(dialogue_s), cut_all=False)
                    for seg in seg_list:
                        if word_dict.get(seg) is None:
                            word_dict[seg] = 1
                        else:
                            word_dict[seg] += 1
    return word_dict


g_root_dir = "F:\MOV\银魂\銀魂第一季(1-201)\\"
n_root_dir = "C:\\Users\hsw11\Downloads\[海贼王][one_piece][451-500][枫雪字幕组外挂字幕][sub]"

g_word_dict = generate_word_dict([g_root_dir + "\\" + x for x in load_all_ass_file_list(g_root_dir)], "utf-16",
                                 ["NTP", "Default"])
n_word_dict = generate_word_dict([n_root_dir + "\\" + x for x in load_all_ass_file_list(n_root_dir)], "utf-8", ["NTP"])

# print(g_word_dict)
# print(n_word_dict)

l = list((set(g_word_dict.keys()).union(set(n_word_dict.keys()))) ^ (set(g_word_dict.keys()) ^ set(n_word_dict.keys())))
# l = list(set(n_word_dict.keys()) - set(g_word_dict.keys()))

print(sorted(g_word_dict.items()))

# for w in l:
#     # print(sorted(g_word_dict.items()))
#     if g_word_dict.get(w) > 10 and len(w) > 1:
#         print(w + ":" + str(g_word_dict.get(w)))
