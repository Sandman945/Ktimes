from appium import webdriver


def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['noReset'] = 'true'
    # app的信息
    desired_caps['appPackage'] = 'com.shuama.cardera'
    desired_caps['appActivity'] = '.ui.login.LoginActivity'
    # uiautomator2
    desired_caps['automationName'] = 'Uiautomator2'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
