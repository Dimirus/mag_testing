from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #this is a pair, 
        #tuple of (how_to_find, what_to_find)
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")

    
class ProductPageLocators():
        ADD_LINK = (By.CLASS_NAME, "btn-add-to-basket")
        ADDED_NAME = (By.CSS_SELECTOR, ".alert:first-child strong")
        ADDED_PRICE = (By.CSS_SELECTOR, " .alertinner p strong")
        CHOSED_NAME = (By.XPATH, "//h1")
        CHOSED_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
        SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:first-child")
        
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #this is a pair,
        #tuple of (how_to_find, what_to_find)
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():    
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    