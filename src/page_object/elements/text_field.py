from .element import Element


class TextField(Element):
    """
    Element class to represent HTML TextField
    """

    def set_value(self, text):
        """
        Set value of text field element

        Args:
            text: text to set the value of the text field.
        """
        self.clear()
        self.send_keys(text)

    def get_value(self):
        """
        Return:
            Current value of text field element
        """
        return self.attribute('value')
