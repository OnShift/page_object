from hamcrest import assert_that, equal_to, instance_of
from page_object import on, PageObject
from page_object.locator_generator import LocatorGenerator
from page_object.elements.div import Div
from .. import BaseTestCase
from . import FakeTestPage
from unittest.mock import patch


class TestPluralAccessors(BaseTestCase):

    @patch('page_object.locator.Locator.divs_for')
    def test_define_plural_accessor_method(self, locator):
        elements = on(FakeTestPage).test_plural_elements()
        locator.assert_called_once_with({'css': 'test'})

    def test_plural_accessor_methods(self):
        page = on(FakeTestPage)
        for tag in LocatorGenerator.ELEMENTS:
            assert_that('{0}s'.format(tag) in dir(page))
