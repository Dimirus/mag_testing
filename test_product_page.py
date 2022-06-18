from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time, pytest
@pytest.mark.parametrize('number_promo', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

def test_guest_can_add_product_to_basket(browser,number_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_promo}"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.remember_name_and_price() #remember_name_and_price of chosen book
    page.add_to_basket() #execute page method-add item into basket
    page.take_a_sale() # handle alert and take_a_sale
    time.sleep(3)
    page.item_in_box() # Test message, which talks that item in basket. Name of item should be
    # the same as the product that we added to the basket.
    page.cost_is_price() # Test message, which talks about cost of item in basket. Cost of 
    #item in basket should be match the price of the item that we added to the basket.
     