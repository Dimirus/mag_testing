from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage

class ProductPage(BasePage):
    """Class ProductPage is inherited from the BasePage class. ProductPage describes PageObject "ProductPage". """
    #class attributes:
    chosed_name = ''
    chosed_price = ''

    def add_to_basket(self):
        """Add item into basket"""
        add_link = self.browser.find_element(*ProductPageLocators.ADD_LINK)
        # * means that we must uppack tuple
        add_link.click()

    def cost_is_price(self):
        """Сompare price of the book we put in the basket with the one in the success message"""
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert self.chosed_price in added_price, f"Added book price in basket not correct.Should be <{self.chosed_price}>,but in fact <{added_price}>"

    def item_in_box(self):
        """Сompare the title of the book we put in the basket with the one in the success message"""
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        assert self.chosed_name == added_name, f"Added book isn`t chosed book. Should be <{self.chosed_name}>,but in fact <{added_name}>"

    def message_should_be_disappeared(self):
        """Negative testing. Success message should be disappeared. """
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def remember_name_and_price(self):
        """Remember title and price book we will put on the basket"""
        self.chosed_name = self.browser.find_element(*ProductPageLocators.CHOSED_NAME).text
        self.chosed_price = self.browser.find_element(*ProductPageLocators.CHOSED_PRICE).text

    def should_not_be_success_message(self):
        """Negative testing. There should be no success message"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def take_a_sale(self):
        """Solve a quize from creators of course"""
        self.solve_quiz_and_get_code()

