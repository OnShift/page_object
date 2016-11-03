from hamcrest import assert_that, equal_to

@when(u'I click the button')
def step_impl(context):
    context.page.button_id()


@when(u'I search for the button by "{how}"')
def step_impl(context, how):
    method = 'button_{0}_element'.format(how)
    context.button = getattr(context.page, method)()


@when(u'I find a button while the script is executing')
def step_impl(context):
    context.button = context.page.button_element({'id': 'button_id'})


@then(u'I should be able to click the button')
def step_impl(context):
    context.button.click()


@then(u'I should see that the button exists')
def step_impl(context):
    assert_that(context.button.exists(), equal_to(True))
