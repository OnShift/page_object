@when(u'I click the button')
def step_impl(context):
    context.page.button_id()


@when(u'I search for the button by "{how}"')
def step_impl(context, how):
    method = 'button_{0}_element'.format(how)
    context.link = getattr(context.page, method)()


@then(u'I should be able to click the button')
def step_impl(context):
    context.link.click()
