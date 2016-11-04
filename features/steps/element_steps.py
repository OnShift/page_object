from hamcrest import assert_that, equal_to

@then(u'it should know it is enabled')
def step_impl(context):
    assert_that(context.element.is_enabled(), equal_to(True))


@then(u'it should know that is it not disabled')
def step_impl(context):
    assert_that(context.element.is_disabled(), equal_to(False))


@then(u'it should know it is not enabled')
def step_impl(context):
    assert_that(context.element.is_enabled(), equal_to(False))


@then(u'it should know that it is disabled')
def step_impl(context):
    assert_that(context.element.is_disabled(), equal_to(True))
