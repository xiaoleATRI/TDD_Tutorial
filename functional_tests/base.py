from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

MAX_WAIT = 10

desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
    'build': "build-1234",
}


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        # test on saurce lab
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Remote(
            command_executor="http://xiaoleATRI:48d14f57-6c67-45cb-8775-f28c7fe7e56f@ondemand.saucelabs.com:80/wd/hub",
            desired_capabilities=desired_cap)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                WebDriverWait(self.browser, 0.5)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                WebDriverWait(self.browser, 0.5)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
