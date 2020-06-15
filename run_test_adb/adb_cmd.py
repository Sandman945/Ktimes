import os


# 连接设备
def adb_con():
    os.system("adb connect 127.0.0.1:62001")


# 获取app启动包名和启动名(⚠️ 手机需要先打开对应app)
def app_ran_pack_name__and_ran_name():
    os.system("adb shell dumpsys window windows | findstr mFocusedApp")


# 获取系统版本
def adb_version(devices_name):
    os.system("adb - s" + devices_name + "shell getprop ro.build.version.release")


if __name__ == '__main__':
    adb_con()
