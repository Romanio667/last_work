from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium import webdriver 
import pytest
import time

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                  #открываем страницу
    page.should_be_login_link()  #должна быть ссылка на логин
    page.go_to_login_page()      #переходим к странице авторизации

    
@pytest.mark.need_review 
def test_guest_can_add_product_to_basket(browser):
       link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       page = ProductPage(browser, link)
       page.open()
       page.click_add_to_basket()     #нажимаем добавить в корзину
       
@pytest.mark.need_review 
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    #открываем страницу
    page.should_be_login_link()    #должна быть ссылка на логин
    page.go_to_basket_page()       #переход к корзине
    pageB = BasketPage(browser,browser.current_url)
    pageB.open()    
    pageB.should_be_basket_empty() #проверка корзины на пустоту
    pageB.should_be_text_empty()   

class TestUserAddToBasketFromProductPage():   
    @pytest.fixture(scope="function", autouse=True)  
    def setup(self,browser):
       link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       page = ProductPage(browser, link)
       page.open()
       page.go_to_login_page()     #переходим к странице авторизации
       page1 = LoginPage(browser,browser.current_url)
       page1.open()
       email=str(time.time())+"@fakemail.org"
       password="123errere324fdr"
       page1.register_new_user(email,password) #Регистрация пользователя
       page1.should_be_authorized_user()       #Проверка на авторизацию
 
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
       link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       page = ProductPage(browser, link)
       page.open()
       page.click_add_to_basket() #Доабвление товара в корзину