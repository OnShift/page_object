from .element import Element


class Table(Element):
    """
    Element class to represent HTML Table
    """

    def __iter__(self):
        return iter(self.row_elements({'css': 'tbody tr'}))

    def find_row(self, predicate=None):
        if predicate is None:
            raise Exception
        return next(row for row in self if predicate(row) is True)
