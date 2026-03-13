import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.main_page import MainPage
import allure
from url import Url
from locators.base_locators import BaseLocators


class TestMain:
    @allure.title('Переход в конструктор')
    def test_go_to_constructor(self, browser):
        page = MainPage(browser)
        page.go_to_constructor()
        assert browser.current_url == Url.url_page

    @allure.title('Переход в ленту заказов')
    def test_go_to_feed(self, browser):
        page = MainPage(browser)
        page.go_to_feed()
        assert browser.current_url == Url.url_feed

    @allure.title('Открытие модального окна ингредиента')
    def test_open_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        assert page.is_displayed(BaseLocators.MODAL)

    @allure.title('Закрытие модального окна')
    def test_close_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        page.close_modal()
        assert not page.is_displayed(BaseLocators.MODAL)

    @allure.title('Счётчик ингредиента увеличивается')
    def test_counter_increases(self, browser):
        page = MainPage(browser)
        page.open_page(Url.url_page)
        counter_text = page.get_sauce_counter()
        initial = int(counter_text) if counter_text else 0
        page.add_bun()
        page.add_sauce()
        counter_text = page.get_sauce_counter()
        final = int(counter_text) if counter_text else 0
        assert final > initial