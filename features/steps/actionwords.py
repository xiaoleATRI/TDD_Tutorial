# encoding: UTF-8
from behave import *
from django.conf import settings
from selenium.webdriver.common.keys import Keys

from functional_tests.base import wait
from functional_tests.management.commands.create_session import \
    create_pre_authenticated_session


class Actionwords:
    def __init__(self, context):
        self.context = context

    @wait
    def wait_for_list_item(self, context, item_text):
        context.test.assertIn(
            item_text,
            context.browser.find_element_by_css_selector('#id_list_table').text
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
        ## to set a cookie we need to first visit the domain.
        ## 404 pages load the quickest!
        self.context.browser.get(self.context.get_url("/404_no_such_url/"))
        self.context.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))

    def i_add_an_item_p1(self, p1="Immanentize Eschaton"):
        self.context.browser.find_element_by_id('id_text').send_keys(p1)
        self.context.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
        self.wait_for_list_item(self.context, p1)

    def i_create_a_list_with_first_item_p1(self, p1="Reticulate Splines"):
        self.context.browser.get(self.context.get_url('/'))
        self.context.browser.find_element_by_id('id_text').send_keys(p1)
        self.context.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
        self.wait_for_list_item(self.context, p1)

    @wait
    def i_will_see_a_link_to_p1(self, p1 = ""):
        pass

    def i_click_the_link_to_p1(self, p1 = ""):
        pass

    @wait
    def i_will_be_on_the_p1_list_page(self, p1="Reticulate Splines"):
        first_row = self.context.browser.find_element_by_css_selector(
            '#id_list_table tr:first-child'
        )
        expected_row_text = '1: ' + p1
        self.context.test.assertEqual(first_row.text, expected_row_text)

    def this_user_can_not_create_list(self):
        pass
