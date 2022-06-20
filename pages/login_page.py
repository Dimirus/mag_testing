from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    """Class LoginPage is inherited from the BasePage class. LoginPage describes PageObject "LoginPage". """

    def register_new_user(self, email, password):
        """Performing user registration"""
        email_link = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_link.send_keys(email)
        password1_link = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_link.send_keys(password)
        password2_link = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_link.send_keys(password)
        submit_register_link = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit_register_link.click()

    def should_be_login_url(self):
        """checking is there a login substring in the browser url line"""
        assert 'login' in self.browser.current_url, "url not right" 

    def should_be_login_form(self):
        """checking is login form on the page"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not here"

    def should_be_register_form(self):
        """checking is registration form on the page"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not here"

    def should_be_login_page(self):
        """checking is this page is a login page"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
