from hamcrest import assert_that, equal_to


@when(u'I search for the text field by "{how}"')
def step_impl(context, how):
    method = 'text_field_{0}_element'.format(how)
    context.element = getattr(context.page, method)()


@when(u'I type "{text}" into the text field')
def step_impl(context, text):
    context.page.set_text_field_id(text)


@when(u'I clear the text field')
def step_impl(context):
    context.page.text_field_id_element().clear()


@then(u'the text field should contain "{expected_text}"')
def step_impl(context, expected_text):
    assert_that(context.page.text_field_id(), equal_to(expected_text.strip()))


@then(u'I should be able to type "{text}" into the field')
def step_impl(context, text):
    context.element.set_value(text)
    assert_that(context.element.get_value(), equal_to(text))
