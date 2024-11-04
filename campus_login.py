import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取登录信息
login_url = config['login']['url']
username = config['login']['username']
password = config['login']['password']

# 创建WebDriver实例（无需指定driver_path）
# driver = webdriver.Chrome()  # 确保chromedriver在系统路径中
# 创建WebDriver实例，使用Edge浏览器
driver = webdriver.Edge()  # 确保msedgedriver在系统路径中
# 打开校园网登录页面
driver.get(login_url)

# 等待页面加载
try:
    # 等待用户名输入框可用
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userid"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd"))
    )

    # 输入用户名和密码
    username_field.send_keys(username)
    password_field.send_keys(password)

    # 等待登录按钮可用并点击
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginsubmit"))
    )
    login_button.click()

    # 等待登录结果页面加载
    time.sleep(5)

    print("自动登录成功！")
except Exception as e:
    print("登录失败，请检查元素名称和网络连接。")
    print(f"错误信息: {e}")

# 关闭浏览器
driver.quit()
