from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link) #initialize Page Object, 
#and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.go_to_login_page() #execute page method-jump to login page
    login_page = LoginPage(browser, browser.current_url) #initialize class constructor
    #with current browser and current url
    login_page.should_be_login_page() # using method of login_page

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

    