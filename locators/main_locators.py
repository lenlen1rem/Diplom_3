from selenium.webdriver.common.by import By


class MainLocators:
    #ингредиенты
    FLUOR_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]")
    SOUCE = (By.XPATH, "//img[contains(@alt, 'Соус Spicy-X')]")
    BURGER_CONSTR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
    
    #счетчики ингредиентов
    COUNT_SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class, 'counter_counter__num')]")
    
    #кнопка оформления заказа
    BTN_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")