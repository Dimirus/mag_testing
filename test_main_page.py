import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    """Check if the guest can go from the main page to the login page"""
    def test_guest_can_go_to_login_page(self,browser):
        """Check if the guest can go to the login page from main page"""
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link) #initialize Page Object, 
            #and pass into constructor exemplar of driver and url address 
        page.open() # open page with the help of class Base_page function
        page.go_to_login_page() #execute page method-jump to login page
        login_page = LoginPage(browser, browser.current_url) #initialize class constructor
            #with current browser and current url
        login_page.should_be_login_page() # using method of login_page

    def test_guest_should_see_login_link(self,browser):
        """Check if the guest can see the login link on the main page"""
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Check that the user will not see the items in the basket opened from the main page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.go_to_basket_page() #execute page method-jump to basket page
    basket_page = BasketPage(browser, browser.current_url) #initialize class constructor
        #with current browser and current url
    basket_page.should_not_be_items_in_the_basket() # should be no items in the basket
    basket_page.should_be_text_basket_is_empty() #should be message basket is empty

