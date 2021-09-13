from selenium import webdriver
from time import sleep
import sys
sys.path.append('..')
from activePage.django_loginPage import LoginPage

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