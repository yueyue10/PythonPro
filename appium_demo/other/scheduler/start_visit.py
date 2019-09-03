from apscheduler.schedulers.blocking import BlockingScheduler

from log import save_log, init_log
from other.visitors.kuaidaili_visitor import KuiDaiLi
from utils.time_util import now_datetime

scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', day_of_week='mon-sun', hour='10-11', minute='*/1')
def scheduled_job_visit():
    '''
    访问博客
    采集频率：1分整倍数，就执行这个函数
    '''
    init_log(_log_path='', _log_name='scheduler.log', _filemode='a')
    save_log("_________visit start_________", now_datetime())
    KuiDaiLi().start()
    save_log("_________visit end_________\n", now_datetime())


if __name__ == '__main__':
    print('任务启动')
    scheduler.start()

# pyinstaller -F  *.py
# pyinstaller -F appium_demo/other/scheduler/start_visit.py
# .\start_visit.exe
