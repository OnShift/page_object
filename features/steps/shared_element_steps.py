from hamcrest import assert_that, equal_to, contains_string


@then(u'the text should be "{expected_text}"')
def step_impl(context, expected_text):
    assert_that(context.expected_text, equal_to(expected_text))


@then(u'I should be on the success page')
def step_impl(context):
    assert_that(context.page.html, contains_string('Success'))
    assert_that(context.page.title, equal_to('Success'))
