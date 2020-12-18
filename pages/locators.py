from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class  LoginPageLocators():
    LOGIN_FORM = (By.ID, "#login_form")
    REGISTER_FORM = (By.ID, "#register_form")
    EMAIL_INPUT=(By.CSS_SELECTOR, "[name=registration-email]")
    PASSWORD_INPUT=(By.CSS_SELECTOR, "[name=registration-password1]")
    PASSWORD_INPUT2=(By.CSS_SELECTOR, "[name=registration-password2]")
    BUTTON_REGIS = (By.CSS_SELECTOR, "[name=registration_submit]")
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-lg")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-safe:nth-child(1)")
class BasketPageLocators():
    BASKET_BUTTON_OFORMLENIE  = (By.CSS_SELECTOR, ".col-sm-offset-8>a")
    BASKET_LINK  = (By.CSS_SELECTOR, ".btn-group>a")
    CODERS_TEXT = (By.CSS_SELECTOR, "div.alertinner>strong")
    BASKET_TEXT  = (By.CSS_SELECTOR, "div#content_inner>p")
class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a.btn-default")