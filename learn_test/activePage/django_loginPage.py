from selenium.webdriver.common.by import By
import sys
sys.path.append("..")
from basePage.django_BasePage import BasePage

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