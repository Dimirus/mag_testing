from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link) #initialize Page Object, 
#and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.go_to_login_page #execute page method-jump to login page
    