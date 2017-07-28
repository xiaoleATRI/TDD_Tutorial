from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+2, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        # response = home_page(request)
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        '''expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)'''
        self.assertTemplateUsed(response, 'home.html')
