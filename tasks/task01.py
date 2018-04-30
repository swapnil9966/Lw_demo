from selenium import webdriver


def launch_browser(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(url)
    return driver

def test_menu():
    try:
        browser = launch_browser(url="http://istqbexamcertification.com/software-testing-interview-questions-and-answers/")
        expected_val = "Home"
        home = browser.find_element_by_xpath("//*[@id='menu-item-1910']/a/span").text
        if expected_val == home:
            print "Pass"
        else:
            print "Fail"
    except Exception,ex:
        print ex.message

test_menu()