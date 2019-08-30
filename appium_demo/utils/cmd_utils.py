import io
import os
import subprocess


class CmdTest:
    """
    cmd 窗口测试代码
    """
    # 在main.js目录下使用命令：     node main.js --address 127.0.0.1 --port 4723
    # 1.main.js文件位置：   C:\Program Files\Appium\resources\app\node_modules\appium\build\lib\main.js
    # 2.空格问题使用Progra~1替代
    # 3.启动成功截图如：appium_success.png所示
    # 4.cmd通用的命令为：   node C:\Progra~1\Appium\resources\app\node_modules\appium\build\lib\main.js --address 127.0.0.1 --port 4723

    # 查看4723端口占用信息：   netstat -aon |findstr 4723
    # 杀掉pid是23112的程序：   taskkill -f -pid 23112
    # 启动Android模拟器：   E:\Users\Android\sdk\tools\emulator.exe -netdelay none -netspeed full -avd Nexus_6P_API_26


class CmdCode:
    """
    window环境下的cmd命令
    """
    # 查找占用端口的进程     参数:port
    find_port_take_up = "netstat -aon |findstr %s"
    # 通过pid杀掉进程     参数:pid
    kill_process_by_pid = "taskkill -f -pid %s"
    # 通过node启动appium服务      参数：js_path, host, port
    node_start_appium = r'start /b node %s --address %s --port %s'
    adb_devices = 'adb devices'
    # 启动Android模拟器      参数：emulator_path ,avd_name
    start_avd = '%s %s -netdelay none -netspeed full -avd %s'
    kill_adb_service = 'adb kill-server'
    start_adb_service = 'adb start-server'
    # 打包成apk
    setup_exe = 'pyinstaller -F  %s'


def cmd_system(cmd_code, show_log=False):
    if show_log: print("_____执行cmd命令_____", cmd_code)
    cmd_pro = os.system(cmd_code)
    print("cmd_pro", cmd_pro)


# os.popen其实只是对subprocess.Popen
def cmd_popen(cmd_code, line=False, show_log=False):
    '''line:是否需要按集合输出'''
    if show_log: print("_____执行cmd命令_____", cmd_code)
    cmd_pro = os.popen(cmd_code)
    if line:
        cmd_read_lines = cmd_pro.readlines()
        cmd_pro.close()
        return cmd_read_lines
    else:
        cmd_read = cmd_pro.read()
        cmd_pro.close()
        print(cmd_read)
        return cmd_read


# 参考：https://www.jianshu.com/p/9d4e4cf06d23
def process_popen(cmd_code, show_log=False):
    if show_log: print("_____执行cmd命令_____", cmd_code)
    process = subprocess.Popen(cmd_code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # process.communicate()
    process.wait()
    if process.returncode == 0:
        try:
            stdout = io.TextIOWrapper(process.stdout, encoding='utf-8').read()
            stderr = io.TextIOWrapper(process.stderr, encoding='utf-8').read()
            print(stdout)
            print(stderr)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # Windows平台下使用start命令就可以不阻塞当前进程的执行程序
    cmd_system('start calc')
    print("完成")
