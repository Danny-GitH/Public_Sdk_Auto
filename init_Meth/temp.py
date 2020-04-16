#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections
from init_Meth.Data_analy import *


file_path = '../api_data_dir/file_log.txt'


def files_analy():
    # 将生成的json文件进行遍历，找出返回为空的字段
    with open(file_path, 'r', encoding='UTF-8') as f:
        for j in f.readlines():
            JS = eval(j)
            jd = collections.OrderedDict(dict(JS))
            # Phone_Data_50bang(jd)
            # Data_Data_50bang(jd)
            ClickPosEvent_ActionID_50bang(jd)
            # Error_Up_50bang(jd)
            # # Tag_Data_50bang(jd)
            # ActionID_Data_50bang(jd)
            # 完成json的event_type时间与sdkdatabox事件的映射


files_analy()
