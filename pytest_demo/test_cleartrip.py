from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.cleartrip.com/")
time.sleep(9)
#cleartri
#test
#oneway = driver.find_element_by_xpath("//input[@value='OneWay']").click()
origin = driver.find_element_by_xpath("//input[@name='origin']").send_keys("BOM")
destination = driver.find_element_by_xpath("//input[@name='destination']").send_keys("DEL")
origin_date = driver.find_element_by_xpath("//input[@title='Depart date']")
origin_date.clear()
origin_date.send_keys("Thu, 28 Jun, 2018")
origin_date.send_keys(Keys.ENTER)
child = driver.find_element_by_xpath("//*[@id='Childrens']")
select = Select(child)
select.select_by_value('3')
driver.find_element_by_xpath("//*[@value='Search flights']").click()
time.sleep(15)
"""
driver.find_element_by_xpath("//label[@for='1_1_0']").click()
driver.find_element_by_xpath("//*[@for='1_1_1']").click()
driver.find_element_by_xpath("//*[@for='1_1_0_8_departureTime']").click()
driver.find_element_by_xpath("//*[@original-title='Air India']").click()
time.sleep(15)
"""
buttons = driver.find_elements_by_xpath("//*[@class='resultUnit flightDetailsLink ']//*[@class='booking']")
print "Length is "
print len(buttons)
try:
    book_button = random.sample(buttons, 1)

    book_button[0].click()
except:
    buttons[0].click()

#driver.find_element_by_xpath("(//*[@class='resultUnit flightDetailsLink ']//*[@class='booking'])[1]").click()
driver.find_element_by_xpath("//*[@for='insurance_confirm']").click()
coupon = driver.find_element_by_xpath("//input[@name='coupon']")
coupon.clear()
coupon.send_keys("test")

