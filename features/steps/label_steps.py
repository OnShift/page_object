@when(u'I get the text from the label')
def step_impl(context):
    context.expected_text = context.page.label_id()

@when(u'I search for the label by "{how}"')
def step_impl(context, how):
    method = 'label_{0}'.format(how)
    context.expected_text = getattr(context.page, method)()
