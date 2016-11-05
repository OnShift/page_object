class element_predicate():

    def __init__(self, element, predicate):
        self.element = element
        self.predicate = predicate

    def __call__(self, drivers=None):
        return getattr(self.element, self.predicate)()
