from selenium import webdriver
import requests
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://istqbexamcertification.com/software-testing-interview-questions-and-answers/")
download_link=driver.find_element_by_xpath("//*[text()='200+ Software Testing Interview Questions and Answers']")
driver.execute_script("arguments[0].scrollIntoView();",download_link)
download_link=driver.find_element_by_xpath("//*[text()='200+ Software Testing Interview Questions and Answers']/parent::a").get_attribute("href")
print download_link
status_code = requests.get(download_link).status_code
if status_code == 200:
    print "pass"
else:
    print "fail"


print status_code
