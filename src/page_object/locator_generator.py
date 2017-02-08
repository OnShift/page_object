class LocatorGenerator:
    """
    Class to generate all locator functions
    """

    ELEMENTS = ['select_list',
                'option',
                'image',
                'table',
                'row',
                'cell',
                'div',
                'span',
                'paragraph',
                'label',
                'text_area',
                'text_field',
                'link',
                'heading',
                'button',
                'radio_button',
                'checkbox']

    def generate_locators(self):
        for tag in self.ELEMENTS:
            setattr(self, "{}_element".format(tag), getattr(self.locator, "{0}_for".format(tag)))
            setattr(self, "{}_elements".format(tag), getattr(self.locator, "{0}s_for".format(tag)))
