from selenium import webdriver
from steps.actionwords import Actionwords
import os
import django
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
os.environ['DJANGO_SETTINGS_MODULE'] = "superlists.settings"


def before_all(context):
    django.setup()
    context.runner = DiscoverRunner()


def after_all(context):
    # context.runner.teardown_databases(context.old_db_config)
    # context.runner.teardown_test_environment()
    pass


def before_feature(context, feature):

    # context.browser = webdriver.Firefox()
    # desired_cap = cap()
    if ('platform' in context.config.userdata) and \
            ('browserName' in context.config.userdata) and ('version' in context.config.userdata):
        desired_cap = {
            'platform': context.config.userdata['platform'],
            'browserName': context.config.userdata['browserName'],
            'version': context.config.userdata['version'],
        }
        context.driver = webdriver.Remote(
            command_executor="http://luo1211happy:fa8fc713-7613-4751-aeef-b4485cf938ad@ondemand.saucelabs.com:80/wd/hub"
            ,
            desired_capabilities=desired_cap)
        if 'type-tests' in feature.tags:
            feature.skip(reason='Skip root test')


def before_scenario(context, scenario):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()
    context.actionwords = Actionwords(context)


def after_scenario(context, scenario):
    context.test_case.tearDownClass()
    del context.test_case


def after_feature(context, feature):
    if hasattr(context, 'driver'):
        context.driver.quit()
