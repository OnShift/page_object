@when(u'I get the text from the div')
def step_impl(context):
    context.expected_text = context.page.div_id()


@when(u'I search for the div by "{how}"')
def step_impl(context, how):
    method = 'div_{0}'.format(how)
    context.expected_text = getattr(context.page, method)()
