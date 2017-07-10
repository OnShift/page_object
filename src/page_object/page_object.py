from __future__ import absolute_import
import time
import os
from .accessors import Accessors
from .locator_generator import LocatorGenerator


class PageObject(LocatorGenerator, Accessors, object):
    """
    Class that when included adds functionality to a page object.
    This class will add numerous class and instance methods that you use to define and
    interact with web pages.
    """

    def __init__(self, browser):
        """
        Args:
            browser (selenium.webdriver.browser) : selenium browser instance to use
            visit_page                    (bool) : force browser to navigate to page, defaults to false.
        """
        super(PageObject, self).__init__()
        self._load_locator(browser)
        self.generate_locators()
        self.browser = browser

    @property
    def base_url(self):
        return os.environ.get('PAGE_OBJECT_BASE_URL', None)

    @property
    def current_url(self):
        """
        Return:
            Returns the URL of the current page.
        """
        return self.browser.current_url

    @property
    def html(self):
        """
        Return:
            Returns the HTML of the current page.
        """
        return self.browser.page_source

    @property
    def title(self):
        """
        Return:
            Returns the title of the current page.
        """
        return self.browser.title

    def navigate_to(self, url):
        """
        Navigate to url.

        Args:
            url (string): Url to navigate to.
        """
        self.browser.get(url)

    def wait(self, seconds=5):
        """
        Method to wait a given amount of seconds.
        Args:
            seconds (int): Defaults to 5.
        """
        time.sleep(seconds)

    def _load_locator(self, browser):
        from page_object.locator import Locator
        self.locator = Locator(browser)
