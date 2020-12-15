from .pages.product_page import ProductPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      #открываем страницу
    page.click_add_to_basket()   #нажимаем добавить в корзину
    page.solve_quiz_and_get_code()   #решаем пример и получаем код
    #page.coders_at_work() #сравниваем данные при добавлении в корзину
    page.is_disappeared()