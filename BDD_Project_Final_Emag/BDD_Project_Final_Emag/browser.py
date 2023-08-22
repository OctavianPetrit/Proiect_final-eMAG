# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class Browser():
#     s = Service(ChromeDriverManager().install())
#     chrome = webdriver.Chrome(service=s)
#     chrome.maximize_window()
#     chrome.implicitly_wait(5)
#     chrome.set_page_load_timeout(10)
#
#     def close(self):
#         self.chrome.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# from seleniumbase import Driver
# driver = Driver(browser="chrome",headless=False)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdrivermanager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
# driver.get("http://www.python.org")

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.python.org")
import unittest
from seleniumbase import Driver
class Browser(unittest.TestCase):
    # s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)
    chrome = Driver(browser="chrome", headless=False)
    # chrome.get("http://www.emag.ro")
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    chrome.set_page_load_timeout(10)
    chrome.maximize_window()
    chrome.delete_all_cookies()

    def close(self):
        self.chrome.delete_all_cookies()
        self.chrome.close()