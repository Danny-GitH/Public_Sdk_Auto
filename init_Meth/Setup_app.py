#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Config_Files.CommPath import ConnPath


def Start_App_Para():
    # 获取config中的config.ini公用参数
    Obj = ConnPath()
    config = Obj.Conf_Path()
    platformName = config.get("mobile_50bang", "platformName")
    appPackage = config.get("mobile_50bang", "appPackage")
    appActivity = config.get("mobile_50bang", "appActivity")
    # automationName = config.get("mobile_50bang", "automationName")
    server = 'http://localhost:4723/wd/hub'

    # app启动参数
    desired_caps = {
        "platformName": platformName,
        "deviceName": server,
        "appPackage": appPackage,
        "appActivity": appActivity,
        # "automationName": automationName,
        "noReset": "True",  # 启动app时不要清除app里的原有的数据
        "unicodeKeyboard": "True",
        "resetKeyboard": "True"
    }
    return server, desired_caps


def get_driver():
    # 获取app启动参数
    server, desired_caps = Start_App_Para()
    driver = webdriver.Remote(server, desired_caps)
    wait = WebDriverWait(driver, 20)
    return driver, wait
