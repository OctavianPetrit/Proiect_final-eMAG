from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class HomePage(Base_page):
    SEARCH_TEXT_BOX = (By.ID, "searchboxTrigger")
    SEARCH_BUTTON = (By.XPATH, "//i[@class='em em-search']")
    SEARCH_RESULTS = (By.XPATH, "//span[@class='title-phrasing title-phrasing-sm']")
    PRODUCT_BTN = (By.XPATH,"//div[@class='navbar-aux-content__departments']")
    SUBCATEGORY = (By.XPATH,"//span[normalize-space()='Laptop, Tablete & Telefoane']")
    SUBCATEGORY_DROPDOWN_PC = (By.XPATH, "//a[normalize-space()='Laptopuri si accesorii']")
    PRODUCT_MENU = (By.XPATH,"//a[@class='megamenu-item'][normalize-space()='Laptopuri']")
    ADD_CART = (By.XPATH, "//div[@class='container']//div[1]//div[1]//div[1]//div[4]//div[2]//form[1]//button[1]")
    CART = (By.XPATH, "//i[@class='em em-cart2 navbar-icon']")
    REMOVE = (By.XPATH, "//div[@class='line-item line-item-footer visible-xs visible-sm']//button[@class='btn btn-link btn-remove-product gtm_rp080219 remove-product'][normalize-space()='Sterge']")
    RETURN_TO_HOME = (By.XPATH, "//img[@alt='eMAG']")
    SELECT_PRODUCT = (By.XPATH, "//img[@alt='Telefon mobil Samsung Galaxy S23 Ultra, Dual SIM, 8GB RAM, 256GB, 5G, Green']")
    CONTINUE_BTN = (By.XPATH,"//a[@class=' btn btn-emag btn-secondary font-size-md btn-block btn-lg gtm_sn11312018']")
    EMAG_LOGO = (By.XPATH,"//img[@alt='eMAG']")
    # SUBCATEGORY1_AUTO_MOTO_RCA = (By.XPATH,"//span[contains(text(),'Auto, Moto')]")
    # SUBCATEGORY2_ANVELOPE_JANTE = (By.XPATH,"//a[normalize-space()='Anvelope & Jante']")
    # SUBCATEGORY3_ANVELOPE_AUTO = (By.XPATH,"//a[normalize-space()='Anvelope auto']")

    def emag_logo(self):
        self.chrome.find_element(*self.EMAG_LOGO)

    # @T1

    def navigate_to_home_page(self):
        self.chrome.get('https://www.emag.ro/')

    def set_product_search(self):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("samsung galaxy z flip")

    def search_results(self):
        result_list1 = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final1 = result_list1[0].text.replace(',', '')
        assert int(resultat_final1) > 50
        sleep(5)

    # @T2 @ parameter

    def set_product_search1(self):
        category_dropdown1 = Select(self.chrome.find_element(*self.PRODUCT_BTN))
        category_dropdown1.select_by_visible_text('Aspiratoare')
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("aspirator robot")

    def search_results1(self):
        result_list1 = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final2 = result_list1[0].text.replace(',', '')
        assert int(resultat_final2) > 500
        sleep(5)


    #reinterpretare a def-ului de mai sus pt a se putea folosi orice se produs, sa nu mai fie hardcodat
    def set_product_serch_with_parameter(self, product):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(5)

    def check_search_results(self):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final = result_list[0].text.replace(',', '')
        assert int(resultat_final) > 1
        sleep(5)

    # @T3 @outline, @parameter

    def set_product_search_with_parameter(self,product):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)
        sleep(5)

    def check_search_results_with_parameters(self,number_of_results):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final=result_list[0].text.replace(',', '')
        assert int(resultat_final) >= int(number_of_results)
        sleep(5)

    def choose_category(self,category_name):
        category_dropdown = Select(self.chrome.find_element(*self.PRODUCT_BTN))
        # category_dropdown1 = category_dropdown.select_by_visible_text(sub_menu)
        # category_dropdown2 = category_dropdown1.select_by_visible_text(sub_menu1)
        # category_dropdown3 = category_dropdown2.select_by_visible_text(category_name)
        category_dropdown.select_by_visible_text(category_name)
        sleep(5)


  # Feature: Select Product and add to cart

  # @TC1_select_product
    def set_product_search_product_s23_ultra(self):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("s23 ultra")

    def select_product_s23_ultra(self):
        list1=self.chrome.find_elements(*self.SELECT_PRODUCT)
        list1[0].click()
        sleep(7)

    def add_to_cart(self):
        self.chrome.find_element(self.chrome.find_element(By.XPATH, "//button[contains(text(),'Adauga in Cos')]'"))
        s23_ultra = self.chrome.find_element(*self.ADD_CART)
        s23_ultra.click()
        sleep(15)

    # @TC2_remove_product_negative_scenario_on_return_to_shop @ shop
    def click_cart_button(self):
        button=self.chrome.find_element(*self.CART)
        button.click()
        sleep(7)

    def remove_from_cart(self):
        self.chrome.find_element(*self.REMOVE).click()
        sleep(7)

    def continue_shop(self):
        shop=self.chrome.find_element(*self.CONTINUE_BTN)
        shop.click()