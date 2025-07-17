from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
keyevent("HOME")
poco("App5").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
    "com.goldze.mvvmhabit:id/content").offspring("android.support.v7.widget.RecyclerView").wait_for_appearance(10)

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
    "com.goldze.mvvmhabit:id/content").offspring("android.support.v7.widget.RecyclerView").child(
    "com.goldze.mvvmhabit:id/item")[8].swipe([0, -0.2], duration=1)
