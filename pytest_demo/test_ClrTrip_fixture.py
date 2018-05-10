import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


@pytest.fixture(scope="session")
def launch_browser(request):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://www.cleartrip.com/")
    print "Browser Launched Successfully"
    request.addfinalizer(close_browser)

def close_browser():
    print "Browser Closed!!!"
    #driver.close()

@pytest.mark.usefixtures("launch_browser")
class Test(object):
    def test_search(self):
        origin = driver.find_element_by_xpath("//input[@name='origin']").send_keys("BOM")
        destination = driver.find_element_by_xpath("//input[@name='destination']").send_keys("DEL")
        origin_date = driver.find_element_by_xpath("//input[@title='Depart date']")
        origin_date.clear()
        origin_date.send_keys("Thu, 28 Jun, 2018")
        origin_date.send_keys(Keys.ENTER)
        """child = driver.find_element_by_xpath("//*[@id='Childrens']")
        select = Select(child)
        select.select_by_value('3')"""
        driver.find_element_by_xpath("//*[@value='Search flights']").click()
        time.sleep(15)
        #validations need to be added here for seleccted date , pax counts

    def test_book_flight(self):
        time.sleep(10)
        buttons = driver.find_elements_by_xpath("//*[@class='resultUnit flightDetailsLink ']//*[@class='booking']")
        book_button = random.sample(buttons, 1)[0]
        driver.execute_script("arguments[0].scrollIntoView(true);", book_button)
        time.sleep(4)
        driver.execute_script("arguments[0].click();", book_button)


    def test_itinarary(self):
        driver.find_element_by_xpath("//*[@for='insurance_confirm']").click()
        coupon = driver.find_element_by_xpath("//input[@name='coupon']")
        coupon.clear()
        coupon.send_keys("test")
        driver.find_element_by_xpath("//input[@id='itineraryBtn']").click()


    def test_travelerdetail(self):
        email = driver.find_element_by_xpath("//input[@type='email']")
        email.send_keys("abc@gmail.com")
        driver.find_element_by_xpath("//input[@id='LoginContinueBtn_1']").click()
        time.sleep(20)
        title = driver.find_element_by_xpath("//select[@name='AdultTitle1']")
        select = Select(title)
        #select.select_by_value()
        select.select_by_visible_text('Mr')
        fname = driver.find_element_by_xpath("//input[@name='AdultFname1']")
        fname.send_keys("swap")
        lname = driver.find_element_by_xpath("//input[@name='AdultLname1']")
        lname.send_keys("neova")
        mb = driver.find_element_by_xpath("//input[@name='contact1']")
        mb.send_keys("1219944322")
        driver.find_element_by_xpath("//label[@for='use_gst']").click()



