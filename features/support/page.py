from page_object import PageObject


class Page(PageObject):

    def define_elements(self):
        self.text_field(name='text_field_id', identifier={'id': 'text_field_id'})
        self.text_field(name='text_field_class', identifier={'class': 'text_field_class'})
        self.text_field(name='text_field_css', identifier={'css': '[data-test-text-field="text_field_css"]'})

        self.text_area(name='text_area_id', identifier={'id': 'text_area_id'})
        self.text_area(name='text_area_class', identifier={'class': 'text_area_class'})
        self.text_area(name='text_area_css', identifier={'css': '[data-test-text-area="text_area_css"]'})

        self.select_list(name='sel_list_id', identifier={'id': 'sel_list_id'})
        self.select_list(name='sel_list_class', identifier={'class': 'sel_list_class'})
        self.select_list(name='sel_list_css', identifier={'css': '[data-test-select-list="select_list_css"]'})
        self.select_list(name='sel_list_tag', identifier={'tag': 'select'})

        self.checkbox(name='cb_id', identifier={'id': 'cb_id'})
        self.checkbox(name='cb_class', identifier={'class': 'cb_class'})
        self.checkbox(name='cb_css', identifier={'css': '[data-test-checkbox="checkbox_css"]'})

        self.button(name='button_id', identifier={'id': 'button_id'})
        self.button(name='button_class', identifier={'class': 'button_class'})
        self.button(name='button_css', identifier={'css': '[data-test-button="button_css"]'})
        self.button(name='disabled_button', identifier={'id': 'disabled_button'})

        self.link(name='google_search_id', identifier={'id': 'link_id'})
        self.link(name='google_search_class', identifier={'class': 'link_class'})
        self.link(name='google_search_css', identifier={'css': '[data-test-link="link_css"]'})
        self.link(name='google_search_tag', identifier={'tag': 'a'})

        self.div(name='div_id', identifier={'id': 'div_id'})
        self.div(name='div_class', identifier={'class': 'div_class'})
        self.div(name='div_css', identifier={'css': '[data-test-div="div_css"]'})
        self.div(name='div_tag', identifier={'tag': 'div'})

        self.span(name='span_id', identifier={'id': 'span_id'})
        self.span(name='span_class', identifier={'class': 'span_class'})
        self.span(name='span_css', identifier={'css': '[data-test-span="span_css"]'})
        self.span(name='span_tag', identifier={'tag': 'span'})

        self.paragraph(name='paragraph_id', identifier={'id': 'p_id'})
        self.paragraph(name='paragraph_class', identifier={'class': 'p_class'})
        self.paragraph(name='paragraph_css', identifier={'css': '[data-test-p="p_css"]'})
        self.paragraph(name='paragraph_tag', identifier={'tag': 'p'})

        self.label(name='label_id', identifier={'id': 'label_id'})
        self.label(name='label_class', identifier={'class': 'label_class'})
        self.label(name='label_css', identifier={'css': '[data-test-label="label_css"]'})

        self.image(name='image_id', identifier={'id': 'image_id'})
        self.image(name='image_class', identifier={'class': 'image_class'})
        self.image(name='image_css', identifier={'css': '[data-test-image="image_css"]'})
