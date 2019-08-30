# coding=utf-8
import logging
import time
from multiprocessing import Process

from appium import webdriver

from appium_demo import AppConfig, desired_caps
from appium_demo.base.appelement import AppElement
from appium_demo.utils import cmd_utils
from appium_demo.utils.cmd_utils import CmdCode


class AppiumService:

    def kill_appium(self, port):
        print('关闭Appium 进程')
        cmd = CmdCode.find_port_take_up % str(port)
        process_list = cmd_utils.cmd_popen(cmd, line=True, show_log=False)
        if type(process_list) == str and process_list:
            pid = process_list.split(" ")[-1]
            cmd_utils.cmd_popen(CmdCode.kill_process_by_pid % str(pid), show_log=False)
        else:
            for pro in process_list:
                print(pro)
                pid = pro.split(" ")[-1]
                cmd_utils.cmd_popen(CmdCode.kill_process_by_pid % str(pid), show_log=False)
        time.sleep(2)

    def appium_start(self, js_path, host, port):
        '''方法一：通过appium方式 启动appium server
            proc.wait() 有日志，经常无响应。即使启动服务以后也不能用
            proc.communicate() 无日志，不能用。
        '''
        print('开始启动Appium Service')
        cmd = CmdCode.node_start_appium % (js_path, host, port)
        cmd_utils.process_popen(cmd, show_log=True)

    def start_appium_process(self, js_path, host, port):
        p1 = Process(target=self.node_start_appium(js_path, host, port))
        p1.start()
        print("Appium服务启动完成！")

    def node_start_appium(self, js_path, host, port):
        '''方法二：通过node方式 启动appium server
            os.system 执行没有日志，但是服务可以使用
            os.popen 有日志，但是不成功
        '''
        print('开始启动Appium Service')
        cmd = CmdCode.node_start_appium % (js_path, host, port)
        cmd_utils.cmd_system(cmd, show_log=False)


def start_service():
    js_path = r"C:\Progra~1\Appium\resources\app\node_modules\appium\build\lib\main.js"
    host = '127.0.0.1'
    port = 4723
    app_service = AppiumService()
    app_service.kill_appium(port)
    # app_service.appium_start(js_path, host, port)
    app_service.node_start_appium(js_path, host, port)
    # app_service.start_appium_process(js_path, host, port)


def con_device():
    print("\n连接模拟器...")
    con_ = False
    while not con_:
        try:
            AppElement.driver = webdriver.Remote(AppConfig.service_path, desired_caps)
            print("连接成功")
            con_ = True
        except Exception as e:
            time.sleep(15)
            print("正在重新连接", e)


if __name__ == '__main__':
    start_service()
