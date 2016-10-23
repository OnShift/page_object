from page_object import PageObject


class Page(PageObject):

    def define_elements(self):
        self.text_field(name='text_field_id', identifier={'id': 'text_field_id'})
