from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link) #initialize Page Object, 
        #and pass into constructor exemplar of driver and url address 
    page.open() # open page with the help of class Base_page function
    page.remember_name_and_price() #remember_name_and_price of chosen book
    page.add_to_basket() #execute page method-add item into basket
    page.take_a_sale() # handle alert and take_a_sale
    time.sleep(3)
    page.item_in_box() # проверка Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
    page.cost_is_price() # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
    