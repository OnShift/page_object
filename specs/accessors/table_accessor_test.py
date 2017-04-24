from hamcrest import assert_that, equal_to, instance_of
from page_object import on
from .. import BaseTestCase
from . import FakeTestPage
from mock import patch


class TestTable(BaseTestCase):

    def test_element_method(self):
        table = on(FakeTestPage).test_table_element()
        self.fake_browser.find_element.assert_called_once_with('css selector', 'table')
