from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import types
import os
import wd.parallel
from .desired_cap import cap
MAX_WAIT = 10

#desired_cap = cap()
desired_cap = {
            'platform': "Mac OS X 10.9",
            'browserName': "chrome",
            'version': "31",
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

# use decorator to run test on different system and browswers


# def on_platforms(platforms):
#     def decorator(base_class):
#         module = sys.modules[base_class.__module__].__dict__
#         for i, platform in enumerate(platforms):
#             d = dict(base_class.__dict__)
#             d['desired_capabilities'] = platform
#             name = "%s_%s" % (base_class.__name__, i + 1)
#             module[name] = types.new_class(name, (base_class,), d)
#     return decorator


# @on_platforms(desired_cap)
class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        # test on saurce lab
        # self.browser = webdriver.Firefox()
        # self.drivers = wd.parallel.Remote(
        #     desired_capabilities=desired_cap,
        #     command_executor="http://xiaoleATRI:48d14f57-6c67-45cb-8775-f28c7fe7e56f@ondemand.saucelabs.com:80/wd/hub"
        # )
        self.driver = webdriver.Remote(
            command_executor="http://luo1211happy:fa8fc713-7613-4751-aeef-b4485cf938ad@ondemand.saucelabs.com:80/wd/hub",
            desired_capabilities=desired_cap)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.driver.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                WebDriverWait(self.driver, 0.5)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                WebDriverWait(self.driver, 0.5)

    def get_item_input_box(self):
        return self.driver.find_element_by_id('id_text')
