from .element import Element


class TextArea(Element):
    """
    Element class to represent HTML TextArea
    """

    def set_value(self, text):
        """
        Set value of text area element

        Args:
            text: text to set the value of the text area to.
        """
        self.clear()
        self.send_keys(text)

    def get_value(self):
        """
        Return:
            Current value of text field element
        """
        return self.attribute('value')
