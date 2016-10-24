@when(u'I get the text from the paragraph')
def step_impl(context):
    context.expected_text = context.page.paragraph_id()


@when(u'I search for the paragraph by "{how}"')
def step_impl(context, how):
    method = 'paragraph_{0}'.format(how)
    context.expected_text = getattr(context.page, method)()
