import time

import pytest
import softest
from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By  # this is for fetching the by class
from selenium.webdriver.support.select import Select  # helps to select element from dropdown
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.search_result_page import SearchFlightResult
from page.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.sample_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    #@data(("BOM", "Dibrugarh", "15/05/2024", "1 Stop") )
    #@data(*Utils.read_data_from_excel("D:\\Selenium with Python last\\Learning Framework\\testdata\\Book1.xlsx","Sheet1"))
    @data(*Utils.read_data_from_csv("D:\\Selenium with Python last\\Learning Framework\\testdata\\tdatacsv.csv"))
    @unpack
    #@file_data("../testdata/testdata.json")
    #@file_data("../testdata/testyml.yaml")

    def test_search_flight(self,goingfrom,goingto,date,stop):
        # lp = LaunchPage(self.driver)
        search_flight_result = self.lp.searchflights(goingfrom,goingto,date)
        # lp.departfrom("New Delhi")
        # lp.enterdepartfromlocation("New Delhi")
        # lp.entergoingtolocation("Kolkata")
        # lp.enterdeparturedate("05/04/2024")
        # lp.clicksearchbutton()
        self.lp.page_scroll()
        # sf = SearchFlightResult(self.driver)
        search_flight_result.filter_flight()

        # For Choose date

        # time.sleep(10)
        #
        # stop=self.driver.find_element(By.XPATH,"//p[normalize-space()='1']")
        #
        # stop.click()

        # self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        #
        # time.sleep(3)

        wait = WebDriverWait(self.driver, timeout=10)
        #
        #
        #
        #
        #
        # #this is with chatgpt help
        # '''all_stop1=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='Flight-APP']/section/section[2]/section[1]/div[2]/div[2]/div")))
        # desired_expected_data="1 Stop"
        # actual_data=all_stop1.text
        # assert desired_expected_data in actual_data, f"Expected: {desired_expected_data}, Actual: {actual_data}"'''
        #
        # #from youtube tutorial
        # all_stop1=lp.wait_for_presence_all_element(By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        time.sleep(5)
        all_stop1 = search_flight_result.get_search_flight_result()
        # all_stop1=lp.wait_for_presence_of_all_elements(By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        # all_stop1=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
        self.log.info(len(all_stop1))

        # ut = Utils()
        self.ut.assertlist_itemtext(all_stop1,stop)

        # for stop in all_stop1:
        #
        #     print("The text is: "+stop.text)
        #
        #     assert stop.text=="1 Stop"
        #     print("assert pass")

        time.sleep(10)

        time.sleep(10)
