import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver=driver
    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")

        time.sleep(3)
    def wait_for_presence_all_element(self,locator_type,locator):
        wait = WebDriverWait(self.driver, timeout=10)

        list_of_element=wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_element
