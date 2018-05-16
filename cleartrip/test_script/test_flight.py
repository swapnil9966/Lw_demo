import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from cleartrip.common_fixtures import fixtures
from cleartrip.locators import home
from cleartrip.utility import utils


@pytest.fixture(scope="session")
def launch_browser(request):
    global driver
    browser_url = fixtures.load_config_file()['URL']
    driver = utils.launch_browser(browser_url)
    request.addfinalizer(close_browser)

def close_browser():
    driver.close()


@pytest.mark.usefixtures("launch_browser")
class Test(object):


    def test_search(self):
       utils.send_keys(driver,home.FROM,"BOM")
       utils.send_keys(driver, home.TO, "DEL")
       utils.send_keys(driver, home.DEPARTURE_DATE, "Thu, 28 Jun, 2018")
       utils.send_keys(driver, home.DEPARTURE_DATE, Keys.ENTER)
       utils.click(driver,home.SEARCH_BUTTON)

    def test_booking(self):
        pass

    def test_book_flight(self):
        time.sleep(10)
        buttons = driver.find_elements_by_xpath(home.BOOK_FLIGHT)
        button = random.sample(buttons, 1)[0]
        utils.js_click(driver,button)

    def test_itinarary(self):
        ins_checks = driver.find_element_by_xpath(home.CHK_BOX_INSURANCE)
        utils.js_click(driver, ins_checks)
        utils.send_keys(driver, home.COUPON, "test")
        continue_button = driver.find_element_by_xpath(home.CONT_BUTTON)
        utils.js_click(driver, continue_button)
        time.sleep(5)


    def test_travelerdetail(self):

        utils.send_keys(driver, home.EMAIL, "swap@gmail.com")
        cont_button = driver.find_element_by_xpath(home.CONT_BUTTON1)
        utils.js_click(driver, cont_button)
        time.sleep(20)
        title = driver.find_element_by_xpath(home.TITLE)
        select = Select(title)
        select.select_by_visible_text('Mr')
        utils.send_keys(driver, home.FNAME, "swap")
        utils.send_keys(driver, home.LNAME, "barde")
        utils.send_keys(driver, home.MB, "1234567890")


