import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base_page import BasePage
import allure
from locators.base_locators import BaseLocators


class AuthPage(BasePage):
    @allure.step('Выполнить авторизацию')
    def login(self, email, password):
        self.click(BaseLocators.BTN_LOGIN_ACC)
        self.fill_field(BaseLocators.FIELD_EMAIL, email)
        self.fill_field(BaseLocators.FIELD_PASSWORD, password)
        self.click(BaseLocators.BTN_LOGIN)