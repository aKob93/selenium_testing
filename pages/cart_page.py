from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_product_cart = '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[3]/a'  # локатор имени товара
    price_product_cart = '//*[@id="total_sub_total"]/span[2]/nobr'  # локатор цены товара

    # Getters
    # получение имени товара
    def get_name_product_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product_cart)))

    # получение цены товара
    def get_price_product_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product_cart)))

    # Actions
    # проверка на совпадение имён с прошлой страницы
    def assert_name_product(self):
        name_product_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                                 ((By.XPATH, self.name_product_cart))).text
        assert Base.name_product == name_product_cart
        print('Проверка на совпадение имени товара пройдена')

    # проверка на совпадение цены с прошлой страницы
    def assert_price_product(self):
        price_product_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                                  ((By.XPATH, self.price_product_cart))).text
        assert Base.price_product == price_product_cart
        print('Проверка на совпадение цены товара пройдена')

    # Methods

    def asser_product(self):
        self.get_current_url()
        self.assert_name_product()
        self.assert_price_product()
        self.assert_url('https://www.cifrus.ru/basket.php')
        self.create_screenshot()

