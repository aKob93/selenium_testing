import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sidebar_button = '//div[@id="sidebar-btn"]'  # локатор выбора категорий
    button_tvs_and_monitors = '//a[@href="/catalog/50"]'  # локатора тв и мониторов
    button_smartphones = '//a[@href="/catalog/smartfony"]'  # локатора смартфонов

    # Getters
    # получние кнопки категорий
    def get_sidebar_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sidebar_button)))

    # получение кнопки тв и мониторы
    def get_tvs_and_monitors_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_tvs_and_monitors)))

    # получение кнопки смартфоны
    def get_smartphone_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_smartphones)))

    # Actions
    # нажатие на выбор категорий
    def click_sidebar(self):
        self.get_sidebar_button().click()
        print('Выбор категорий получен')

    # скрол страницы
    def window_scroll(self):
        scroll_origin = ScrollOrigin.from_element(self.driver.find_element(By.XPATH, self.button_smartphones))
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 500).perform()
        print('Скрол страницы')

    # Выбор тв и мониторов
    def click_tvs_and_monitors_button(self):
        self.get_tvs_and_monitors_button().click()
        print('Тв и мониторы выбраны')

    # Methods
    def select_product(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_sidebar()
        time.sleep(1)  # ставлю слип чтобы скролл не падал с ошибкой MoveTargetOutOfBoundsException
        self.window_scroll()
        time.sleep(1)  # Иногда выбирает приставки
        self.click_tvs_and_monitors_button()
