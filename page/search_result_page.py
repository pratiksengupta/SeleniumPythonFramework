import logging
import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from utilities.utils import Utils
import logging


class SearchFlightResult(BaseDriver):
    log=Utils.sample_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    SEARCH_FLIGHT_RESULT="//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"
    def filter_flight(self):
        time.sleep(10)

        stop = self.driver.find_element(By.XPATH, "//p[normalize-space()='1']")

        stop.click()
        #wait = WebDriverWait(self.driver, timeout=10)

        # this is with chatgpt help
        '''all_stop1=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='Flight-APP']/section/section[2]/section[1]/div[2]/div[2]/div")))
        desired_expected_data="1 Stop"
        actual_data=all_stop1.text
        assert desired_expected_data in actual_data, f"Expected: {desired_expected_data}, Actual: {actual_data}"'''

        # from youtube tutorial
        #all_stop1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
        #print(len(all_stop1))
    def get_search_flight_result(self):
        return self.wait_for_presence_all_element(By.XPATH, self.SEARCH_FLIGHT_RESULT)


