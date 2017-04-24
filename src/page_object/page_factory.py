from __future__ import absolute_import
from page_object.browser import Browser


def on(page, visit_page=False, url_params={}):
    """
    Creates PageObject with current instance of the selenium_browser.

    Args:
        page     (PageObject): PageObject class name.
        visit_page  (boolean): Navigate to page.
        url_params   (dictionary): url parameter object.

    Returns:
            New instance of page argument.
    """
    page_instance = page(Browser.selenium_browser())

    if hasattr(page_instance, 'define_elements'):
        page_instance.define_elements()

    if visit_page:
        page_instance.goto(url_params)

    if hasattr(page_instance, 'initialize_page'):
        page_instance.initialize_page()

    return page_instance


def visit(page, url_params={}):
    """
    Navigate to page url.

    Creates PageObject with current instance of the selenium_browser.

    Args:
        page     (PageObject): PageObject class name.
        url_params   (dictionary): url parameter object.

    Returns:
            New instance of page argument.
    """
    return on(page, visit_page=True, url_params=url_params)
