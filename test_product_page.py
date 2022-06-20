import time, pytest, random
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

class TestUserAddToBasketFromProductPage():
    """Tests for adding items to the basket as a registered user"""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Generate email and password, open login page and register new user"""
        email = "D" + str(random.randint(0,999)) + "@fakemail.org"
        password = str(time.time()) + "jacfsl812"
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser,link) #initialize Page Object, 
            #and pass into constructor exemplar of driver and url address 
        page.open() # open page with the help of class Base_page function
        page.register_new_user(email, password) #register new user
        page.should_be_authorized_user() #check if user autorized

    def test_user_cant_see_success_message(self, browser):
        """Negative testing. User shouldn`t see success message after jump to product page."""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link) #initialize Page Object, 
            #and pass into constructor exemplar of driver and url address 
        page.open() # open page with the help of class Base_page function
        page.should_not_be_success_message() #Check There is no success message

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Testing user can add product to the basket from product page"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link) #initialize Page Object, 
            #and pass into constructor exemplar of driver and url address 
        page.open() # open page with the help of class Base_page function
        page.remember_name_and_price() #remember_name_and_price of chosen book
        page.add_to_basket() #execute page method-add item into basket
        page.item_in_box() # Test message, which talks that item in basket. Name of item should be
            #the same as the product that we added to the basket.
        page.cost_is_price() # Test message, which talks about cost of item in basket. Cost of 
            #item in basket should be match the price of the item that we added to the basket.

@pytest.mark.need_review
@pytest.mark.parametrize('number_promo', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number_promo):
    """Testing guest can add product to the basket from product page"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_promo}"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.remember_name_and_price() #remember_name_and_price of chosen book
    page.add_to_basket() #execute page method-add item into basket
    page.take_a_sale() # handle alert and take_a_sale
    time.sleep(3)
    page.item_in_box() # Test message, which talks that item in basket. Name of item should be
        #the same as the product that we added to the basket.
    page.cost_is_price() # Test message, which talks about cost of item in basket. Cost of 
        #item in basket should be match the price of the item that we added to the basket.


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Negative testing. Guest will see success message after add item to the basket from product page"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.add_to_basket() #execute page method-add item into basket
    page.should_not_be_success_message() #Check There is no success message

def test_guest_cant_see_success_message(browser):
    """Guest should not see success message after jump to product page"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.should_not_be_success_message() #Check There is no success message

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Negative testing. Success message after add item to the basket from product page not disappear"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.add_to_basket() #execute page method-add item into basket
    page.message_should_be_disappeared() #Check that the message is disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    """Check if the guest can see the login link on product page"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review 
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Check if the guest can go to the login page from product page"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url) #initialize class constructor
    #with current browser and current url
    login_page.should_be_login_page() # using method of login_page

@pytest.mark.need_review   
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Check that the user will not see the items in the basket opened from the product page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.go_to_basket_page() #execute page method-jump to basket page
    basket_page = BasketPage(browser, browser.current_url) #initialize class constructor
        #with current browser and current url
    basket_page.should_not_be_items_in_the_basket() # should be no items in the basket 
    basket_page.should_be_text_basket_is_empty() #should be message basket is empty

