# coding=utf-8
import os
import shutil
import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
from init_Meth.Get_50bang_file import *
from init_Meth.Data_50bang_analy import *


class TestRunner(object):
    """ Run test """

    def __init__(self, cases="./", title=u'自动化测试报告', description=u'环境：windows 10'):
        self.cases = cases
        self.title = title
        self.des = description
        self.cur_path = os.getcwd()

    # 删除log日志里面之前的所有文件
    def clear_logfiles(self):
        delDir = self.cur_path + "\\Log\\"
        if not os.path.exists(delDir):
            os.mkdir(delDir)
        delList = []
        delList = os.listdir(delDir)
        if delList:
            for f in delList:
                filePath = os.path.join(delDir, f)
                if os.path.isfile(filePath):
                    os.remove(filePath)
                    print(filePath + " was removed!")
                elif os.path.isdir(filePath):
                    shutil.rmtree(filePath, True)
                    print("Directory: " + filePath + " was removed!")
        else:
            pass

    def run(self):
        rep_path = self.cur_path + "\\report\\"
        if not os.path.exists(rep_path):
            os.mkdir(rep_path)

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("./report/" + now + "result.html", 'wb')
        case_path = self.cur_path + "\\test_Case\\"
        tests = unittest.defaultTestLoader.discover(case_path, pattern='S00*.py', top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()


if __name__ == '__main__':
    print("开始测试")
    test = TestRunner()
    test.clear_logfiles()
    test.run()
    print("开始执行获取文件")
    time.sleep(30)
    log_url = 'http://test.app.50bang.org/logs/'
    G5F = Get50bangFlie(log_url)
    tup_Y = G5F.get_Year()
    max_Y = G5F.findMinAndMax(tup_Y)

    url_month = log_url + max_Y + '/'
    tup_YM = G5F.get_Month(url_month)
    max_YM = G5F.findMinAndMax(tup_YM)
    url_YM = url_month + max_YM

    # 找到对应的test项目文件夹
    url_YM_Test = url_YM + '/test/'
    tup_File = G5F.get_Filename(max_YM, url_YM_Test)
    tup_File_last = tup_File[-1]
    log_file_path = url_YM_Test + tup_File_last
    path_script = G5F.get_Num12_Log(log_file_path)

    G5F.dele_tab(path_script)
    print("测试结束！")

    FA = Files_Analy(path_script)
    FA.files_analy()
