from selenium import webdriver
import requests
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://istqbexamcertification.com/software-testing-interview-questions-and-answers/")
link = driver.find_element_by_xpath("//*[@title='Verification in software testing']/parent::td//a")
driver.execute_script("arguments[0].scrollIntoView();",link)
link = driver.find_element_by_xpath("//*[@title='Verification in software testing']/parent::td//a").get_attribute("href")
print link
status_code = requests.get(link).status_code
if status_code == 200 :
    print "pass"
else:
    print "fail"
print status_code
