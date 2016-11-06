from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from .element import Element
from .option import Option


class SelectList(Select, Element):
    """
    Element class to represent HTML Select List
    """

    def __init__(self, element):
        Select.__init__(self, element)
        Element.__init__(self, element)

    def selected(self):
        return Option(self.first_selected_option)

    def text(self):
        return self.selected().text()

    def value(self):
        return self.selected().attribute('value')

    def select(self, text):
        return self.select_by_visible_text(text)

    def options_text(self):
        return [option.text for option in self.options]
