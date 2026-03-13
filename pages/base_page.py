import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Дождаться видимости элемента')
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Дождаться исчезновения элемента')
    def wait_for_element_not_visible(self, locator, timeout=None):
        #ожидание, пока элемент не станет невидимым
        if timeout is None:
            wait = self.wait
        else:
            wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click(self, locator):
        self.wait_for_clickable(locator).click()

    @allure.step('Заполнить поле')
    def fill_field(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Перетащить ингредиент')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_for_element(locator).text

    @allure.step('Проверить отображение элемента')
    def is_displayed(self, locator):
        return self.wait_for_element(locator).is_displayed()