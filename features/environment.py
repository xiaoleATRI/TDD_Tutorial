from selenium import webdriver


def before_all(context):
    desired_cap = {
        'platform': "Mac OS X 10.9",
        'browserName': "chrome",
        'version': "31",
        'build': "build-1234",
    }
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Remote(
    #     command_executor="http://xiaoleATRI:48d14f57-6c67-45cb-8775-f28c7fe7e56f@ondemand.saucelabs.com:80/wd/hub",
    #     desired_capabilities=desired_cap)


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
