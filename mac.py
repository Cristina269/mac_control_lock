import time
import Quartz
import os


def lock_status():
    d = Quartz.CGSessionCopyCurrentDictionary()
    riqi=time.strftime("%Y-%m-%d", time.localtime())
    shijian=time.strftime("%H:%M:%S", time.localtime())
    if 'CGSSessionScreenIsLocked' in d and d['CGSSessionScreenIsLocked'] == 1:
        # print('锁屏中')
        status = '日期：'+riqi+'\n'+'时间：'+shijian+'\n'+'锁屏中'
    else:
        status ='日期：'+riqi+'\n'+'时间：'+shijian+'\n'+'\n没有锁屏'
        # print('没有锁屏')
    return status


def into_sleep_mode():
    # 进入屏幕保护
    os.popen('open -b com.apple.ScreenSaver.Engine')
    # 进入睡眠
    os.popen('pmset displaysleepnow')
    return '已锁屏'


def enter_screen_saver():
    # 进入屏幕保护
    os.popen('open -b com.apple.ScreenSaver.Engine')
    return '已进入屏保'


