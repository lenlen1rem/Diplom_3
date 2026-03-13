import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base_page import BasePage
import allure
from locators.base_locators import BaseLocators
from locators.order_locators import OrderLocators

class OrderPage(BasePage):
    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        self.click(BaseLocators.BTN_MODAL_CLOSE)
        self.wait_for_element_not_visible(BaseLocators.MODAL)

    @allure.step('Получить номера заказов в работе')
    def get_orders_in_progress(self):
        return self.get_text(OrderLocators.ORDERS_IN_PROGRESS)

    @allure.step('Получить общий счётчик заказов')
    def get_total_count(self):
        return self.get_text(OrderLocators.TOTAL_ORDERS_COUNT)

    @allure.step('Получить счётчик заказов за сегодня')
    def get_today_count(self):
        return self.get_text(OrderLocators.TODAY_ORDERS_COUNT)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_text(OrderLocators.ID_ORDER)