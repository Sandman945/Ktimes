from selenium.webdriver.common.by import By

'''
  登录页
'''
# 手机号输入框
input_phone = (By.ID, "com.shuama.cardera:id/UI_AccountEditText")

# 密码输入框
input_password = (By.ID, "com.shuama.cardera:id/UI_PwdEditText")

# 登录按钮
login_btn = (By.ID, "com.shuama.cardera:id/UI_Login")

# 记住密码
save_pwd = (By.CLASS_NAME, "android.widget.CheckBox")

'''
  首页
'''
# 首页文本
index_text = (By.ID, "com.shuama.cardera:id/largeLabel")
