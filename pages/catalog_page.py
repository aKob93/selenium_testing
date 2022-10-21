from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CatalogPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    tvs_and_monitors = '/html/body/div[1]/div[5]/div[2]/ol/li[2]/span'  # локатор телевизоров
    left_min_price = '//*[@id="mfilter-opts-price-min"]'  # локатор минимальной цены
    right_max_price = '//*[@id="mfilter-opts-price-max"]'  # локатор максимальной цены
    right_max_diagonal = '//*[@id="filter"]/ul/li[6]/div[2]/div/div/div/div/div[2]/div/span[2]'  # макс диагональ
    button_smarttv = '//*[@id="mfilter-content-wrapper-7"]/div/div/div/div/div'  # локатор выбора смарттв
    sort_filter = '//*[@id="input-sort"]'  # локатора фильтра
    cart = '//*[@id="products"]/div[2]/div/div/div[4]/div[5]/button'  # локатор корзины
    go_cart = '//*[@id="OrderContainer"]/div/center/div/div/a'  # локатора перехода в корзину
    name_product_loc = '//*[@id="products"]/div[2]/div/div/div[4]/div[1]'  # локатор имено товара
    price_product_loc = '//*[@id="products"]/div[2]/div/div/div[4]/div[4]/div/span[1]'  # локатора цены товара

    # Getters
    # получение кнопки тв и монииторы
    def get_tvs_and_monitor(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.tvs_and_monitors)))

    # получение максимальной диагональ
    def get_right_max_diagonal(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.right_max_diagonal)))

    # получение мин цены
    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.left_min_price)))

    # получение макс цены
    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.right_max_price)))

    # получение кнопки смарттв
    def get_button_smarttv(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_smarttv)))

    # получение кнопки фильтра
    def get_sort_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_filter)))

    # получение имено товара
    def get_name_product_loc(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_product_loc)))

    # получение цены товара
    def get_price_product_loc(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product_loc)))

    # получение корзины
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    # получение перехода в корзину
    def get_go_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.go_cart)))

    # Actions
    # выбор минимальной и максимальной цены
    def click_sidebar(self):
        self.get_min_price().send_keys(30000)
        self.get_max_price().send_keys(100000)
        print('Выбрана минимальная и максимальная цены')

    # изменение максимальной диагонали
    def choice_diagonal(self):
        self.driver.maximize_window()
        action = ActionChains(self.driver)
        diagonal_right = self.get_right_max_diagonal()
        action.click_and_hold(diagonal_right).move_by_offset(-25, 0).release().perform()
        print('Максимальная диагональ выбрана')

    # нажатие на кнопки выборв смарттв
    def choice_smarttv(self):
        scroll_origin = ScrollOrigin.from_element(self.get_button_smarttv())
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 500).perform()
        self.get_button_smarttv().click()
        print('Кнопка выбора смарттв выбрана')

    # обновление страницы
    def update_page(self):
        self.driver.refresh()
        print('страница обновлена')

    # выбор фильтра
    def get_filter(self):
        self.driver.execute_script('window.scrollTo(0, -100)')
        self.get_sort_filter().click()
        self.get_sort_filter().send_keys(Keys.ARROW_DOWN * 2)
        print('Фильтра изменён')

    # нахождение имени и цены торвара
    def get_product(self):
        Base.name_product = self.get_name_product_loc().text
        Base.price_product = self.get_price_product_loc().text[6:]
        self.get_cart().click()
        self.get_go_cart().click()
        print('Имя и цены товара найдены')

    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_sidebar()
        self.choice_diagonal()
        self.choice_smarttv()
        self.update_page()
        self.get_filter()
        self.get_product()
