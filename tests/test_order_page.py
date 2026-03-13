import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure


class TestOrder:
    @allure.title('Номер заказа отображается в "В работе"')
    def test_order_appears_in_progress(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        order_page = OrderPage(logged_in_browser)
        
        #создаем заказ на главной странице
        main_page.go_to_constructor()
        order_num = main_page.create_order()
        
        #переходим в ленту заказов и проверяем
        main_page.go_to_feed()
        in_feed = order_page.get_orders_in_progress()
        assert order_num == in_feed

    @allure.title('Счётчик "Всего" увеличивается')
    def test_total_counter_increases(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        order_page = OrderPage(logged_in_browser)
        
        #переходим в ленту заказов и запоминаем начальное значение
        main_page.go_to_feed()
        initial = int(order_page.get_total_count())
        
        #возвращаемся в конструктор и создаем заказ
        main_page.go_to_constructor()
        main_page.create_order()
        
        #снова переходим в ленту заказов и проверяем
        main_page.go_to_feed()
        updated = int(order_page.get_total_count())
        assert updated == initial + 1

    @allure.title('Счётчик "Сегодня" увеличивается')
    def test_today_counter_increases(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        order_page = OrderPage(logged_in_browser)
        
        main_page.go_to_feed()
        initial = int(order_page.get_today_count())
        
        main_page.go_to_constructor()
        main_page.create_order()
        
        main_page.go_to_feed()
        updated = int(order_page.get_today_count())
        assert updated == initial + 1