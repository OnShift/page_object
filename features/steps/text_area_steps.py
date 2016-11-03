from hamcrest import assert_that, equal_to


@when(u'I type "{text}" into the text area')
def step_impl(context, text):
    context.page.set_text_area_id(text)


@when(u'I search for the text area by "{how}"')
def step_impl(context, how):
    method = 'text_area_{0}_element'.format(how)
    context.text_area = getattr(context.page, method)()


@when(u'I clear the text area')
def step_impl(context):
    context.page.text_area_id_element().clear()

@then(u'I should be able to type "{text}" into the area')
def step_impl(context, text):
    context.text_area.set_value(text)
    assert_that(context.text_area.get_value(), equal_to(text.strip()))

@then(u'the text area should contain "{text}"')
def step_impl(context, text):
    text_area = context.page.text_area_id_element()
    assert_that(text_area.get_value(), equal_to(text.strip()))
