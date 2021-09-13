from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class BasePage(object):
    # 初始化
    def __init__(self, driver):
        self.base_url = 'http://127.0.0.1:8000/admin'
        self.driver = driver
        self.timeout = 5
    # 定义打开登录页面的方法
    def _open(self):
        url = self.base_url
        self.driver.get(url)
    # 定义open方法，调用_open()进行打开
    def open(self):
        self._open()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

class LoginPage(BasePage):
    username_loc = (By.ID, "id_username")
    password_loc = (By.ID, "id_password")
    login_loc = (By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=\"submit\"]")

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.find_element(*self.login_loc).submit()

def test_user_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    username = 'admin'
    password = 'admin123456'
    test_user_login(driver, username, password)
    sleep(3)
    driver.quit()