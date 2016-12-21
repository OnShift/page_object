from hamcrest import assert_that, equal_to
from page_object import visit, PageObject
from .. import BaseTestCase
from . import MagicPage, FakeTestPage


class CompleteUrlTestPage(PageObject):

    def define_elements(self):
        self.page_url('{base_url}/test_route/{id}?{filter}')


class TestVisit(BaseTestCase):

    def set_base_url(self):
        import os
        os.environ['PAGE_OBJECT_BASE_URL'] = 'www.pageobject.com'

    def test_creates_instance(self):
        page = visit(FakeTestPage)
        assert_that(isinstance(page, FakeTestPage), equal_to(True))
        assert_that(isinstance(page, PageObject), equal_to(True))

    def test_should_navigate_to_hardcoded_url(self):
        visit(FakeTestPage)
        self.fake_browser.get.assert_called_with('www.noop.com')

    def test_builds_url_from_base_url(self):
        self.set_base_url()
        url_params = {'filter': 'start_date:today', 'id': 18}
        visit(CompleteUrlTestPage, url_params=url_params)

        expected_url = 'www.pageobject.com/test_route/18?start_date:today'
        self.fake_browser.get.assert_called_with(expected_url)

    def test_calls_define_elements(self):
        page = visit(MagicPage)
        page.define_elements.assert_called_with()

    def test_calls_goto(self):
        expect_url_params = {}
        page = visit(MagicPage, url_params=expect_url_params)
        page.goto.assert_called_with(expect_url_params)

    def test_calls_initalize_page(self):
        page = visit(MagicPage)
        page.initialize_page.assert_called_with()
