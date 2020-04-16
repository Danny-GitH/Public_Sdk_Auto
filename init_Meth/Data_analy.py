#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections
import os
import sys
import time

# js = {"error":[{"tag":"danny","msg":"topActivity: com.staticsdemo\/com.statistic2345.demo.test.TestErrorActivity\njava.lang.RuntimeException: 主动上报错误测试\n\tat com.statistic2345.demo.test.TestErrorActivity.onBtnReportError(TestErrorActivity.java:48)\n\tat com.statistic2345.demo.test.TestErrorActivity_ViewBinding$1.doClick(TestErrorActivity_ViewBinding.java:42)\n\tat butterknife.internal.DebouncingOnClickListener.onClick(DebouncingOnClickListener.java:22)\n\tat android.view.View.performClick(View.java:6291)\n\tat android.view.View$PerformClick.run(View.java:24931)\n\tat android.os.Handler.handleCallback(Handler.java:808)\n\tat android.os.Handler.dispatchMessage(Handler.java:101)\n\tat android.os.Looper.loop(Looper.java:166)\n\tat android.app.ActivityThread.main(ActivityThread.java:7529)\n\tat java.lang.reflect.Method.invoke(Native Method)\n\tat com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:245)\n\tat com.android.internal.os.ZygoteInit.main(ZygoteInit.java:921)\n","msgMD5":"4ec0b19da65193951dd8a4672c0c0fc6","version":"1.0","channel":"test_demo","date":"2020-04-10","time":"13:56:33"}],"header":{"accessibility":[],"activate":0,"local_day":"3","angle":1.858,"api_level":26,"sys_can_uninstall":2,"package":"com.staticsdemo","origin_version_code":"1","origin_version_name":"1.0","version_code":"1","app_version":"1.0","local_id":{"iccid":"","imei":"863020046259713","imei2":"863020046254516","imsi":"","meid":"a000009e301bab","wmac":"88bfe4269fc8"},"mainchannel":"test_demo","channel":"test_demo","send_time":1586498213,"debug_state":1,"android_id":"a18ea95895588a86","battery":100,"blutooth_addr":"","brand":"HONOR","charge_status":2,"hardware":"qcom","incremental":"227(C00)","manufacturer":"HUAWEI","device_model":"LND-AL30","os":"Android","os_version":"8.0.0","ram_remain":1280,"ram":2826,"resolution":"720*1360","build_date":1573618849,"rom_os_name":"EMUI","rom_remain":15107,"rom":25113,"rom_os_version":"8.0.0","deviceRoot":0,"serial":"73egk18c17000002","emulator_state":0,"extend":"","lat":"","lon":"","access":"WiFi","start":0,"oaid":"","pass_id":"13579","phone":"1565655","project_name":"test","proxy":1,"qq_modify":1586497034,"sdk_version":"5.1.5-SNAPSHOT","screen_brightness":68,"total_time":948434,"font_scale":1,"volume":"7\/15","traffic":1255,"uid":"863020046259713","uuid":"qdEFYoNctkLCewJaqooP2p8mB0lpVKUJlJ6ftjS10PF0qc%2F%2Fy3WTgQJKu1gMGIiI","vituralApp":0,"webview_version":"70.0.3538.110","wechat_modify":1586411117,"xposed":0},"install_apks":{"apps":[{"appName":"大众点评","packageName":"com.dianping.v1"},{"appName":"微信","packageName":"com.tencent.mm"},{"appName":"今日头条","packageName":"com.ss.android.article.news"},{"appName":"QQ","packageName":"com.tencent.mobileqq"},{"appName":"京东","packageName":"com.jingdong.app.mall"},{"appName":"微博","packageName":"com.sina.weibo"},{"appName":"手机淘宝","packageName":"com.taobao.taobao"},{"appName":"支付宝","packageName":"com.eg.android.AlipayGphone"}],"counts":8,"notSysAppCounts":27},"pageUseData":{"trails":[{"channel":"test_demo","lauchSession":"1586498177605","startLink":[{"pageName":"com.statistic2345.demo.MainActivity","timeMillis":1586498197006}],"versionName":"1.0"}],"usages":[{"channel":"test_demo","count":1,"durationMillis":14529,"pageName":"com.statistic2345.demo.test.TestErrorActivity","timeMillis":1586498196966,"versionName":"1.0"}]}}
# 创建一个txt文件,并向文件写入msg
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def text_create(key_name):
    log_path = root_path + "\\Log\\txt_log\\"  # 新创建的txt文件的存放路径
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    else:
        pass
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    full_path = log_path + key_name + '_' + str(now_time) + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'a+', encoding="utf-8")
    return file


def Phone_Data_50bang(js):
    """
    对应脚本S001，手机号、pass_id、extend
    :param js:
    :return:
    """
    if isinstance(js, dict):  # 判断是否是字典类型isinstance 返回True false
        global fa_key
        for key in js:
            if isinstance(js[key], dict):  # 如果dic_json[key]依旧是字典类型
                # fa_key = key
                Phone_Data_50bang(js[key])

            elif isinstance(js[key], list):
                # fa_key = key
                len_list_js = len(js[key])
                for j in range(0, len_list_js):
                    Phone_Data_50bang(js[key][j])
            else:
                # print(str(key) + " : " + str(js[key]))
                # file = text_create(key)
                if key == "phone":
                    file = text_create(key)
                    if js[key] == "1565655":
                        file.write('header -> phone: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                    else:
                        file.write('header -> phone: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
                if key == "pass_id":
                    file = text_create(key)
                    if js[key] == "13579":
                        file.write('header -> pass_id: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                    else:
                        file.write('header -> pass_id: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
                if key == "extend":
                    file = text_create(key)
                    if js[key] == "098":
                        file.write('header -> extend: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                    else:
                        file.write('header -> extend: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
    else:
        def_name = sys._getframe().f_code.co_name
        file = text_create(def_name)
        file.write(def_name + ' :数据格式有问题' + '\n')
        file.close()
        return False


def Data_Data_50bang(js):
    """
    对应脚本S002，data事件
    :param js:
    :return:
    """
    if isinstance(js, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in js:
            if isinstance(js[key], dict):  # 如果dic_json[key]依旧是字典类型
                Data_Data_50bang(js[key])

            elif isinstance(js[key], list):
                global fa_key
                len_list_js = len(js[key])
                for j in range(0, len_list_js):
                    Data_Data_50bang(js[key][j])
            else:
                # print(str(key) + " : " + str(js[key]))
                # file = text_create(key)
                if key == "data" and fa_key == "data":
                    file = text_create(key)
                    if js[key] == "abc":
                        file.write('data -> data: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                        break
                    else:
                        file.write('data -> data: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
    else:
        def_name = sys._getframe().f_code.co_name
        file = text_create(def_name)
        file.write(def_name + ' :数据格式有问题' + '\n')
        file.close()
        return False


def ClickPosEvent_ActionID_50bang(js):
    """
    对应脚本S003，计数事件统计值
    :param js:
    :return:
    """
    if isinstance(js, dict):  # 判断是否是字典类型isinstance 返回True false
        global fa_key
        for key in js:
            if isinstance(js[key], dict):  # 如果dic_json[key]依旧是字典类型
                fa_key = key
                ClickPosEvent_ActionID_50bang(js[key])

            elif isinstance(js[key], list):
                fa_key = key
                len_list_js = len(js[key])
                for j in range(0, len_list_js):
                    ClickPosEvent_ActionID_50bang(js[key][j])
            else:
                # print(str(key) + " : " + str(js[key]))
                # file = text_create(key)
                if key == "actionID" and fa_key == "clickPosEvents":
                    file = text_create(key)
                    if js[key] == "abc":
                        file.write('clickPosEvents -> actionID: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                        break
                    else:
                        file.write('clickPosEvents -> actionID: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
    else:
        def_name = sys._getframe().f_code.co_name
        file = text_create(def_name)
        file.write(def_name + ' :数据格式有问题' + '\n')
        file.close()
        return False


def Error_Up_50bang(js):
    """
    对应脚本S004，主动上报错误
    :param js:
    :return:
    """
    if isinstance(js, dict):  # 判断是否是字典类型isinstance 返回True false
        global fa_key
        for key in js:
            if isinstance(js[key], dict):  # 如果dic_json[key]依旧是字典类型
                fa_key = key
                Error_Up_50bang(js[key])

            elif isinstance(js[key], list):
                fa_key = key
                len_list_js = len(js[key])
                for j in range(0, len_list_js):
                    Error_Up_50bang(js[key][j])
            else:
                # print(str(key) + " : " + str(js[key]))
                # file = text_create(key)
                if key == "tag" and fa_key == "error":
                    file = text_create(key)
                    if js[key] == "Danny":
                        file.write('error -> tag: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                        break
                    else:
                        file.write('error -> tag: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
    else:
        def_name = sys._getframe().f_code.co_name
        file = text_create(def_name)
        file.write(def_name + ' :数据格式有问题' + '\n')
        file.close()
        return False


# def Tag_Data_50bang(js):
#     """
#     对应脚本S005，tag事件
#     :param js:
#     :return:
#     """
#     if isinstance(js, dict):  # 判断是否是字典类型isinstance 返回True false
#         for key in js:
#             if isinstance(js[key], dict):  # 如果dic_json[key]依旧是字典类型
#                 Tag_Data_50bang(js[key])
#
#             elif isinstance(js[key], list):
#                 len_list_js = len(js[key])
#                 for j in range(0, len_list_js):
#                     Tag_Data_50bang(js[key][j])
#             else:
#                 # print(str(key) + " : " + str(js[key]))
#                 # file = text_create(key)
#                 if key == "tag":
#                     file = text_create(key)
#                     if js[key] == "danny":
#                         file.write('tag: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
#                         # print(str(key) + " : " + str(js[key]))
#                         break
#                     else:
#                         file.write('tag: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
#                     file.close()
#     else:
#         def_name = sys._getframe().f_code.co_name
#         file = text_create(def_name)
#         file.write(def_name + ' :数据格式有问题' + '\n')
#         file.close()
#         return False


def ActionID_Data_50bang(js):
    """
    对应脚本S006，计数事件统计值
    :param js:
    :return:
    """
    if isinstance(js, dict):  # 判断是否是字典类型isinstance 返回True false
        global fa_key
        for key in js:
            if isinstance(js[key], dict):  # 如果dic_json[key]依旧是字典类型
                fa_key = key
                ActionID_Data_50bang(js[key])

            elif isinstance(js[key], list):
                fa_key = key
                len_list_js = len(js[key])
                for j in range(0, len_list_js):
                    ActionID_Data_50bang(js[key][j])
            else:
                # print(str(key) + " : " + str(js[key]))
                # file = text_create(key)
                if key == "actionID" and fa_key == "action":
                    file = text_create(key)
                    if js[key] == "ABC":
                        file.write('action -> actionID: ' + str(js[key]) + '  ' + '期望值存在: PASS' + '\n')
                        # print(str(key) + " : " + str(js[key]))
                        break
                    else:
                        file.write('action -> actionID: ' + str(js[key]) + '  ' + '期望值不存在: FAIL' + '\n')
                    file.close()
    else:
        def_name = sys._getframe().f_code.co_name
        file = text_create(def_name)
        file.write(def_name + ' :数据格式有问题' + '\n')
        file.close()
        return False



# js = collections.OrderedDict(dict(js))
# js_Data_50bang(js)
