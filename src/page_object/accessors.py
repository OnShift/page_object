from __future__ import absolute_import
from page_object.locator_generator import LocatorGenerator

class Accessors(object):
    """
    Contains the methods that are inserted into your page objects when you inherit from the PageObject class.
    These methods will generate accessor methods for specfic elements, to interact with elements.

    Args:
        name      (string): The name you want to refer to the element as.
        identifier  (dict): Method to identify the element.

    Example:
        self.table(name = "example", { 'css' : "[data-test-*='example']" })

        Will generate:
            - self.example_element()
    """

    def __init__(self):
        for tag in LocatorGenerator.ELEMENTS:
            setattr(self, "{0}s".format(tag), self._define_plural_accessor(tag))

    def page_url(self, url):
        def navigate_to(url_params):
            complete_url = url.format(base_url=self.base_url, **url_params)
            self.browser.get(complete_url)

        setattr(self, "goto", navigate_to)

    def table(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
        """

        self._standard_methods(name, identifier, 'table_for')

    def image(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
        """
        self._standard_methods(name, identifier, 'image_for')

    def button(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}"        : clicks the element
        """
        def click():
            return getattr(self, "{0}_element".format(name))().click()

        setattr(self, "{0}".format(name), click)

        self._standard_methods(name, identifier, 'button_for')

    def link(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}         : clicks the element
        """

        def click_method():
            return getattr(self, "{0}_element".format(name))().click()

        setattr(self, name, click_method)

        self._standard_methods(name, identifier, 'link_for')

    def text_area(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "set_{name}     : sets text of element
        """
        def set_method(value):
            return getattr(self, "{0}_element".format(name))().set_value(value)

        setattr(self, "set_{0}".format(name), set_method)

        self._standard_methods(name, identifier, 'text_area_for')

    def text_field(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "set_{name}     : sets text of element
        """
        def set_method(value):
            return getattr(self, "{0}_element".format(name))().set_value(value)

        def get_method():
            return getattr(self, "{0}_element".format(name))().get_value()

        setattr(self, "set_{0}".format(name), set_method)
        setattr(self, "{0}".format(name), get_method)

        self._standard_methods(name, identifier, 'text_field_for')

    def div(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'div_for')

    def span(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """
        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'span_for')

    def paragraph(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """
        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'paragraph_for')

    def label(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """
        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'label_for')

    def h1(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'heading_for')

    def h2(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'heading_for')

    def h3(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'heading_for')

    def h4(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'heading_for')

    def h5(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'heading_for')

    def h6(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "{name}:        : returns text of element
        """

        def text():
            return getattr(self, "{0}_element".format(name))().text()

        setattr(self, "{0}".format(name), text)

        self._standard_methods(name, identifier, 'heading_for')

    def select_list(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "set_{name}"    : sets the option by option text
            "{name}_options": returns options text as list of strings
        """

        def set_method(text):
            return getattr(self, "{0}_element".format(name))().select(text)

        def get_method():
            return getattr(self, "{0}_element".format(name))().text()

        def options():
            return getattr(self, "{0}_element".format(name))().options_text()

        setattr(self, "set_{0}".format(name), set_method)
        setattr(self, "get_{0}".format(name), get_method)
        setattr(self, "{0}_options".format(name), options)

        self._standard_methods(name, identifier, 'select_list_for')

    def checkbox(self, name, identifier):
        """
        Will generate:
            "{name}_element": returns an element
            "uncheck_{name}": to uncheck a checked checkbox
            "check_{name}"  : to check an unchecked checkbox
        """

        def check():
            return getattr(self, "{0}_element".format(name))().check()

        def uncheck():
            return getattr(self, "{0}_element".format(name))().uncheck()

        def is_checked():
            return getattr(self, "{0}_element".format(name))().is_checked()

        setattr(self, "check_{0}".format(name), check)
        setattr(self, "uncheck_{0}".format(name), uncheck)
        setattr(self, "is_{0}_checked".format(name), is_checked)

        self._standard_methods(name, identifier, 'checkbox_for')

    def _define_plural_accessor(self, tag):
        def plural_accessor(name, identifier):
            def elements():
                return getattr(self.locator, "{0}s_for".format(tag))(identifier)

            setattr(self, "{0}_elements".format(name), elements)

        return plural_accessor

    def _standard_methods(self, name, identifier, method):
        def element():
            return getattr(self.locator, method)(identifier)

        setattr(self, "{}_element".format(name), element)
