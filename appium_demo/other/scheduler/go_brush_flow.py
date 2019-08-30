from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from appium_demo.log import save_log, init_log
from appium_demo.other.visitors.mogu_visitor import MoGuRequest
from appium_demo.utils.time_util import now_datetime

scheduler = BlockingScheduler()


def job_brush_flow():
    '''
    访问博客
    采集频率：1分整倍数，就执行这个函数
    '''
    init_log(_log_path='', _log_name='brush_flow.log', _filemode='a')
    save_log("_________brush start_________", now_datetime())
    mogu = MoGuRequest()
    mogu.start(_type='mogu')
    save_log("_________brush end_________\n", now_datetime())


def start_scheduler():
    trigger = CronTrigger(day_of_week='mon-sun', hour='9-18', minute='45')
    scheduler.add_job(job_brush_flow, trigger)  # 根据需要进行设置
    scheduler.start()


if __name__ == '__main__':
    print('任务启动')
    start_scheduler()

# pyinstaller -F  *.py
# pyinstaller -F appium_demo/other/scheduler/go_brush_flow.py
# .\go_brush_flow.exe
