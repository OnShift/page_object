class SubstituteWebElement():

    def __init__(self, locator, identifier, element_type):
        self.locator = locator
        self.identifier = identifier
        self.element_type = element_type

    def exists(self):
        element = self._attempt_to_locate()
        return not isinstance(element.element, SubstituteWebElement)

    def _attempt_to_locate(self):
        return self.locator.element_for(self.element_type, self.identifier)
