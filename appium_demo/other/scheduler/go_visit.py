from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from appium_demo.log import save_log, init_log
from appium_demo.other.visitors.kuaidaili_visitor import KuiDaiLi
from appium_demo.utils.time_util import now_datetime

scheduler = BlockingScheduler()


def scheduled_job_visit():
    '''
    访问博客
    采集频率：1分整倍数，就执行这个函数
    '''
    init_log(_log_path='', _log_name='scheduler.log', _filemode='a')
    save_log("_________visit start_________", now_datetime())
    KuiDaiLi().start()
    save_log("_________visit end_________\n", now_datetime())


def start_scheduler1():
    scheduler.add_job(scheduled_job_visit, 'cron', day_of_week='mon-sun', hour='11-14', minute='*/1')
    scheduler.start()


def start_scheduler2():
    trigger = CronTrigger(day_of_week='mon-sun', hour='11-14', minute='*/1')
    scheduler.add_job(scheduled_job_visit, trigger)  # 根据需要进行设置
    scheduler.start()


if __name__ == '__main__':
    print('任务启动')
    start_scheduler2()

# pyinstaller -F  *.py
# pyinstaller -F appium_demo/other/scheduler/go_visit.py
# .\go_visit.exe
