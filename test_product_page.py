from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_offer',["0", "1", "2", "3", "4", "5", "6", pytest.param(7, marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_go_to_login_page(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    #открываем страницу
    page.should_be_login_link()    
    #page.click_add_to_basket()   #нажимаем добавить в корзину
    #page.solve_quiz_and_get_code()   #решаем пример и получаем код
    #page.coders_at_work() #сравниваем данные при добавлении в корзину
    