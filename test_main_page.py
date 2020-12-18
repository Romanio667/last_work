from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
 @pytest.mark.login
 def test_guest_can_go_to_login_page(self,browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()

 @pytest.mark.basket
 def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
    link = "http://selenium1py.pythonanywhere.com/"
    link2 = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_page()          # выполняем метод страницы — переходим на страницу корзины
    pageB = BasketPage(browser, link2)
    pageB.open()    
    pageB.should_be_basket_empty()
    pageB.should_be_text_empty()