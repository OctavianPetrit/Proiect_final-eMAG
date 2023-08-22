# from selenium.webdriver.common.by import By
# from pages.base_page import Base_page
#
# class CartPage(Base_page):
#     SUBTOTAL = (By.XPATH, "//body[1]/div[3]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]")
#     REMOVE_FROM_CART= (By.XPATH, "//div[@class='placeholder vendors-container']//div//div[1]//div[2]//div[1]//div[2]//div[2]//button[1]")
#     COSUL_TAU_ESTE_GOL_MSG = (By.XPATH, "//p[@class='mrg-btm-none']")
#     CHECKOUT_BTN = (By.XPATH, "//a[normalize-space()='sa te intorci in magazin.']")
#
#     def total_price(self, expected_price):
#         self.chrome.find_element(*self.SUBTOTAL).text
#
#     def click_remove_link(self):
#         self.wait_and_click_elem_by_selector(*self.REMOVE_FROM_CART)
#
#     def verify_empty_cart_msg(self):
#         self.verify_element_is_displayed_by_selector(*self.COSUL_TAU_ESTE_GOL_MSG)
#
#     def click_checkout_btn(self):
#         self.wait_and_click_elem_by_selector(*self.CHECKOUT_BTN)
