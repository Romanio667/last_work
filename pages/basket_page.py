from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import pytest
import time

class BasketPage(BasePage): 
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BUTTON_OFORMLENIE),"Oformlenie button is presented, but should not be"
    def should_be_text_empty(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
        text = basket.text
        assert (text=="Your basket is empty. Continue shopping"),"Корзина не пуста"