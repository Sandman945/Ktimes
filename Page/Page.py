from Page.login_page import Login_Page


class Page_Obj:
    def __init__(self, driver):
        self.driver = driver

    def return_login(self):
        # 登录页对象
        return Login_Page(self.driver)
