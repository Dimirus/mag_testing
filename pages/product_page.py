from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage

class ProductPage(BasePage):
    chosed_name = ''
    chosed_price = ''
    
    def add_to_basket(self):
        
        add_link = self.browser.find_element(*ProductPageLocators.ADD_LINK) 
        # * means that we must uppack tuple
        add_link.click()
        
    def remember_name_and_price(self):
        self.chosed_name = self.browser.find_element(*ProductPageLocators.CHOSED_NAME).text
        self.chosed_price = self.browser.find_element(*ProductPageLocators.CHOSED_PRICE).text
        
    def take_a_sale(self):
        self.solve_quiz_and_get_code()
    
    
    
    
    
    def item_in_box(self):
        
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        
        
        assert self.chosed_name in added_name, "Added book isn`t chosed book"
        
        
    def cost_is_price(self):
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        
        assert self.chosed_price in added_price, "Added book price in basket not correct"  
        