import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from page.search_result_page import SearchFlightResult
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log=Utils.sample_logger()

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    #Locators
    DEPART_FROM_FIELD="//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD="//input[@id='BE_flight_arrival_city']"
    DEPART_CAL_FIELD="//input[@id='BE_flight_origin_date']"
    ALL_DATES="//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']"
    SEARCH_BUTTON="BE_flight_flsearch_btn"
    def getdepartfromfield(self):
        return self.driver.find_element(By.XPATH, self.DEPART_FROM_FIELD)
    def enterdepartfromlocation(self,departloc):
        self.getdepartfromfield().click()
        self.getdepartfromfield().send_keys(departloc)
        time.sleep(3)
        self.getdepartfromfield().send_keys(Keys.ENTER)
        time.sleep(3)
    # def departfrom(self,departloc):
    #     depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #
    #     time.sleep(3)
    #
    #     depart_from.click()
    #
    #     time.sleep(3)
    #
    #     depart_from.send_keys(departloc)
    #
    #     time.sleep(3)
    #
    #     depart_from.send_keys(Keys.ENTER)
    #
    #     time.sleep(3)
    def getgoingtofield(self):
        return self.driver.find_element(By.XPATH, self.GOING_TO_FIELD)
    def entergoingtolocation(self,goingloc):
        self.getgoingtofield().click()
        self.getgoingtofield().send_keys(goingloc)
        time.sleep(3)
        self.getgoingtofield().send_keys(Keys.ENTER)
        time.sleep(3)
    # def goingto(self,goingloc):
    #     going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #
    #     going_to.click()
    #
    #     going_to.send_keys(goingloc)
    #
    #     time.sleep(3)
    #
    #     going_to.send_keys(Keys.ENTER)
    def departdatefield(self):
        time.sleep(10)
        return self.driver.find_element(By.XPATH, self.DEPART_CAL_FIELD)
    def alldate(self):
        time.sleep(3)
        return self.driver.find_elements(By.XPATH,self.ALL_DATES)
    def enterdeparturedate(self,departuredate):
        self.departdatefield().click()
        all_dates=self.alldate()
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                time.sleep(4)
                break
        time.sleep(3)
    def getsearchbutton(self):
        time.sleep(3)
        return self.driver.find_element(By.ID, self.SEARCH_BUTTON)
    def clicksearchbutton(self):
        self.getsearchbutton().click()
        time.sleep(3)
    def searchflights(self,departloc,goingloc,departuredate):
        self.enterdepartfromlocation(departloc)
        self.entergoingtolocation(goingloc)
        self.enterdeparturedate(departuredate)
        self.clicksearchbutton()
        search_flights_result = SearchFlightResult(self.driver)
        return search_flights_result
    # def departtime(self,dtime):
    #     time.sleep(10)
    #     depart_cal = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
    #
    #     depart_cal.click()
    #
    #     time.sleep(3)
    #
    #     all_dates = self.driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == dtime:
    #             date.click()
    #             time.sleep(4)
    #             break
    #     time.sleep(3)
    #
    #     time.sleep(3)
    # def click_search_bttn(self):
    #     search_flight = self.driver.find_element(By.ID, "BE_flight_flsearch_btn")
    #
    #     search_flight.click()


