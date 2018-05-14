import time

from selenium import webdriver


def launch_browser(url):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)
        return driver
    except:
        return None


def scroll_to_element(driver,element):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true)",element)
    except:
        pass


def js_click(driver, element):
    try:
        driver.execute_script("arguments[0].click()", element)
    except:
        pass

def click(driver, element):
    try:
        driver.find_element_by_xpath(element).click()
    except:
        pass


def scroll_and_click():
    try:
        pass
    except:
        pass


def send_keys(driver, element, text):
    try:
        we = driver.find_element_by_xpath(element)
        we.clear()
        time.sleep(2)
        we.send_keys(text)
    except:
        pass


def scroll_to_top(driver):
    try:
        driver.execute_script("window.scrollTo(0,0)")
    except:
        pass


def scroll_to_button():
    try:
        pass
    except:
        pass

def select_dropdown_by_index():
    try:
        pass
    except:
        pass


def select_dropdown_by_text():
    try:
        pass
    except:
        pass

def select_dropdown_by_value():
    try:
      pass
    except:
        pass

def check_element_exist():
    try:
        pass
    except:
        pass