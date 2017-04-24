from __future__ import absolute_import
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from page_object.elements import *


class Locator(object):
    """
    Class to encapsulate all selenium selector behavior.
    """

    def __init__(self, target):
        self.target = target

    def select_list_for(self, identifier):
        return self.element_for(SelectList, identifier)

    def select_lists_for(self, identifier):
        return self.elements_for(SelectList, identifier)

    def option_for(self, identifier):
        return self.element_for(Option, identifier)

    def options_for(self, identifier):
        return self.elements_for(Option, identifier)

    def button_for(self, identifier):
        return self.element_for(Button, identifier)

    def buttons_for(self, identifier):
        return self.elements_for(Button, identifier)

    def image_for(self, identifier):
        return self.element_for(Image, identifier)

    def images_for(self, identifier):
        return self.elements_for(Image, identifier)

    def text_area_for(self, identifier):
        return self.element_for(TextArea, identifier)

    def text_areas_for(self, identifier):
        return self.elements_for(TextArea, identifier)

    def text_field_for(self, identifier):
        return self.element_for(TextField, identifier)

    def text_fields_for(self, identifier):
        return self.elements_for(TextField, identifier)

    def div_for(self, identifier):
        return self.element_for(Div, identifier)

    def divs_for(self, identifier):
        return self.elements_for(Div, identifier)

    def span_for(self, identifier):
        return self.element_for(Span, identifier)

    def spans_for(self, identifier):
        return self.elements_for(Span, identifier)

    def paragraph_for(self, identifier):
        return self.element_for(Paragraph, identifier)

    def paragraphs_for(self, identifier):
        return self.elements_for(Paragraph, identifier)

    def label_for(self, identifier):
        return self.element_for(Label, identifier)

    def labels_for(self, identifier):
        return self.elements_for(Label, identifier)

    def link_for(self, identifier):
        return self.element_for(Link, identifier)

    def links_for(self, identifier):
        return self.elements_for(Link, identifier)

    def heading_for(self, identifier):
        return self.element_for(Heading, identifier)

    def headings_for(self, identifier):
        return self.elements_for(Heading, identifier)

    def table_for(self, identifier):
        return self.element_for(Table, identifier)

    def tables_for(self, identifier):
        return self.elements_for(Table, identifier)

    def cells_for(self, identifier):
        return self.elements_for(TableCell, identifier)

    def cell_for(self, identifier):
        return self.element_for(TableCell, identifier)

    def rows_for(self, identifier):
        return self.elements_for(TableRow, identifier)

    def row_for(self, identifier):
        return self.element_for(TableRow, identifier)

    def radio_buttons_for(self, identifier):
        return self.elements_for(RadioButton, identifier)

    def radio_button_for(self, identifier):
        return self.element_for(RadioButton, identifier)

    def checkbox_for(self, identifier):
        return self.element_for(CheckBox, identifier)

    def checkboxs_for(self, identifier):
        return self.elements_for(CheckBox, identifier)

    def element_for(self, element_type, identifier):
        """
        Method to find a element through selenium
        Arg:
            element_type (page_object.Element): class to instantiate
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of element class for type
        """
        how, what = self._parse_identifier(identifier)
        try:
            element = self.target.find_element(how, what)
        except NoSuchElementException:
            return Element(SubstituteWebElement(self, identifier, element_type))

        return element_type(element)

    def elements_for(self, element_type, identifier):
        """
        Method to find all elements matching the identifier through selenium

        Arg:
            element_type (page_object.Element): class to instantiate
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of element class for type
        """
        how, what = self._parse_identifier(identifier)
        elements = self.target.find_elements(how, what)
        return list(map(lambda element: element_type(element), elements))

    def _parse_identifier(self, identifier):
        mapping = {
            'css': By.CSS_SELECTOR,
            'class': By.CLASS_NAME,
            'tag': By.TAG_NAME,
            'id': By.ID
        }
        key, value = identifier.copy().popitem()
        return mapping[key], value
