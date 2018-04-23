from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.thinkbroadband.com/download")
download_link=driver.find_element_by_xpath("//*[@class='module']//*[text()='Large File (512MB)']/preceding-sibling::p//a")
link=download_link.get_attribute("href")
print link