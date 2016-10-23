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
