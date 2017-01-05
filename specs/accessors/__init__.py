from page_object import PageObject


class FakeTestPage(PageObject):

    def define_elements(self):
        self.divs(name='test_plural', identifier={'css': 'test'})
        self.div(name='test_div', identifier={'css': 'div'})
        self.table(name='test_table', identifier={'css': 'table'})
