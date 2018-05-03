from selenium import webdriver

import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://toolsqa.com/iframe-practice-page/")
time.sleep(9)
frame1 = driver.find_element_by_xpath("//iframe[@name='iframe2']")
driver.execute_script("arguments[0].scrollIntoView();",frame1)
driver.switch_to.frame(frame1)
first_name = driver.find_element_by_xpath("//*[@class='col-md-4']//h5[text()='Very Flexible']")
driver.execute_script("arguments[0].scrollIntoView();",first_name)
print first_name.text
driver.switch_to.default_content()