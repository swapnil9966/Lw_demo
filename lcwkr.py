from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

time1  = time.time()
driver=webdriver.Chrome()  # type: WebDriver
driver.maximize_window()
driver.get("")

time2 = time.time()

print "Total TIme Taken ", time2-time1

#GOOGLE = driver.find_element_by_xpath("//*[@class='undefined icon-google']")