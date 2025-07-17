# -*- encoding=utf8 -*-
__author__ = "H"

from airtest.core.api import *
init_device()
auto_setup(__file__)
touch(Template(r"tpl1747486196391.png", record_pos=(0.353, -0.043), resolution=(1080, 2400)))
wait(Template(r"tpl1747486207807.png", record_pos=(-0.251, -0.932), resolution=(1080, 2400)))
swipe(Template(r"tpl1747486287121.png", record_pos=(0.006, 0.241), resolution=(1080, 2400)), vector=[-0.0131, -0.3522])
keyevent("HOME")
