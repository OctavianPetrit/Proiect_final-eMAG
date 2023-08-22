# from selenium.webdriver.common.by import By
# from pages.base_page import Base_page
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
#
#
# class Login_page(Base_page):
#
#     LOGIN_PAGE = (By.XPATH,"//i[@class='em em-user2 navbar-icon']")
#     EMAIL_INPUT = (By.XPATH, "//input[@id='user_login_email']")
#     PASSWORD_INPUT= (By.XPATH, "//button[@id='user_login_continue']")
#     CONTINUA_BTN = (By.XPATH, "//button[@id='user_login_continue']")
#     LOGO_IMG = (By.XPATH, "//img[@alt='eMAG']")
#     ERROR_MSG = (By.XPATH, "//div[contains(text(),'Ai introdus greșit parola sau adresa de email. Te ')]")
#     CHECK_BOX = (By.XPATH, "//label[contains(text(),'Ține-mă minte')]")
#
#     def nav_home_page(self):
#         self.chrome.get('https://www.emag.ro/')
#
#
#
#     def navigate_to_login_page(self):
#         self.chrome.get('https://auth.emag.ro/user/login')
#
#     def set_email(self, email):
#         self.chrome.find_element(*self.EMAIL_INPUT, email)
#
#     def set_password(self, email):
#         self.chrome.find_element(*self.PASSWORD_INPUT, email)
#
#     def click_continua_btn(self):
#         self.chrome.find_element(*self.CONTINUA_BTN)
#
#     def click_logo_img(self):
#         self.chrome.find_element(*self.LOGO_IMG).click()
#         self.chrome.find_element(*self.CHECK_BOX).click()
#
#     def verify_error_msg(self):
#         self.chrome.find_element(*self.ERROR_MSG)
