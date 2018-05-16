import time
import pytest
from cleartrip.common_fixtures import fixtures
from cleartrip.locators import home
from cleartrip.test_data import home_data
from cleartrip.utility import utils


@pytest.fixture(scope="session")
def launch_browser(request):
    global driver
    browser_url = fixtures.load_config_file()['URL']
    driver = utils.launch_browser(browser_url)
    request.addfinalizer(close_browser)

def close_browser():
    #driver.close()
    pass


@pytest.mark.usefixtures("launch_browser")
class Test(object):

    def test_home_page_title(self):
        " Verifying common features of cleartrip home page e.g title, "
        assert utils.validate_page_text(driver,home.SEARCH_FLIGHT,home_data.search_flight_text)

    def test_cleartrip_left_menu_items(self):
        "Verifying the left menu items"
        assert utils.validate_menu_options(driver,home.BOOKING_OPTIONS,home_data.BOOKING_OPTIONS_LIST)

    def test_cleartrip_currency(self):
        "Verifying the currency "
        utils.click(driver, home.CURRENCY_TEXT)
        assert utils.validate_menu_options(driver, home.CURRENCY,home_data.CURRENCY_LIST)





    def test_cleartrip_county(self):
        ""
        pass

    def test_cleartrip_yourtrip_options(self):
        ""
        pass

    def test_cleartrip_footer_links(self):
        ""
        pass


