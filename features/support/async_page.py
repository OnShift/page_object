from page_object import PageObject


class AsyncPage(PageObject):

    def define_elements(self):
        self.button(name='target', identifier={'id': 'target'})
        self.button(name='enable', identifier={'id': 'enable'})
        self.button(name='disable', identifier={'id': 'disable'})
