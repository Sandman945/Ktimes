import os
import sys
import time
import allure

sys.path.append(os.getcwd())
from Base.InitDiver import init_driver
# from Base.Read_Data import ret_yaml_data
from Base.Read_Data import yml_data_with_filename_and_key
from Page.Page import Page_Obj
import Page
import pytest


# def read_test_data():
#     list_data = []
#     test_Data = ret_yaml_data("login_data").get("Login_data")
#     for i in test_Data.keys():
#         list_data.append((i, test_Data.get(i).get("phone")
#                           , test_Data.get(i).get("password"),
#                           test_Data.get(i).get("expect")))
#     return list_data

def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)


@allure.feature('登录功能')
class Test_Login_Page:
    def setup(self):
        # 初始化对象
        self.driver = init_driver()
        self.login_obj = Page_Obj(self.driver).return_login()

    def teardown(self):
        self.driver.quit()

    # @allure.step(title="登录模块")
    # @pytest.mark.parametrize("test_num, phone, password, expect", read_test_data())
    # def test_login(self, test_num, phone, password, expect):
    #     # 输入手机号
    #     allure.attach('输入%s' % phone, '输入手机号')
    #     self.login_obj.phone_input(phone)
    #     # 输入密码
    #     allure.attach('输入%s' % password, '输入密码')
    #     self.login_obj.pwd_input(password)
    #     # 点击登录按钮
    #     allure.attach('', '点击登录按钮')
    #     self.login_obj.click_login_btn()
    #     if test_num == "输入正确的手机号正确的密码":
    #         self.login_obj.if_disp(Page.index_text)
    #         ele = self.login_obj.find_element_o(Page.index_text)
    #         self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)
    #         assert expect in ele.text
    #     elif test_num == "密码为空":
    #         self.login_obj.is_toast("请输入")
    #         toast_text = self.login_obj.find_toast("请输入")
    #         self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)
    #         assert expect in toast_text

    @allure.step("登录步骤")
    @pytest.mark.parametrize("args", data_with_key("Login_data"))
    @allure.story("登录功能测试用例")
    def test_login(self, args):
        test_num = data_with_key("Login_data")
        screen_name = args["screen_name"]
        phone = args["phone"]
        password = args["password"]
        # 输入手机号
        allure.attach('输入%s' % phone, '输入手机号')
        self.login_obj.phone_input(phone)
        # 输入密码
        allure.attach('输入%s' % password, '输入密码')
        self.login_obj.pwd_input(password)
        # 点击登录按钮
        allure.attach('点击', '点击登录按钮')
        self.login_obj.click_login_btn()
        time.sleep(1)
        self.driver.get_screenshot_as_file("./screen/%s.png" % screen_name)
        # 上传截图到报告
        allure.attach(open('./screen/' + screen_name + '.png', 'rb').read(), '截图', allure.attachment_type.PNG)
        if test_num == "test_login_001":
            self.login_obj.if_disp(Page.index_text)
            ele = self.login_obj.find_element_o(Page.index_text)
            assert args["expect"] in ele.text
        elif test_num == "test_login_002":
            assert self.login_obj.is_toast("请输入密码")
