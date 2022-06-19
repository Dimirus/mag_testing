from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #this is a pair, 
        #tuple of (how_to_find, what_to_find)
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
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
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")