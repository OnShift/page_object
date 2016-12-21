from hamcrest import assert_that, equal_to, instance_of
from page_object import on, PageObject
from page_object.locator_generator import LocatorGenerator
from page_object.elements.div import Div
from .. import BaseTestCase


class FakeTestPage(PageObject):

    def define_elements(self):
        self.divs(name='test_plural', identifier={'css': 'test'})


class TestPluralAccessors(BaseTestCase):

    def test_define_plural_accessor_method(self):
        self.configure_mock(self.fake_browser, {'find_elements.return_value': [object, object]})
        elements = on(FakeTestPage).test_plural_elements()
        self.fake_browser.find_elements.assert_called_once_with('css selector', 'test')
        for element in elements:
            assert_that(element, instance_of(Div))

    def test_plural_accessor_methods(self):
        page = on(FakeTestPage)
        for tag in LocatorGenerator.ELEMENTS:
            assert_that('{0}s'.format(tag) in dir(page))
