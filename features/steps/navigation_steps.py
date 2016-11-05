from support.page import Page
from support.async_page import AsyncPage
from page_object import Browser
import os


@given(u'I am on the static elements page')
def step_impl(context):
    path = os.path.abspath("support/html/static_elements.html")
    context.page = Page(Browser.selenium_browser())
    context.page.navigate_to('file://{0}'.format(path))
    context.page.define_elements()


@given(u'I am on the async elements page')
def step_impl(context):
    path = os.path.abspath("support/html/async_elements.html")
    context.page = AsyncPage(Browser.selenium_browser())
    context.page.navigate_to('file://{0}'.format(path))
    context.page.define_elements()
