from selenium import webdriver

import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://istqbexamcertification.com/software-testing-interview-questions-and-answers/")
time.sleep(3)
expected_val = "Home"
home = driver.find_element_by_xpath("//*[@id='menu-item-1910']/a/span").text
if expected_val == home:
       print "Pass"
       driver.get_screenshot_as_file(filename="pass.png")
else:
       print "Fail"
       driver.get_screenshot_as_file(filename="fail.png")