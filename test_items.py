from selenium.webdriver.common.by import By
import pytest
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestMainPage():
    def test_add_bookmark_to_cart(self,browser):
        browser.get(link)
        # time.sleep(3)
        button = browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
        button_len = len(button)
        assert button_len >= 1 , 'BUTTON NOT FOUND'
        # ожидание, для визуальной оценки результата
        time.sleep(3)
        print('\nтест пройден успешно')
