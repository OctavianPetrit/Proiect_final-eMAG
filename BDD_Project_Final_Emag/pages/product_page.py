# from selenium.webdriver.common.by import By
# from pages.base_page import Base_page
#
# class ProductsPage(Base_page):
#     RESULTS_TITLE = (By.XPATH, "//span[@class='title-phrasing title-phrasing-xl']")
#     VEZI_DETALII_COS_BTN = (By.XPATH, "//a[normalize-space()='Vezi detalii cos']")
#     ADD_TO_CART = (By.ID, "//div[@class='container']//div[1]//div[1]//div[1]//div[4]//div[2]//form[1]//button[1]")
#
#     def verify_results_contain_text(self, text):
#         title_list = self.chrome.find_elements(*self.RESULTS_TITLE)
#         for i in range(5):
#             title = title_list[i].text.lower()
#             self.assertTrue(text in title, 'Result does not contain search query')
#
#     def click_vezi_detalii_cos(self):
#         self.wait_and_click_elem_by_selector(*self.VEZI_DETALII_COS_BTN)
#
#     def add_to_cart(self, ):
#         self.chrome.find_element(self.ADD_TO_CART).click()