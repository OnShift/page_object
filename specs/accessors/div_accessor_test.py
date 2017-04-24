from hamcrest import assert_that, equal_to, instance_of
from page_object import on
from .. import BaseTestCase
from . import FakeTestPage
from mock import patch


class TestDiv(BaseTestCase):

    @patch('page_object.locator.Locator.div_for')
    def test_element_method(self, mock):
        self.element = self.create_mock()
        self.configure_mock(mock, {'return_value': self.element})

        actual_element = on(FakeTestPage).test_div_element()
        assert_that(actual_element, equal_to(self.element))

    @patch('page_object.locator.Locator.div_for')
    def test_get_text_method(self, mock):
        self.element = self.create_mock()
        self.configure_mock(mock, {'return_value': self.element})

        expected_text = 'I am in a div!'
        self.configure_mock(self.element.text, {'return_value': expected_text})

        actual_text = on(FakeTestPage).test_div()
        assert_that(actual_text, equal_to(expected_text))
