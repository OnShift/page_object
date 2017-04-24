from unittest import TestCase
from mock import MagicMock
from page_object import PageObject, Browser

fake = MagicMock()


class MagicPage(PageObject):

    def __new__(self, cls):
        return fake


class BaseTestCase(TestCase):
    fake_browser = None

    def setup_method(self, method):
        self.fake_browser = self.create_mock()
        Browser.set_browser(self.fake_browser)

    def create_mock(self, values=None):
        mock = MagicMock()
        if values is not None:
            self.configure_mock(mock, **values)
        return mock

    def configure_mock(self, mock, values):
        mock.configure_mock(**values)
