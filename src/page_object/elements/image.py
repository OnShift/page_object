from .element import Element


class Image(Element):
    """
    Element class to represent HTML Image
    """

    @property
    def width(self):
        return self.attribute('width')

    @property
    def height(self):
        return self.attribute('height')
