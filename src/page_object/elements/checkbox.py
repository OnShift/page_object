from .element import Element


class CheckBox(Element):
    """
    Element class to represent an HTML Checkbox

    Should maybe have a method to set the value to 'checked' or 'unchecked'
    """

    def check(self):
        if(not self.element.is_selected()):
            self.element.click()

    def uncheck(self):
        if(self.element.is_selected()):
            self.element.click()

    def is_checked(self):
        return self.element.is_selected()
