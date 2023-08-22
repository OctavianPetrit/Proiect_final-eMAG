from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_page

class HomePage(Base_page):
    SEARCH_TEXT_BOX = (By.ID, "searchboxTrigger")
    SEARCH_BUTTON = (By.XPATH, "//i[@class='em em-search']")
    SEARCH_RESULTS = (By.XPATH, "//span[@class='title-phrasing title-phrasing-sm']")
    PRODUCT_BTN = (By.XPATH,"//div[@class='navbar-aux-content__departments']")
    # SUBCATEGORY = (By.XPATH,"//span[normalize-space()='Laptop, Tablete & Telefoane']")
    # SUBCATEGORY_DROPDOWN_PC = (By.XPATH, "//a[normalize-space()='Laptopuri si accesorii']")
    PRODUCT_MENU = (By.XPATH,"//a[@class='megamenu-item'][normalize-space()='Laptopuri']")
    ADD_CART = (By.XPATH, "//div[@class='container']//div[1]//div[1]//div[1]//div[4]//div[2]//form[1]//button[1]")
    CART = (By.XPATH, "//i[@class='em em-cart2 navbar-icon']")
    REMOVE = (By.XPATH, "//div[@class='line-item line-item-footer visible-xs visible-sm']//button[@class='btn btn-link btn-remove-product gtm_rp080219 remove-product'][normalize-space()='Sterge']")
    RETURN_TO_HOME = (By.XPATH, "//img[@alt='eMAG']")
    SELECT_PRODUCT = (By.XPATH, "//img[@alt='Telefon mobil Samsung Galaxy S23 Ultra, Dual SIM, 8GB RAM, 256GB, 5G, Green']")
    CONTINUE_BTN = (By.XPATH,"//a[@class=' btn btn-emag btn-secondary font-size-md btn-block btn-lg gtm_sn11312018']")
    EMAG_LOGO = (By.XPATH,"//img[@alt='eMAG']")
    ACCEPT_COOKIES_BUTTON = (By.XPATH,'//button[@class="btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')
    # SUBCATEGORY1_AUTO_MOTO_RCA = (By.XPATH,"//span[contains(text(),'Auto, Moto')]")
    # SUBCATEGORY2_ANVELOPE_JANTE = (By.XPATH,"//a[normalize-space()='Anvelope & Jante']")
    # SUBCATEGORY3_ANVELOPE_AUTO = (By.XPATH,"//a[normalize-space()='Anvelope auto']")

    def emag_logo(self):
        emag_logo = self.chrome.find_element(*self.EMAG_LOGO)
        assert emag_logo.is_displayed() == True, "Error. Emag logo is not displayed"

    def navigate_to_home_page(self):
        self.chrome.get('https://www.emag.ro/')

    def set_product_search(self, product_name):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product_name)

    def search_results(self,number_of_results):
        result = self.chrome.find_element(*self.SEARCH_RESULTS).text
        final_result = result.replace(result[result.index("de"):],"").replace(result[result.index("rezultate"):],"").replace(" ","")
        assert int(final_result) >= int(number_of_results)


    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(5)

    def choose_category(self,category_name):
        pass
        self.chrome.find_element(*self.PRODUCT_BTN).click()
        self.chrome.find_element(By.XPATH,f'//span[text()="{category_name}"]//parent::a').click()

    # def add_to_cart(self):
    #     self.chrome.find_element(self.chrome.find_element(By.XPATH, "//button[contains(text(),'Adauga in Cos')]'"))
    #     s23_ultra = self.chrome.find_element(*self.ADD_CART)
    #     s23_ultra.click()
    #
    # # @TC2_remove_product_negative_scenario_on_return_to_shop @ shop
    # def click_cart_button(self):
    #     button=self.chrome.find_element(*self.CART)
    #     button.click()
    #
    # def remove_from_cart(self):
    #     self.chrome.find_element(*self.REMOVE).click()
    #
    # def continue_shop(self):
    #     shop=self.chrome.find_element(*self.CONTINUE_BTN)
    #     shop.click()