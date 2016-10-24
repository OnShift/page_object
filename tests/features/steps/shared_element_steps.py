from hamcrest import assert_that, equal_to


@then(u'the text should be "{expected_text}"')
def step_impl(context, expected_text):
    assert_that(context.expected_text, equal_to(expected_text))
