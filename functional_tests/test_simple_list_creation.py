from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import wd.parallel
MAX_WAIT = 10


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.driver.get(self.live_server_url)
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.driver.title)
#       self.fail('Finish the test!')
        header_text = self.driver.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        # since the page will be redirected after posting, there is no item_text associate with the form
        # time.sleep(1)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        '''self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows), f"New to-do item did not appear in table."
                                                                        f" Contents were:\n{table.text}"
        )'''
        '''self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])'''
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        # self.wait_for_row_in_list_table('foo')
        # self.fail('Finish the test!')
        # She visits that URL - her to-do list is still there.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.driver.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # She noticed that her list has a unique URL
        edith_list_url = self.driver.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        # Satisfied, she goes back to sleep

        # Now a new user, Francis, comes along to the site

        # We use a new browser session to make sure that no information
        # of Edith's is coming through from cookies et
        self.driver.quit()
        self.driver = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's
        # list
        self.driver.get(self.live_server_url)
        page_text = self.driver.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item.
        # is less interesting than Edith...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        # self.assertEqual(self.browser.find_element_by_tag_name('h1').text, 'Your To-do list')
        # self.assertEqual(self.browser.current_url, '')
        # time.sleep(10)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.driver.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.driver.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


