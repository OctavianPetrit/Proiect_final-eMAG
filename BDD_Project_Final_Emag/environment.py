# from browser import Browser
# # from pages.advanced_search_page import Advanced_search_page
# from pages.home_page import HomePage

from pages.home_page import HomePage
# from pages.login_page import Login_page
# from pages.secure_page import Secure_page
# from pages.forgot_password_page import Forgot_password_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    # context.login_page = Login_page()
    context.home_page = HomePage()
    # context.secure_page = Secure_page()
    # context.forgot_password_page = Forgot_password_page()



def after_all(context):
    context.browser.close()
