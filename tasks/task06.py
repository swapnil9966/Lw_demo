from selenium import webdriver
import requests
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://istqbexamcertification.com/contact-us/")
time.sleep(3)
links = driver.find_elements_by_xpath("//a[contains(@href,'http')]")
for link in links:

    if requests.get(link.get_attribute("href")).status_code == 200:
        print "pass"
    else:
        print "fail"



