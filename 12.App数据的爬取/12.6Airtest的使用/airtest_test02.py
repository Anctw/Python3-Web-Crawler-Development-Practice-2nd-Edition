# -*- encoding=utf8 -*-
__author__ = "H"

from airtest.core.android import Android
from airtest.core.api import *
import logging

logging.getLogger("airtest").setLevel(logging.WARNING)

# device: Android = init_device('Android')
# is_locked = device.is_locked()
# print(f'is_locked: {is_locked}')
#
# if is_locked:
#     device.unlock()
#
# device.wake()
#
# app_list = device.list_app()
# print(f'app list: {app_list}')
#
# uuid = device.uuid
# print(f'uuid: {uuid}')
#
# display_info = device.get_display_info()
# print(f'display info: {display_info}')
#
# resolution = device.get_render_resolution()
# print(f'resolution: {resolution}')
#
# ip_address = device.get_ip_address()
# print(f'ip address: {ip_address}')
#
# top_activity = device.get_top_activity()
# print(f'top activity: {top_activity}')
#
# is_keyboard_shown = device.is_keyboard_shown()
# print(f'is keyboard shown: {is_keyboard_shown}')

"""获取当前设备
def device():
    return G.DEVICE
"""

"""获取所有设备"""
# print(G.DEVICE_LIST)
# # url = 'Android://192.168.10.180:5037/emulator-5554'
# url = 'android://127.0.0.1:5037/b5d2f0f'
# device: Android = connect_device(url)
# print(G.DEVICE_LIST)

"""执行命令行
@logwrap
def shell(cmd):
    return G.DEVICE.shell(cmd)
"""

# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)
# result = shell('cat /proc/meminfo')
# print(result)

"""启动和停止App
@logwrap
def start_app(package, activity=None):
    G.DEVICE.start_app(package, activity)

@logwrap
def stop_app(package):
    G.DEVICE.stop_app(package)
"""

# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)

# package = 'com.ss.android.ugc.aweme'
# start_app(package)
# sleep(10)
# stop_app(package)

"""安装和卸载App"""

# @logwrap
# def install(filepath, **kwargs):
#     return G.DEVICE.install_app(filepath, **kwargs)


# @logwrap
# def uninstall(package):
#     return G.DEVICE.uninstall_app(package)


"""截图
def snap_shot(filename=None, msg="", quality=ST.SNAPSHOT_QUALITY)
"""

# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)
# package = 'com.ss.android.ugc.aweme'
# start_app(package)
# sleep(10)
# snapshot("weixin.png", quality=30)


"""唤醒和回到首页
@logwrap
def wake():
    G.DEVICE.wake()

@logwrap
def home():
    G.DEVICE.home()
"""

# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)
# wake()
# home()

"""点击屏幕
@logwrap
def touch(v, times, **kwargs)
"""

# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)
# # touch(Template('tp1.png'), 1)
#
# touch((400, 600), times=2)

"""滑动
@logwrap
def swipe(v1, v2=None, vector=None, **kwargs)
"""
# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)
# home()
# swipe((200, 300), (900, 300))

"""放大缩小
@logwrap
def pinch(in_or_out="in", center=None, percent=0.5)
"""
# url = 'android://127.0.0.1:5037/b5d2f0f'
# connect_device(url)
# home()
# pinch(in_or_out="out", center=(300, 300), percent=0.4)

"""键盘事件
def keyevent(keyname, **kwargs)
"""
url = 'android://127.0.0.1:5037/b5d2f0f'
connect_device(url)
keyevent("HOME")

"""输入内容
@logwrap
def text(text, enter=True, **kwargs)
"""
