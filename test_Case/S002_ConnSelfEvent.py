#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'

import time
import re
import os
import unittest
# from init_Meth.Result_Excel import *
# from init_Meth.Color_Change import *
# from appium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from Config_File.CommPath import ConnPath
# from comm_method.Setup_app import Start_App_Para
from init_Meth.Get_script_name import *
# from elem_Encap.Screen_Shot import *
from elem_Encap.UI_Method import *
from init_Meth.Log_Method import Logger


class ConnSelfEvent(unittest.TestCase):
    def setUp(self, name=os.path.basename(__file__)):
        self.name = name
        obj = script_name(self.name)
        self.ScriptName = obj.ScriptName()
        # 获取log记录对象
        self.mylogger = Logger(logger=__name__, logname=obj.ScriptName())
        PySelenuim().start_app()
        time.sleep(3)
        self.mylogger.getlog().info("驱动加载成功")

    def test_search_in(self):
        # 首次启动信息流sdk，检查进入通用demo页面
        """
        com.staticsdemo:id/edt_version_name  com.staticsdemo:id/btn_set_version_name
        com.staticsdemo:id/edt_version_code  com.staticsdemo:id/btn_set_version_code
        com.staticsdemo:id/edt_phone         com.staticsdemo:id/btn_set_phone
        com.staticsdemo:id/edt_passid        com.staticsdemo:id/btn_set_passid
        com.staticsdemo:id/edt_header_extend com.staticsdemo:id/btn_set_header_extend
        :return:
        """
        self.event_types = PySelenuim().by_elements("id", "com.staticsdemo:id/item_des")
        if self.event_types:
            for event in self.event_types:
                event_content = event.get_attribute("text")
                self.mylogger.getlog().info(event.get_attribute("text"))
                if event_content == "宿主应用自定义业务事件":
                    event.click()
                    time.sleep(1)
                    self.setEventId = PySelenuim().by_element_dr("id", "com.staticsdemo:id/edt_content")
                    self.setEventId.send_keys('abc')
                    time.sleep(1)
                    self.nowSend = PySelenuim().by_element_dr("id", "com.staticsdemo:id/btn_send")
                    self.nowSend.click()
                    time.sleep(5)
                    break
                else:
                    continue
        else:
            print("操作事件元素找不到，请检查！")
            self.mylogger.getlog().info(u"操作事件元素找不到，请检查！：")

    def tearDown(self):
        # 驱动
        # wait = WebDriverWait(self.driver, 30)
        # 清除测试数据，还原测试前的环境
        PySelenuim().click_keycode(4)
        self.mylogger.getlog().info("该测试用例结束，关闭应用！\n")
        # 获取日志正文信息，写入到email中
        log_name = self.mylogger.log_name
        f = open(log_name, 'rb')
        # 读取测试报告正文
        # mail_body = f.readlines()
        f.close()
        # send_Mail(self, mail_body)


if __name__ == "__main__":
    unittest.main()
