from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from page_object.elements.substitute_web_element import SubstituteWebElement
from page_object.elements.table import Table
from page_object.elements.table_row import TableRow
from page_object.elements.table_cell import TableCell
from page_object.elements.div import Div
from page_object.elements.span import Span
from page_object.elements.paragraph import Paragraph
from page_object.elements.label import Label
from page_object.elements.image import Image
from page_object.elements.select_list import SelectList
from page_object.elements.text_area import TextArea
from page_object.elements.text_field import TextField
from page_object.elements.link import Link
from page_object.elements.heading import Heading
from page_object.elements.button import Button
from page_object.elements.radio_button import RadioButton
from page_object.elements.checkbox import CheckBox
from page_object.elements.element import Element


class Locator(object):
    """
    Class to encapsulate all selenium selector behavior.
    """

    def __init__(self, target):
        self.target = target

    def select_list_for(self, identifier):
        """
        Method to find a single select_list element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of SelectList element
        """
        return self.element_for(SelectList, identifier)

    def select_lists_for(self, identifier):
        """
        Method to find all select_list elements by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of SelectList elements
        """
        return self.elements_for(SelectList, identifier)

    def button_for(self, identifier):
        """
        Method to find a single button element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Image element
        """
        return self.element_for(Button, identifier)

    def buttons_for(self, identifier):
        """
        Method to find all button elements by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of Button elements
        """
        return self.elements_for(Button, identifier)

    def image_for(self, identifier):
        """
        Method to find a single image element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Image element
        """
        return self.element_for(Image, identifier)

    def images_for(self, identifier):
        """
        Method to find all image elements by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of Image elements
        """
        return self.elements_for(Image, identifier)

    def text_area_for(self, identifier):
        """
        Method to find a single textarea element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Textarea element
        """
        return self.element_for(TextArea, identifier)

    def text_areas_for(self, identifier):
        """
        Method to find all textarea elements by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of Textarea elements
        """
        return self.elements_for(TextArea, identifier)

    def text_field_for(self, identifier):
        """
        Method to find a single text field element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of TextField element
        """
        return self.element_for(TextField, identifier)

    def text_fields_for(self, identifier):
        """
        Method to find all text field elements by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of TextField elements
        """
        return self.elements_for(TextField, identifier)

    def div_for(self, identifier):
        """
        Method to find a single div element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Div element
        """
        return self.element_for(Div, identifier)

    def divs_for(self, identifier):
        """
        Method to find div elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns array of Div elements
        """
        return self.elements_for(Div, identifier)

    def span_for(self, identifier):
        """
        Method to find a single span element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Span element
        """
        return self.element_for(Span, identifier)

    def spans_for(self, identifier):
        """
        Method to find span elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns array of Span elements
        """
        return self.elements_for(Span, identifier)

    def paragraph_for(self, identifier):
        """
        Method to find a single paragraph element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Paragraph element
        """
        return self.element_for(Paragraph, identifier)

    def paragraphs_for(self, identifier):
        """
        Method to find paragraph elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns array of Paragraph elements
        """
        return self.elements_for(Paragraph, identifier)

    def label_for(self, identifier):
        """
        Method to find a single label element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Label element
        """
        return self.element_for(Label, identifier)

    def labels_for(self, identifier):
        """
        Method to find label elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns array of Label elements
        """
        return self.elements_for(Label, identifier)

    def link_for(self, identifier):
        """
        Method to find Link element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Link
        """
        return self.element_for(Link, identifier)

    def links_for(self, identifier):
        """
        Method to find Link elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns array of a Links
        """
        return self.elements_for(Link, identifier)

    def heading_for(self, identifier):
        """
        Method to find heading element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Heading
        """
        return self.element_for(Heading, identifier)

    def headings_for(self, identifier):
        """
        Method to find heading elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns array of a Headings
        """
        return self.elements_for(Heading, identifier)

    def table_for(self, identifier):
        """
        Method to find a single table element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Table element
        """
        return self.element_for(Table, identifier)

    def tables_for(self, identifier):
        """
        Method to find a single table element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of Table element
        """
        return self.elements_for(Table, identifier)

    def cells_for(self, identifier):
        """
        Method to find table cell elements by an identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns list of TableCell elements
        """
        return self.elements_for(TableCell, identifier)

    def cell_for(self, identifier):
        """
        Method to find a single table cell element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of TableCell element
        """
        return self.element_for(TableCell, identifier)

    def rows_for(self, identifier):
        """
        Method to find table row elements by the identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns list of TableRow elements
        """
        return self.elements_for(TableRow, identifier)

    def row_for(self, identifier):
        """
        Method to find table row elements by the identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns instance of TableRow element
        """
        return self.element_for(TableRow, identifier)

    def radio_buttons_for(self, identifier):
        """
        Method to find radio button elements by the identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns list of RadioButton elements
        """
        return self.elements_for(RadioButton, identifier)

    def radio_button_for(self, identifier):
        """
        Method to find radio button elements by the identifier

        Arg:
            identifier (dict): how to identify elements and what the value is

        Return:
            Returns instance of RadioButton element
        """
        return self.element_for(RadioButton, identifier)

    def checkbox_for(self, identifier):
        """
        Method to find a single checkbox element by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns instance of CheckBox element
        """
        return self.element_for(CheckBox, identifier)

    def checkboxs_for(self, identifier):
        """
        Method to find all checkbox elements by the identifier

        Arg:
            identifier (dict): how to identify element and what the value is

        Return:
            Returns list of CheckBox elements
        """
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
        """
        Method to parse identifier and map it to the corresponding selenium key

        Arg:
            identifier (dict): mapping to selenium selector

        Return:
            Returns list of element class for type
        """
        mapping = {
            'css': By.CSS_SELECTOR,
            'class': By.CLASS_NAME,
            'tag': By.TAG_NAME,
            'id': By.ID
        }
        key, value = identifier.copy().popitem()
        return mapping[key], value
