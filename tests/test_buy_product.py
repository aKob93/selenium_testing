from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.cart_page import CartPage


def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=
                              "C:\\Users\\Aleksandr\\PycharmProjects\\selenium_testing\\utilities\\chromedriver.exe",
                              chrome_options=options)

    print('Start Test')

    mp = MainPage(driver)
    mp.select_product()

    cp = CatalogPage(driver)
    cp.select_product()

    cart_page = CartPage(driver)
    cart_page.asser_product()

    print('Finish Test')
