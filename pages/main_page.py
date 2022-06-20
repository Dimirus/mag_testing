from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    """Class MainPage is inherited from the BasePage class. Class MainPage describes PageObject "MainPage". """
    def __init__(self, *args, **kwargs):
        # *args - unpacking list of arguments, 
        #**kwargs - unpacking dict with keyword(named) arguments
        super(MainPage, self).__init__(*args, **kwargs)
        # call constructor of parent class (Mainpage) and
        # pull him all arguments which has been received by MainPage

