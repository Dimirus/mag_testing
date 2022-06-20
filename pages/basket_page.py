from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_items_in_the_basket(self):
        """Negative testing.Check if there are no items in the basket"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE),\
            "Items in the basket is presented, but should not be"

    def should_be_text_basket_is_empty(self):
        """Check if there are text "no items in the basket" """
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
            "Message 'no items in the basket' is not presented, but should be"

