from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import pytest
import time

class ProductPage(BasePage): 
 def click_add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()
       # return LoginPage(browser=self.browser, url=self.browser.current_url)      
 def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
 def coders_at_work(self):
    element=self.browser.find_element(*BasketPageLocators.CODERS_TEXT)
    coders = element.text
    assert coders=="Coders at Work","Book name error"
 def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"
 def is_disappeared(self):
    assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"