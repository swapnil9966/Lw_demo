import time

from selenium import webdriver
from selenium.webdriver import ActionChains


def launch_browser(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(url)
    return driver

def test_menu():
    try:
        browser = launch_browser(url="https://www.ebay.in/")
        Home_Living = browser.find_element_by_xpath("//*[text()='Home & Living']/parent::td")
        ActionChains(browser).move_to_element(Home_Living).perform()
        time.sleep(3)
        expected_val = "Furniture"
        home_decor = browser.find_element_by_xpath("//a[@title='Home & Living - Furniture']").text
        print home_decor
        if expected_val == home_decor:
            print "Pass"
        else:
            print "Fail"
    except Exception,ex:
        print ex.message

test_menu()
