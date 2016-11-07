from page_object import PageObject


class AsyncPage(PageObject):

    def define_elements(self):
        self.button(name='target', identifier={'id': 'target'})
        self.button(name='enable', identifier={'id': 'enable'})
        self.button(name='disable', identifier={'id': 'disable'})
        self.button(name='create', identifier={'id': 'create'})
        self.button(name='hide', identifier={'id': 'hide'})
        self.button(name='unhide', identifier={'id': 'unhide'})
        self.button(name='new', identifier={'id': 'new'})
