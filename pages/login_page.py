from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
           
        # checking is there a login tweak in the browser url line
        assert 'login' in self.browser.current_url, "url not right" 

    def should_be_login_form(self):
        # checking is login form on the page
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not here"

    def should_be_register_form(self):
        # checking is registration form on the page
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not here"