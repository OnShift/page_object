from hamcrest import assert_that, equal_to


@given(u'I disable the button')
def step_impl(context):
    context.page.disable()
    context.page.wait(3)


@when(u'I enable the button')
def step_impl(context):
    context.page.enable()


@when(u'I create a new button')
def step_impl(context):
    context.page.create()


@then(u'I should be able to wait for the button to be enabled')
def step_impl(context):
    element = context.page.target_element()
    assert_that(element.is_enabled(), equal_to(False))
    element.when_enabled()
    assert_that(element.is_enabled(), equal_to(True))


@then(u'I should be able to wait for the button to be present')
def step_impl(context):
    element = context.page.new_element()
    assert_that(element.exists(), equal_to(False))
    element.when_present()
    assert_that(element.exists(), equal_to(True))
