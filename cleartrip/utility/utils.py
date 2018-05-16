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

def validate_page_text(driver , locators, expected_text):
    try:
        actutal_text = driver.find_element_by_xpath(locators).text
        return str(actutal_text).__eq__(expected_text)
    except:
        return False


def validate_menu_options(driver , locators, menu_list):
    try:
        menu_items = []
        options = driver.find_elements_by_xpath(locators)
        print len(options)
        print "Real Menu Items ",len(menu_list)
        for i in options:
            menu_items.append(str(i.text))
        print menu_list
        print menu_items
        return all(x in menu_items for x in menu_list)
    except Exception,ex:
        print ex
        return False