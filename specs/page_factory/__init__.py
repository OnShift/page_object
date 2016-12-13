from unittest import TestCase
from unittest.mock import MagicMock
from page_object import PageObject, Browser

fake = MagicMock()


class FakeTestPage(PageObject):

    def define_elements(self):
        self.page_url('www.noop.com')


class MagicPage(PageObject):

    def __new__(self, cls):
        return fake
