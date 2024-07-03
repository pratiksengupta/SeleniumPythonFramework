import os

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By #this is for fetching the by class
from selenium.webdriver.support.select import Select #helps to select element from dropdown

@pytest.fixture(scope="class")
def setup(request):

    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extra.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory=os.path.dirname(item.config.option.htmlpath)
            # file_name=str(int(round(time.time()*1000)))+".png"
            file_name=report.nodied.replace("::","_")+".png"
            destinationFile=os.path.join(report_directory,file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
               html='<div><img src="%s" alt="screenshot" style="width:300px;height=200px"'\
                  'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra
def pytest_html_report_title(report):
    report.title="learning automation report"