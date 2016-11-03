@when(u'I get the text from the span')
def step_impl(context):
    context.expected_text = context.page.span_id()


@when(u'I search for the span by "{how}"')
def step_impl(context, how):
    method = 'span_{0}'.format(how)
    context.expected_text = getattr(context.page, method)()
