from page_object import Browser


def after_all(context):
    Browser.selenium_browser().close()
