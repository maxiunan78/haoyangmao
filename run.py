#!/usr/bin/env python
#-*- coding:utf-8 -*- 

#author:maxiunan

import time
import logging

import datetime
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("hello")


if __name__ == '__main__':
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用
    scheduler = BackgroundScheduler()
    # 采用阻塞的方式

    # 采用corn的方式
    scheduler.add_job(job, 'cron', hour='22', minute='30', timezone="Asia/Shanghai")
    '''
    year (int|str) – 4-digit year
    month (int|str) – month (1-12)
    day (int|str) – day of the (1-31)
    week (int|str) – ISO week (1-53)
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    hour (int|str) – hour (0-23)
    minute (int|str) – minute (0-59)
    econd (int|str) – second (0-59)

    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

    *    any    Fire on every value
    */a    any    Fire every a values, starting from the minimum
    a-b    any    Fire on any value within the a-b range (a must be smaller than b)
    a-b/c    any    Fire every c values within the a-b range
    xth y    day    Fire on the x -th occurrence of weekday y within the month
    last x    day    Fire on the last occurrence of weekday x within the month
    last    day    Fire on the last day within the month
    x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''

    scheduler.start()
    scheduler.print_jobs()
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)


    def my_listener(event):
        if event.exception:
            print('The job crashed :(')

        else:
            print('The job worked :)')


    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)




#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename=r'd:\log.txt',
#                     filemode='w')
#
#
# def aps_test():
#     print(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), '你好')
#
#
# def aps_test_name(name):
#     """
#     带参定时任务
#     :param name:
#     :return:
#     """
#     print(datetime.datetime.now().strftime('%Y-%m-%D %H-%M-%S'), name)
#
#
# def aps_test_param(number):
#     print('aps_test_param invoker....')
#     # 如果number == 0 ,这里会报错，报错信息会打印到日志文件log.txt中
#     # 虽然这儿会报错，但是定时任务并不会中断
#     print(10 / number)
#
#
# def job_listener(event):
#     """
#     APScheduler提供的监控功能
#     :param event:
#     :return:
#     """
#     if event.exception:
#         # print(dir(event))
#         print(event.job_id, '任务执行过程出错，发个邮件通知运维人员')
#     else:
#         # print('定时任务正常执行。。。。。')
#         pass
#
#
# scheduler = BlockingScheduler(timezone="Asia/Shanghai")
# # 添加一个定时任务， 使用cron触发器
# aps_test = scheduler.add_job(func=aps_test, trigger='cron', hour='22', minute='20')
# # print(aps_test)
# # 可以用来修改这个定时任务，比如间隔周期啥的
# # aps_test.modify()
#
# # 添加一个定时任务， 使用interval触发器
# scheduler.add_job(func=aps_test_name, args=('美女',), trigger='interval', seconds=10, id='id1')
#
# # 添加一个定时任务（只会执行1次），使用date触发器
# scheduler.add_job(func=aps_test_param, args=(10,), trigger='date', run_date='2022-03-11 20:01:01')
#
# # 添加一个定时任务，用来模拟定时任务中报错的情况
# # 每个job默认都有一个job_id, 不过默认的job_id 是一串随机字符串，没有可读性，这儿显示声明一个job_id 以便于定位问题job
# scheduler.add_job(func=aps_test_param, args=[0], trigger='interval', seconds=6, id='aps_test_param2')
# scheduler.print_jobs()
# # 添加监控
# scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
#
# # 日志
# scheduler._logger = logging
#
# scheduler.start()