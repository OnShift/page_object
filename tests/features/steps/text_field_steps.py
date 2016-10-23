from hamcrest import assert_that, equal_to

@when(u'I type "{text}" into the text field')
def step_impl(context, text):
    context.page.set_text_field_id(text)

@when(u'I clear the text field')
def step_impl(context):
    context.page.text_field_id_element().clear()

@then(u'the text field should contain "{expected_text}"')
def step_impl(context, expected_text):
    assert_that(context.page.text_field_id(), equal_to(expected_text.strip()))
