from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element_o(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元祖(By.ID,ID属性值)
        :param timeout:超时时间
        :param poll:评率
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_element(*loc))

    def find_elements_o(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元祖(By.ID,ID属性值)
        :param timeout:
        :param poll:
        :return: 一组定位对象
        """
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_elements(*loc))

    def if_disp(self, loc):
        # 判断元素是否存在
        try:
            self.find_element_o(loc)
            return True
        except Exception as e:
            return False

    def click_element(self, loc):
        # 点击函数
        self.find_element_o(loc).click()

    def input_text(self, loc, text):
        """
        :param loc:
        :param text: 输入的内容
        :return:
        """
        ele = self.find_element_o(loc)
        ele.clear()
        ele.send_keys(text)

    def find_toast(self, message, timeout=3, poll=0.5):
        """
        :param poll:
        :param timeout:
        :param message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"
        element = self.find_element_o((By.XPATH, message), timeout, poll)
        return element.text

    def is_toast(self, message, timeout=3, poll=0.5):
        # 判断toast是否存在
        try:
            self.find_toast(message, timeout, poll)
            return True
        except Exception as e:
            return False
