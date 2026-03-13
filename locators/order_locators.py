from selenium.webdriver.common.by import By


class OrderLocators:
    #счётчики (специфичные для страницы заказов)
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    #раздел "В работе"
    ORDERS_IN_PROGRESS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])")