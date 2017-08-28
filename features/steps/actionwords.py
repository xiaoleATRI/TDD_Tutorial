# encoding: UTF-8
from django.conf import settings
from selenium.webdriver.common.keys import Keys

from functional_tests.base import wait
from functional_tests.management.commands.create_session import \
    create_pre_authenticated_session
import subprocess


class Actionwords:
    def __init__(self, context):
        self.context = context

    @wait
    def wait_for_list_item(self, context, item_text):
        context.test.assertIn(
            item_text,
            context.driver.find_element_by_css_selector('#id_list_table').text
        )

    def i_logged_in_as_administrator(self):
        pass

    def i_choose_one_user(self):
        pass

    def i_update_its_permission_that_this_user_can_only_read_list(self):
        pass

    def i_logged_out(self):
        pass

    def logged_in_with_updated_user_account(self):
        pass

    def this_user_can_only_view_list(self):
        pass

    def this_user_can_not_create_item(self):
        pass

    def this_user_can_not_update_item(self):
        pass

    def this_user_can_not_delete_item(self):
        pass

    def this_user_can_not_update_list(self):
        pass

    def this_user_can_not_delete_list(self):
        pass
# Create list part

    def i_am_a_loggedin_user(self):
        session_key = create_pre_authenticated_session(email='edith@example.com')
        self.context.driver.get(self.context.get_url("/404_no_such_url/"))
        self.context.driver.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))

    def i_add_an_item_p1(self, p1="Immanentize Eschaton"):
        self.context.driver.find_element_by_id('id_text').send_keys(p1)
        self.context.driver.find_element_by_id('id_text').send_keys(Keys.ENTER)
        self.wait_for_list_item(self.context, p1)

    def i_create_a_list_with_first_item_p1(self, p1="Reticulate Splines"):
        self.context.driver.get(self.context.get_url('/'))
        self.context.driver.find_element_by_id('id_text').send_keys(p1)
        self.context.driver.find_element_by_id('id_text').send_keys(Keys.ENTER)
        self.wait_for_list_item(self.context, p1)

    @wait
    def i_will_see_a_link_to_p1(self, p1 = ""):
        pass

    def i_click_the_link_to_p1(self, p1 = ""):
        pass

    @wait
    def i_will_be_on_the_p1_list_page(self, p1="Reticulate Splines"):
        # first_row = self.context.driver.find_element_by_css_selector(
        #     '#id_list_table tr:first-child'
        # )
        # expected_row_text = '1: ' + p1
        # self.context.test.assertEqual(first_row.text, expected_row_text)
        pass

    def this_user_can_not_create_list(self):
        pass

    def i_use_the_current_directory_as_working_directory(self):
        self.context.path = settings.BASE_DIR

    def i_run_p1(self, p1 = "", datatable = "||"):
        for row in datatable:
            platform = row["platform"]
            browserName = row["browserName"]
            version = row["version"]
            res = subprocess.check_call(
                ["python", "manage.py", "behave", "-D", "platform="+platform, "-D", "browserName="+browserName, "-D",
                 "version="+version, "features/"])
            print(res)

    def it_should_pass(self):
        pass
