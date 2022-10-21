import os
import datetime
import time


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.name_product: str
        self.price_product: str

    url = 'https://www.cifrus.ru'

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    def create_screenshot(self):
        """Method create screenshot"""
        date = str(datetime.datetime.now().strftime('%Y.%m.%d.%H.%M'))
        self.driver.maximize_window()
        time.sleep(1)
        if not os.path.exists('..\screen'):
            os.mkdir('..\screen')
        self.driver.save_screenshot(
            f'..\screen\screen_{date}.png')
        print('Скришот сохранён')

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')
