import time, pytest
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.parametrize('number_promo', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#@pytest.mark.skip
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

@pytest.mark.xfail 
#@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.add_to_basket() #execute page method-add item into basket
    page.should_not_be_success_message() #Check There is no success message

#@pytest.mark.skip    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.should_not_be_success_message() #Check There is no success message

@pytest.mark.xfail
#@pytest.mark.skip    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.add_to_basket() #execute page method-add item into basket
    page.message_should_be_disappeared() #Check that the message is disappeared

#@pytest.mark.skip     
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.skip 
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url) #initialize class constructor
    #with current browser and current url
    login_page.should_be_login_page() # using method of login_page
 
#@pytest.mark.skip  
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.go_to_basket_page() #execute page method-jump to basket page
    basket_page = BasketPage(browser, browser.current_url) #initialize class constructor
        #with current browser and current url
    basket_page.should_not_be_items_in_the_basket() # should be no items in the basket 
    basket_page.should_be_text_basket_is_empty() #should be message basket is empty
     