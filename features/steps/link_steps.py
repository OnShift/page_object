from hamcrest import assert_that


@when(u'I select the link labeled "{link_text}"')
def step_impl(context, link_text):
    context.page.google_search_id()


@when(u'I search for the link by "{how}"')
def step_impl(context, how):
    method = 'google_search_{0}_element'.format(how)
    context.link = getattr(context.page, method)()


@then(u'I should be able to select the link')
def step_impl(context):
    context.link.click()
