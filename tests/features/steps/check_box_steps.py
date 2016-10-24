from hamcrest import assert_that, equal_to


@when(u'I select the First check box')
def step_impl(context):
    context.page.check_cb_id()


@when(u'I unselect the First check box')
def step_impl(context):
    context.page.uncheck_cb_id()


@when(u'I search for the check box by "{how}"')
def step_impl(context, how):
    method = 'cb_{0}_element'.format(how)
    context.element = getattr(context.page, method)()

@then(u'the First check box should be selected')
def step_impl(context):
    assert_that(context.page.is_cb_id_checked(), equal_to(True))


@then(u'the First check box should not be selected')
def step_impl(context):
    assert_that(context.page.is_cb_id_checked(), equal_to(False))


@then(u'I should be able to check the check box')
def step_impl(context):
    context.element.check()
    assert_that(context.element.is_checked(), equal_to(True))
