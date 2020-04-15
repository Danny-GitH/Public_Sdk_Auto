#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'

import os
import re
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup


class Get50bangFlie(object):
    """
    获取50bang 接口数据，已地址文件形式存储
    将日志存入到指定的文件中
    :param log_url:
    """

    def __init__(self, log_url):
        self.log_url = log_url
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.root_path = root_path
        self.api_data_dir = root_path + '\\api_data_dir'
        if not os.path.exists(self.api_data_dir):
            os.mkdir(self.api_data_dir)
        else:
            pass

    def get_Year(self):
        html_1 = urllib.request.Request(self.log_url)
        html = urllib.request.urlopen(html_1).read()
        with open(self.api_data_dir + '\\' + 'year.html', 'wb') as f:
            f.write(html)
        f.close()

        with open(self.api_data_dir + '\\' + 'year.html', encoding='utf-8') as file_obj:
            contents = file_obj.read()
        contents = contents.rstrip()
        soup = BeautifulSoup(contents, 'html.parser')
        regex = "(\d{4}.)"
        tup = []
        for k in soup.find_all('a'):
            # print(k)
            # print(k['class'])#查a标签的class属性
            # print(k['id'])#查a标签的id值
            # print(k['href'])#查a标签的href值
            # print(k.string)  # 查a标签的string
            match_obj = re.match(regex, k['href'])
            if match_obj:
                t = match_obj.group(0).split('/')
                # print(t[0])
                tup.append(t[0])
        return tup

    def findMinAndMax(self, L):
        n = 0
        Min = 0
        Max = 0
        # for i,value in enumerate(L):
        # print(i, value)
        for n in range(len(L)):
            a = L[n]
            b = L[n - 1]
            if a < b:
                Min = a

            else:

                Max = a
        n = n + 1
        return Max

    def get_Month(self, url_month):
        dir_2 = urllib.request.Request(url_month)
        dir_2 = urllib.request.urlopen(dir_2).read()
        with open(self.api_data_dir + '\\' + 'month.html', 'wb') as f:
            f.write(dir_2)
        f.close()

        # print(html.text)
        with open(self.api_data_dir + '\\' + 'month.html', encoding='utf-8') as file_obj:
            contents = file_obj.read()
        contents = contents.rstrip()
        soup = BeautifulSoup(contents, 'html.parser')
        regex_YM = "(\d{4}-\d{2}-\d{2}.)"
        tup_YM = []
        for k in soup.find_all('a'):
            # print(k)
            # print(k['class'])#查a标签的class属性
            # print(k['id'])#查a标签的id值
            # print(k['href'])#查a标签的href值
            # print(k.string)  # 查a标签的string
            match_obj = re.match(regex_YM, k['href'])

            if match_obj:
                tup_YM = match_obj.group(1).split('/')
                tup_YM.append(tup_YM[0])
        return tup_YM

    def get_Filename(self, max_YM, url_YM_Test):
        file_1 = urllib.request.Request(url_YM_Test)
        fiel_1 = urllib.request.urlopen(file_1).read()
        with open(self.api_data_dir + '\\' + 'file.html', 'wb') as f:
            f.write(fiel_1)

        # print(html.text)
        with open(self.api_data_dir + '\\' + 'file.html', encoding='utf-8') as file_obj:
            contents = file_obj.read()
        contents = contents.rstrip()
        # print(contents)
        soup = BeautifulSoup(contents, 'html.parser')
        regex_file = "(\w{4}\d{3})(\W)(\w{4})(\W)" + (str(max_YM)) + "(\W\d{2}\w9)(\.log)"
        tup = []
        for k in soup.find_all('a'):
            # print(k)
            # print(k['class'])#查a标签的class属性
            # print(k['id'])#查a标签的id值
            # print(k['href'])#查a标签的href值
            # print(k.string)  # 查a标签的string
            match_obj = re.match(regex_file, k['href'])
            if match_obj:
                t = match_obj.group(0)
                # print(t[0])
                tup.append(t)
            else:
                continue
        return tup

    def get_Num12_Log(self, log_file_path):
        if log_file_path:
            file_log = urllib.request.Request(log_file_path)
            file_log = urllib.request.urlopen(file_log).read()
            regix_time = "(\d{10}\s)"
            regix_ip = "(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
            fl = re.sub(regix_ip, '', file_log.decode('utf-8'))
            f2 = re.sub(regix_time, '\n', fl)
            path_script = self.api_data_dir + '/file_log.txt'
            with open(path_script, 'w+', encoding='UTF-8') as FILE:
                FILE.write(f2)
            FILE.close()
            return path_script

    def dele_tab(self, path_script):
        with open(path_script, 'r+', encoding='UTF-8') as f:
            line = f.read()
            f.seek(0, 0)
            f.truncate()
            line = line.replace("\t", "")
            line.strip()
            f.write(line)
        f.close()


# if __name__ == "__main__":
#     log_url = 'http://test.app.50bang.org/logs/'
#     G5F = Get50bangFlie(log_url)
#     tup_Y = G5F.get_Year()
#     max_Y = G5F.findMinAndMax(tup_Y)
#
#     url_month = log_url + max_Y + '/'
#     tup_YM = G5F.get_Month(url_month)
#     max_YM = G5F.findMinAndMax(tup_YM)
#     url_YM = url_month + max_YM
#
#     # 找到对应的test项目文件夹
#     url_YM_Test = url_YM + '/test/'
#     tup_File = G5F.get_Filename(max_YM, url_YM_Test)
#     tup_File_last = tup_File[-1]
#     log_file_path = url_YM_Test + tup_File_last
#     path_script = G5F.get_Num12_Log(log_file_path)
#
#     G5F.dele_tab(path_script)
