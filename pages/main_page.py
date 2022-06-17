from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
class MainPage(BasePage):
    
    def go_to_login_page(self):
        
        login_link = self.browser.find_element(*MainPageLocators) 
        # * means that we must uppack tuple
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators), "Login link is not presented"