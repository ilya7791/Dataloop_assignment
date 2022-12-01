from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_btn = (By.CSS_SELECTOR, "[data-track='gnSignin']")
        self.user_name_box = (By.ID, "login-email")
        self.next_btn = (By.CSS_SELECTOR, "[class='user-select-none']")
        self.password_box = (By.ID, "login-password")
        self.sign_in_btn = (By.CSS_SELECTOR, "[class='user-select-none']")

    def click_login_btn(self):
        self.click(self.login_btn)

    def insert_user_name(self, user_name):
        self.send_text(self.user_name_box, user_name)

    def click_next_btn(self):
        self.click(self.next_btn)

    def insert_user_password(self, user_password):
        self.send_text(self.password_box, user_password)

    def click_sign_in_btn(self):
        self.click(self.sign_in_btn)

    def perform_login(self, user_name, user_password):
        self.click_login_btn()
        self.insert_user_name(user_name)
        self.click_next_btn()
        self.insert_user_password(user_password)
        self.click_sign_in_btn()
