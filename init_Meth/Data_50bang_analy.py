#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections
from init_Meth.Data_analy import *


class Files_Analy(object):
    # file_path = '../api_data_dir/file_log.txt'
    def __init__(self, path_script):
        self.file_path = path_script

    def files_analy(self):
        # 将生成的json文件进行遍历，找出返回为空的字段
        with open(self.file_path, 'r', encoding='UTF-8') as f:
            for j in f.readlines():
                JS = eval(j)
                jd = collections.OrderedDict(dict(JS))
                Phone_Data_50bang(jd)
                # Data_Data_50bang(jd)
                ClickPosEvent_ActionID_50bang(jd)
                Error_Up_50bang(jd)
                # Tag_Data_50bang(jd)
                ActionID_Data_50bang(jd)
                # 完成json的event_type时间与sdkdatabox事件的映射


# if __name__ == "__main__":
#     FA = Files_Analy()
#     FA.files_analy()
