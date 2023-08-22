# from browser import Browser
# # from pages.advanced_search_page import Advanced_search_page
# from pages.home_page import HomePage

from pages.home_page import HomePage
from pages.product_page import ProductsPage
# from pages.secure_page import Secure_page
# from pages.forgot_password_page import Forgot_password_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.product_page = ProductsPage()
    context.home_page_object = HomePage()

def after_all(context):
    context.browser.close()
