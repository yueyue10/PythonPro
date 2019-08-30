import os
import time
from multiprocessing import Process
from threading import Thread

from appium_demo.utils import cmd_utils
from appium_demo.utils.cmd_utils import CmdCode


class AndroidAvd:
    # 是否有设备连接
    con_device = False

    def __init__(self, _emulator_path, _avd_name, _device_name):
        self._emulator_path = _emulator_path
        self._device_name = _device_name
        self._avd_name = _avd_name

    def start_avd_exe(self):
        if self.kill_adb():  # 如果模拟器已经启动，不需要再次启动
            self.start_avd(start_header='start')
            print("Android模拟器启动完成！")

    def start_avd_thread(self):
        if self.kill_adb():  # 如果模拟器已经启动，不需要再次启动
            thread_ = Thread(target=self.start_avd())
            thread_.start()
            print("Android模拟器启动完成！")

    def start_avd_process(self):
        if self.kill_adb():  # 如果模拟器已经启动，不需要再次启动
            p1 = Process(target=self.start_avd())
            p1.start()
            print('主进程', os.getpid())
            print("Android模拟器启动完成！")

    def start_avd(self, start_header=''):
        print("打开Android模拟器：")
        print("子进程：", os.getppid(), os.getpid())
        cmd_utils.cmd_system(CmdCode.start_avd % (start_header, self._emulator_path, self._avd_name), show_log=True)

    def kill_adb(self):
        if self.check_avd(device_name=self._device_name):
            print("Android模拟器已经启动！")
            return False
        else:
            cmd_utils.cmd_popen(CmdCode.kill_adb_service, show_log=True)
            cmd_utils.cmd_popen(CmdCode.start_adb_service, show_log=True)
            return True

    def kill_adb_port(self, port):
        print('关闭adb 进程')
        cmd = CmdCode.find_port_take_up % str(port)
        process_list = cmd_utils.cmd_popen(cmd, line=True)
        for pro in process_list:
            print(pro)
            pid = pro.split(" ")[-1]
            cmd_utils.cmd_popen(CmdCode.kill_process_by_pid % pid)
        time.sleep(2)

    def check_avd(self, device_name=''):
        device_open = False
        adb_devices = CmdCode.adb_devices
        adb_devices_line = cmd_utils.cmd_popen(adb_devices, line=True)
        if len(adb_devices_line) > 2:
            for adb in adb_devices_line[1:-1]:  # 去掉第一个和最后一个
                con_device_ = adb.replace('\n', '').replace('\t', '').replace('device', '')
                print('已连接设备：', con_device_)
                self.con_device = True
                if device_name == con_device_:
                    device_open = True
        else:
            print("暂无设备连接")
            self.con_device = False
        return device_open

    def confirmCon(self):
        while not self.con_device:
            time.sleep(1)
            self.check_avd()


def start_avd(start_style='process'):
    avd_name = 'Nexus_6P_API_26'
    device_name = 'emulator-5554'
    emulator_path = r'E:\Users\Android\sdk\tools\emulator.exe'
    avd = AndroidAvd(emulator_path, avd_name, device_name)
    if start_style == 'thread': avd.start_avd_thread()
    if start_style == 'process': avd.start_avd_process()
    if start_style == 'exe': avd.start_avd_exe()  # 这种方式会启动一个命令窗口


if __name__ == '__main__':
    start_avd()
