from hamcrest import assert_that, equal_to
from page_object import on, PageObject
from .. import BaseTestCase
from . import MagicPage, FakeTestPage


class TestOn(BaseTestCase):

    def setup_method(self, method):
        super().setup_method()

    def test_creates_instance(self):
        page = on(FakeTestPage)
        assert_that(isinstance(page, FakeTestPage), equal_to(True))
        assert_that(isinstance(page, PageObject), equal_to(True))

    def test_calls_define_elements(self):
        page = on(MagicPage)
        page.define_elements.assert_called_with()

    def test_calls_goto(self):
        expect_url_params = {}
        page = on(MagicPage, visit_page=True, url_params=expect_url_params)
        page.goto.assert_called_with(expect_url_params)

    def test_calls_initalize_page(self):
        page = on(MagicPage)
        page.initialize_page.assert_called_with()
