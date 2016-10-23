from .element import Element


class TableRow(Element):
    """
    Element class to represent HTML tr
    """

    def __iter__(self):
        """
        Return all cells in row as an iterable
        """
        return iter(self.cell_elements({'css': 'th,td'}))

    def get_cells(self, identifier, operation=None):
        """
        Method to retrieve row cells

        Args:
            identifier: selector for table cells
            operation: lambda to perform on each cell element

        Return:
            Mapped cells filtered by identifier
        """
        if operation is None:
            def operation(obj): return obj

        return [operation(cell) for cell in self.cell_elements(identifier)]
