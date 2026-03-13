import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base_page import BasePage
import allure
from url import Url
from locators.base_locators import BaseLocators
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators


class MainPage(BasePage):
    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.click(BaseLocators.BTN_CONSTRR)

    @allure.step('Перейти в ленту заказов')
    def go_to_feed(self):
        self.click(BaseLocators.BTN_ORDER_FEED)
        self.wait_for_element(BaseLocators.FEED_TITLE)

    @allure.step('Открыть модальное окно ингредиента')
    def open_ingredient_modal(self):
        self.click(MainLocators.FLUOR_BUN)
        self.wait_for_element(BaseLocators.MODAL)

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click(BaseLocators.BTN_MODAL_CLOSE)

    @allure.step('Добавить булку в конструктор')
    def add_bun(self):
        self.drag_and_drop(MainLocators.BUN, MainLocators.BURGER_CONSTR)

    @allure.step('Добавить соус в конструктор')
    def add_sauce(self):
        self.drag_and_drop(MainLocators.SOUCE, MainLocators.BURGER_CONSTR)

    @allure.step('Получить счётчик соуса')
    def get_sauce_counter(self):
        return self.get_text(MainLocators.COUNT_SPICY_X)

    @allure.step('Создать заказ')
    def create_order(self):
        #добавляем ингредиенты
        self.add_bun()
        self.add_sauce()
        
        #оформляем заказ
        self.click(MainLocators.BTN_ORDER)
        
        #получаем номер заказа и добавляем ведущий ноль
        order_number = self.get_text(OrderLocators.ID_ORDER)
        formatted_number = '0' + order_number
        
        #закрываем модальное окно
        self.close_modal()
        
        return formatted_number