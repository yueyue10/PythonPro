"""
日志输出模块
"""
import logging
import os


class LogConfig:
    fmt_style = '%(asctime)s  %(module)s/%(filename)s:%(lineno)d  %(message)s'
    log_path = r'E:\Users\Github\MyApplication\python_project\python_demo\appium_demo\log\data'
    log_name = 'error.log'
    INIT_LOG = False


def init_log(_log_path=LogConfig.log_path, _log_name=LogConfig.log_name, _filemode='w'):
    '''配置方法一：保存日志到文件不会输出到控制台'''
    LogConfig.INIT_LOG = True
    LogConfig.log_path = _log_path
    LogConfig.log_name = _log_name
    logging.basicConfig(level=logging.ERROR, filename=os.path.join(LogConfig.log_path, LogConfig.log_name),
                        filemode=_filemode,
                        # 模式:有w和a
                        # w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=LogConfig.fmt_style)
    print("log.init配置log成功")


'''配置方法二：输出日志到控制台不会输出到文件'''


# logging.basicConfig(level=logging.DEBUG,
#                     format=LogConfig.fmt_style)
#
# --------------------测试一------------------------------
# 为了将日志输出到控制台和输出到文件进行分离：
#
# 使用上面的配置，使用下面的测试代码进行测试：
# 1.在别的类中使用下面的测试代码:
# logging.debug("debug") #输出到控制台
# TestLog().e("出错了")    #输出到文件
# 2.输出>>>>>>>>>>>>
# 2019-07-25 14:46:11,956  multi_appium/multi_appium.py:53  debug
# 2019-07-25 14:46:11,966  logs/logs.py:46  出错了
# 3.结果>>>>>>>>>>>>
# 虽然实现了目的，但是输出到文件的日志定位路径失败


#
# --------------------测试二------------------------------
# 为了测试将日志保存到固定文件夹,使用网上找到的logger.MyLog进行测试
# 1.执行logs_test中的测试三代码test()
# 2.结果>>>>>>>>>>>可以将文件保存到log/data/logs_test中,但是日志定位错误,只能定位到日志输出原始位置.
#
# --------------------测试三------------------------------
# 借鉴上面测试二的部分代码进行折中处理:
# 目的: 不输出日志到控制台,只保存到文件.
# 1.使用上面的配置方法一
# 2.优化logging.basicConfig,将filename修改为文件全路径
# 3.在需要的时候执行:logging.info("输出日志")即可
# 4:结果:控制台没有输出,保存的日志文件在log/data/error.log中

def save_log(*objects):
    if not LogConfig.INIT_LOG:
        init_log()
    try:
        strings = []
        for obj in objects:
            try:
                strings.append(str(obj))
            except Exception as e:
                print('strings.append错误', e)
        logging.error("".join(strings))
    except Exception as e:
        print('save_log错误', e)
