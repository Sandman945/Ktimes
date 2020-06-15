from Base.Base import Base
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def phone_input(self, text):
        # 输入手机号码
        self.input_text(Page.input_phone, text)

    def pwd_input(self, text):
        # 输入密码
        self.input_text(Page.input_password, text)

    def click_login_btn(self):
        # 点击登录按钮
        self.click_element(Page.login_btn)
